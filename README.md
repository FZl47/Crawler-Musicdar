# Crawler-Musicdar
Crawler for site 'musicdar.ir'


### TODO :
    - [ ] create base models crawler
    - [ ] remove category pages - pages geted(use count musics / per music in page)
    - [ ] set exception logs



#### Note:

    موردی ک باید به ان توجه شود زمانی ک موزیکی را حذف میکنیم همان موزیک در سایت هاست حذف میشود
    برای اعمال این عملکرد به درستی باید از فانکشنی که برای حذف موزیک ها ایحاد شده است استفاده کرد
    
    مشکل : اگر به صورت عملیات حذف در QueryDict انجام شود از متود حذف دیگری استفاده میکند که برای عملیات حذف محصول در سایت هاست تنظیم نشده است
    مثال : foo.objects.delete()
    
    برای حل این مشکل باید به صورت تک به تک روی ابجکت ها ایتریت زد و عملیات حذف رو اعمال کرد