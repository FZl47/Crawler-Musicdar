from .get import select, selects
from crawler.core.utils import normalize_num, normalize_title


def last_page_num(page, category):
    selector = category.get_page_last_by
    return normalize_num(select(page, selector).text)


def musics(page, category):
    selector = category.get_music_by
    return selects(page, selector)


def musics_count(page, category):
    return len(musics(page, category))


# Music Model Field

def title(page, music_model):
    selector = music_model.get_title_by
    if selector:
        return normalize_title(select(page, selector).text)


def picture(page, music_model):
    selector = music_model.get_picture_by
    if selector:
        key_element = music_model.key_picture
        res = select(page, selector)
        if res:
            return res[key_element]


def link_128(page, music_model):
    selector = music_model.get_128_by
    if selector:
        key_element = music_model.key_link_128
        res = select(page, selector)
        if res:
            return res[key_element]


def link_320(page, music_model):
    selector = music_model.get_320_by
    if selector:
        key_element = music_model.key_link_320
        res = select(page, selector)
        if res:
            return res[key_element]


def singer(page, music_model):
    selector = music_model.get_singer_by
    if selector:
        key_element = music_model.key_singer
        res = select(page, selector)
        if res:
            if key_element == 'text':
                return res.text
            return res[key_element]


def category(page, music_model):
    selector = music_model.get_category_by
    if selector:
        key_element = music_model.key_category
        res = select(page, selector)
        if res:
            if key_element == 'text':
                return res.text
            return res[key_element]
