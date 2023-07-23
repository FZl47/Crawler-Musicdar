from django.contrib import admin
from . import models

admin.site.register(models.SiteModel)
admin.site.register(models.CategoryModel)
admin.site.register(models.MusicModel)
admin.site.register(models.AddMusics)
admin.site.register(models.AddMusicsCategoryState)
