from django.db import models


class UserQueue(models.Model):
    """記錄待寄信件"""
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='user_queue')
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
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='music_links')
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
