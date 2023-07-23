import requests
from django.conf import settings

api_conf = settings.SITE_CONFIG['API']
api_endpoints = api_conf['ENDPOINTS']


def create_music(music_obj):
    data = {
        'name': music_obj.title,
        'link_320': music_obj.link_320,
        'link_128': music_obj.link_128,
        'content': music_obj.description,
        'cover_url': music_obj.picture,
        'artist_name': music_obj.singer,
        'category_name': music_obj.category,
        'duration':'0'
    }
    response = requests.post(api_endpoints['music'], data=data)
    if response.status_code == 201:
        return response.json()
    return None