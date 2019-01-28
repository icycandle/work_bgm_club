from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from musiclink.models import MusicLink, UserQueue, LinkQueue
from musiclink.mail import send_email


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
        to_email = user_from_queue.user.email
        subject = '來自背景音樂俱樂部的「{0.jobtype}」音樂 #{0.id}'.format(musiclink)
        send_email(
            subject=subject,
            from_email='service@dwave.cc',
            to_email=to_email,
            template='mail_template.html',
            context={
                'subject': subject,
                'musiclink': musiclink,
                'site': 'https://workbgmclub.wearetags.com',
            }
        )
        user_from_queue.delete()
    else:
        #代表現在暫時沒有適合的使用者可寄，儲存至 LinkQueue
        LinkQueue.objects.create(
            musiclink=musiclink,
            jobtype=musiclink.jobtype,
        )
