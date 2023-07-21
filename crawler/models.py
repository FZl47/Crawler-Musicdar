from django.db import models
from django.db.models import Sum
from config import celery_app


# Models for get and crawl
class SiteModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    domain = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    replace_labels = models.CharField(max_length=400, null=True, blank=True, help_text='با استفاده از | جداشوند')

    def __str__(self):
        return self.name[:30]

    def get_count_musics_geted(self):
        return self.categorymodel_set.aggregate(count=Sum('count_music_geted'))['count']

    def get_count_pages_geted(self):
        return self.categorymodel_set.aggregate(count=Sum('count_pages_geted'))['count']

    def get_categories(self):
        return self.categorymodel_set.filter(is_active=True)

    def get_categories_add_state(self):
        categories = self.get_categories()

        return list(map(lambda i: i.category_state, categories))

    def has_categories_add_state(self):
        categories = self.categorymodel_set.exclude(category_state=None).count()
        return bool(categories)


class CategoryModel(models.Model):
    """
        Get elements by (CSS Selectors)
    """
    site = models.ForeignKey('SiteModel', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='_all_')
    count_music_geted = models.PositiveBigIntegerField(default=0,
                                                       help_text='تعداد اهنگ هایی ک از این دسته بندی گرفته شده است')
    count_pages_geted = models.PositiveBigIntegerField(default=0, help_text='تعداد صفحه های اهنگ(Pages) گرفته شده')
    count_music_per_page = models.PositiveIntegerField(help_text='تعداد موزیک ها در هر صفحه')
    url_musics = models.URLField(help_text='ادرس صفحه ای که موزیک ها در ان وجود دارند')
    get_music_by = models.TextField(help_text='گرفتن موزیک ها بر اساس')
    get_page_first_by = models.TextField(help_text='گرفتن اولین صفحه بر اساس')
    get_page_last_by = models.TextField(help_text='گرفتن اخرین صفحه بر اساس')
    get_page_url_by_format = models.TextField(
        help_text="""
            گرفتن ادرس صفحه بر اساس فرمت 
             به عنوان مثال : google.com/pages/{}
              باید با آکولاد مکان عدد صفحه مشخص شود
        """)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Musics - {self.site}'


class MusicModel(models.Model):
    """
        Get elements by (CSS Selectors)
    """
    site = models.OneToOneField('SiteModel', on_delete=models.CASCADE)
    category = models.OneToOneField('CategoryModel', on_delete=models.CASCADE)
    get_title_by = models.TextField(help_text='گرفتن عنوان موزیک بر اساس', null=True, blank=True)
    get_picture_by = models.TextField(help_text='گرفتن عکس موزیک بر اساس', null=True, blank=True)
    get_128_by = models.TextField(help_text='گرفتن موزیک با کیفیت 128 بر اساس', null=True, blank=True)
    get_320_by = models.TextField(help_text='گرفتن موزیک با کیفیت 320 بر اساس', null=True, blank=True)
    get_singer_by = models.TextField(help_text='گرفتن خواننده بر اساس', null=True, blank=True)
    get_category_by = models.TextField(help_text='گرفتن دسته بندی بر اساس', null=True, blank=True)

    key_picture = models.CharField(max_length=200,default='src',help_text='کلید مقدار المان عکس')
    key_link_128 = models.CharField(max_length=200,default='href',help_text='کلید مقدار المان اهنگ 128')
    key_link_320 = models.CharField(max_length=200,default='href',help_text='کلید مقدار المان اهنگ 320')
    key_singer = models.CharField(max_length=200,default='text',help_text='کلید مقدار المان خواننده')
    key_category = models.CharField(max_length=200,default='text',help_text='کلید مقدار المان دسته بندی')

    def __str__(self):
        return f'Music - {self.category}'


class AddMusics(models.Model):
    task_id = models.CharField(max_length=200, null=True)
    sites = models.ManyToManyField('SiteModel')
    is_running = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'#{self.id} Add music'

    def delete(self, *args, **kwargs):
        for site in self.sites.all():
            for category in site.categorymodel_set.all():
                try:
                    category.category_state.delete()
                except:
                    # RelatedObjectDoesNotExist
                    pass
        self.delete_task()
        super(AddMusics, self).delete(*args, **kwargs)

    def delete_task(self):
        celery_app.control.revoke(self.task_id, terminate=True)


class AddMusicsCategoryState(models.Model):
    category = models.OneToOneField('CategoryModel', on_delete=models.CASCADE, related_name='category_state')
    new_pages = models.CharField(max_length=20)
    new_musics = models.CharField(max_length=20)
    new_pages_geted = models.PositiveBigIntegerField(default=0)
    new_musics_geted = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'#{self.id} Add music category state'


class HistoryAdd(models.Model):
    add = models.ForeignKey('AddMusics', on_delete=models.CASCADE)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'History - {self.add}'
