from django.db import models
from django.utils import timesince
from django.conf import settings
from . import utils


class Log(models.Model):
    LEVEL_OPTIONS = (
        ('DEBUG', 'DEBUG'),
        ('INFO', 'INFO'),
        ('WARNING', 'WARNING'),
        ('ERROR', 'ERROR'),
    )

    title = models.CharField(max_length=200)
    level = models.CharField(max_length=10, choices=LEVEL_OPTIONS)
    description = models.TextField(null=True,blank=True)
    checked_note = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_checked = models.BooleanField(default=False)

    class Meta:
        ordering = ('-id',)

    def save(self, *args, **kwargs):
        super(Log, self).save(*args, **kwargs)
        utils.log_write(self)
        if self.level in settings.LOG_CONFIG['email_levels']:
            utils.send_email(self.title, self.content)

    def __str__(self):
        return f'#{self.id} -l {self.level} - {self.get_time_past()} ago'

    @property
    def content(self):
        return f"""
            \n
            #{self.id} -l {self.level} - {self.title}\n
            {self.description or 'no description'}
            {self.created_at}
            \n        
        """.strip()

    def get_time_past(self):
        return timesince.timesince(self.created_at)
