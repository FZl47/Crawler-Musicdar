from django.db import models


# Models for get and crawl
class SiteModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    domain = models.CharField(max_length=150)
    url_musics = models.URLField(help_text='ادرس صفحه ای که موزیک ها در ان وجود دارند')
    count_music_geted = models.PositiveBigIntegerField(default=0,
                                                       help_text='تعداد اهنگ هایی ک از این سایت گرفته شده است')
    count_pages = models.PositiveBigIntegerField(default=0, help_text='تعداد صفحه های اهنگ(Pages)')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name[:30]


class MusicsModel(models.Model):
    """
        Get elements by (CSS Selectors)
    """
    site = models.OneToOneField('SiteModel', on_delete=models.CASCADE)
    get_music_by = models.TextField(help_text='گرفتن موزیک ها بر اساس')

    def __str__(self):
        return f'Musics - {self.site}'


class MusicModel(models.Model):
    """
        Get elements by (CSS Selectors)
    """
    site = models.ForeignKey('SiteModel', on_delete=models.CASCADE)
    musics = models.ForeignKey('MusicsModel', on_delete=models.SET_NULL, null=True)
    get_title_by = models.TextField(help_text='گرفتن عنوان موزیک بر اساس', null=True)
    get_picture_by = models.TextField(help_text='گرفتن عکس موزیک بر اساس', null=True)
    get_128_by = models.TextField(help_text='گرفتن موزیک با کیفیت 128 بر اساس', null=True)
    get_320_by = models.TextField(help_text='گرفتن موزیک با کیفیت 320 بر اساس', null=True)
    get_singer_by = models.TextField(help_text='گرفتن خواننده بر اساس', null=True)
    get_category_by = models.TextField(help_text='گرفتن دسته بندی بر اساس', null=True)

    def __str__(self):
        return f'Music - {self.site}'
