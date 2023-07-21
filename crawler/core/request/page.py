import requests
from bs4 import BeautifulSoup


def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    req = requests.get(url, headers=headers)
    if req.status_code != 200:
        raise Exception('request is not success')
    return BeautifulSoup(req.content, 'html.parser')
