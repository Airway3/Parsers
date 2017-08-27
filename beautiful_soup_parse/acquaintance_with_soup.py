#!/usr/bin/env python3

import os
import urllib.request
from bs4 import BeautifulSoup as BS


BASE_URL = 'https://www.youtube.com/watch?v=kNGHvuSNNpY&list=PLRQ6TOHo3O4-5vP6soFnxBxFOtO-i7E8U'


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def parse(html):
    soup = BS(html, "html.parser")
    ol = soup.find('ol', id='playlist-autoscroll-list').find_all('h4')

    titles = [title.text.strip() for title in ol]
    print(titles)


def main():
    parse(get_html(BASE_URL))


if __name__ == '__main__':
    main()