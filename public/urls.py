from django.urls import path
from . import views

app_name = 'public'
urlpatterns = [
    path('', views.home, name='home'),
    path('start-crawl', views.start_crawl, name='start_crawl'),
    path('pause-crawl', views.pause_crawl, name='pause_crawl'),
    path('continue-crawl', views.continue_crawl, name='continue_crawl'),
    path('delete-crawl', views.delete_crawl, name='delete_crawl'),


    path('tes', views.test, name='test'),
]
