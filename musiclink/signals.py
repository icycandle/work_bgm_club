from allauth.account.models import EmailAddress
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.db.models.signals import post_save
from django.dispatch import Signal, receiver

from musiclink.mail import send_email
from musiclink.models import LinkQueue, MusicLink, UserQueue, User

admin_action_send_music_email_to_user = Signal(providing_args=["user"])

@receiver(admin_action_send_music_email_to_user, sender=User)
def admin_action_send_music_email_to_user_(sender, user, **kwargs):
    seed_musiclink = user.music_links.last()
    if not seed_musiclink:
        return (False, '{user} seed_musiclink not found.'.format(user=user))
    same_type_musiclink = MusicLink.objects.filter(
        jobtype=seed_musiclink.jobtype,
        pk__gt=seed_musiclink.pk,  # get newer
    ).exclude(user=user)
    if same_type_musiclink:
        musiclink = same_type_musiclink.order_by('?')[0]
        send_music_email_to_user(user, musiclink)
        return (True, '{user} action done.'.format(user=user))
    else:
        return (False, '{user} same_type_musiclink not found.'.format(user=user))

def send_music_email_to_user(user, musiclink):
    to_emails = EmailAddress.objects.filter(user=user).values_list('email', flat=True)
    subject = '來自背景音樂俱樂部的「{0.jobtype}」音樂 #{0.id}'.format(musiclink)
    site = 'https://' + get_current_site(None).domain
    send_email(
        subject=subject,
        from_email='service@dwave.cc',
        to_emails=list(to_emails),
        template='mail_template.html',
        context={
            'user': user,
            'subject': subject,
            'musiclink': musiclink,
            'site': site,
        }
    )

@receiver(post_save, sender=MusicLink)
def send_music_link_email(sender, **kwargs):
    '''
    新的 musiclink 會寄給舊的使用者。沒有的話則加入待寄清單。
    這邊只會消耗UserQueue， LinkQueue 要交給 celery beat 消耗
    situation 1: uo lo > send
    situation 2: uo lx > save u
    situation 3: ux lo > save l
    situation 4: ux lx > save u & save l
    '''
    musiclink = kwargs['instance']
    jobtype = musiclink.jobtype

    user_from_queue = UserQueue.objects.filter(
        jobtype=jobtype,
    ).exclude(
        user=musiclink.user,
    ).order_by('create_at').first()
    if user_from_queue:
        # 代表有東西可寄了
        user = user_from_queue.user
        send_music_email_to_user(user, musiclink)
        user_from_queue.delete()
    else:
        #代表現在暫時沒有適合的使用者可寄，儲存至 LinkQueue
        LinkQueue.objects.create(
            musiclink=musiclink,
            jobtype=musiclink.jobtype,
        )
