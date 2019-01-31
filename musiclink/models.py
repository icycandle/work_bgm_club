from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class UserQueue(models.Model):
    """記錄待寄信件"""
    user = models.ForeignKey('musiclink.User', on_delete=models.CASCADE, related_name='user_queue')
    jobtype = models.CharField('jobtype', max_length=32, db_index=True)
    create_at = models.DateTimeField('create_at', auto_now_add=True)

    class Meta:
        verbose_name = 'UserQueue'
        verbose_name_plural = 'UserQueues'

    def __str__(self):
        return '{0.user_id}-{0.jobtype}-{0.create_at}'.format(self)


class LinkQueue(models.Model):
    """記錄待寄信件"""
    musiclink = models.ForeignKey('musiclink.MusicLink', on_delete=models.CASCADE, related_name='link_queue')
    jobtype = models.CharField('jobtype', max_length=32, db_index=True)
    create_at = models.DateTimeField('create_at', auto_now_add=True)

    class Meta:
        verbose_name = 'LinkQueue'
        verbose_name_plural = 'LinkQueues'

    def __str__(self):
        return '{0.musiclink_id}-{0.jobtype}-{0.create_at}'.format(self)


class MusicLink(models.Model):
    """Model definition for MusicLink."""
    user = models.ForeignKey('musiclink.User', on_delete=models.CASCADE, related_name='music_links')
    url = models.URLField('url', max_length=255)
    jobtype = models.CharField('jobtype', max_length=32, db_index=True)
    comment = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField('create_at', auto_now_add=True)

    def get_absolute_url(self):
        return '/#/bgm/{}'.format(self.pk)

    def save(self, *args, **kwargs):
        just_created = True if not self.pk else False
        super().save(*args, **kwargs)
        if just_created:
            # record user to user queue
            UserQueue.objects.create(user=self.user, jobtype=self.jobtype)

    class Meta:
        verbose_name = 'MusicLink'
        verbose_name_plural = 'MusicLinks'

    def __str__(self):
        return '{0.user.email}-{0.jobtype}-{0.url}'.format(self)

FEEDBACK_VALUE_CHOICES = (
    (1, '喜歡'),
    (0, '不喜歡'),
    (-1, '這不是音樂！'),
)

class MusicRating(models.Model):
    """Model definition for Feedback."""
    user = models.ForeignKey('musiclink.User', on_delete=models.CASCADE, related_name='music_rating')
    musiclink = models.ForeignKey('musiclink.MusicLink', on_delete=models.CASCADE, related_name='music_rating')
    value = models.IntegerField('value', choices=FEEDBACK_VALUE_CHOICES)
    create_at = models.DateTimeField('create_at', auto_now_add=True)

    class Meta:
        """Meta definition for Feedback."""
        unique_together = (
            ('user', 'musiclink'),
        )

        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

    def __str__(self):
        return '{0.user}-{0.musiclink}: {0.value}'.format(self)
