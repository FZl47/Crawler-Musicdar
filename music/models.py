from django.utils.crypto import get_random_string
from django.db import models
from django.conf import settings
from crawler.core.utils import slugify


class Music(models.Model):
    sku = models.CharField(max_length=30)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    picture = models.URLField(null=True, blank=True)
    singer = models.CharField(max_length=300, null=True, blank=True)
    category = models.CharField(max_length=300, null=True, blank=True)
    link_128 = models.URLField(null=True, blank=True)
    link_320 = models.URLField(null=True, blank=True)
    url_page = models.URLField()
    url_page_from_host = models.URLField(null=True)
    is_out = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Music - {self.title[:30]}'

    def get_slug(self):
        return slugify(self.title)

    def get_url_from_host(self):
        return self.url_page_from_host


