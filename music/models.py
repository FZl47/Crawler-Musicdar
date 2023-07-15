from django.db import models


class Music(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    picture = models.URLField(null=True)
    singer = models.CharField(max_length=200, null=True)
    categories = models.CharField(max_length=300, null=True, help_text='بر اساس | باید جدا شوند')
    link_128 = models.URLField(null=True)
    link_320 = models.URLField(null=True)
    url_page = models.URLField()
    is_out = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Music - {self.title[:30]}'
