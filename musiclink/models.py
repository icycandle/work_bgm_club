from django.db import models


class MusicLink(models.Model):
    """Model definition for MusicLink."""
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='music_links')
    url = models.URLField('url', max_length=255)
    jobtype = models.CharField('jobtype', max_length=32, db_index=True)
    comment = models.TextField(null=True)

    class Meta:
        """Meta definition for MusicLink."""
        verbose_name = 'MusicLink'
        verbose_name_plural = 'MusicLinks'

    def __str__(self):
        return '{0.user.email}-{0.jobtype}-{0.url}'.format(self)
