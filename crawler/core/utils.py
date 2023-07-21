import datetime
from django.conf import settings
from crawler.models import SiteModel

_replace_words = SiteModel.objects.exclude(replace_labels=None).values_list('replace_labels',flat=True)
_replace_words = list(map(lambda i: str(i.split('|')),_replace_words))


def normalize_num(num):
    num = str(num).replace(',', '').replace('-', '')
    return int(num)


def normalize_text(text, remove_words=[]):
    text = replace_words_labels(text)
    remove_words = remove_words or []
    res = ' '.join(filter(lambda x: x.lower() not in remove_words, text.split()))
    return res


def normalize_title(text, remove_words=[]):
    text = replace_words_labels(text)
    remove_words = remove_words or []
    remove_words.extend(settings.WP_CONFIG['REMOVE_WORDS_FROM_TITLE'])
    return normalize_text(text,remove_words)


def replace_words_labels(text):
    for word in _replace_words:
        text.replace(word, settings.WP_CONFIG['TITLE'])
    return text


def slugify(text):
    return text.replace(' ','-')


def get_time():
    return datetime.datetime.now()