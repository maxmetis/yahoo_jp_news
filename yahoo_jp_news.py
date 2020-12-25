# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 08:21:49 2020

@author: Johnny Tsai
"""


import requests
from bs4 import BeautifulSoup

def yahoo_jp():
    url = 'https://news.yahoo.co.jp/topics/top-picks'
    headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4122.7 Mobile Safari/537.36'}

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    title = [title_item.text for title_item in soup.find_all('div', class_='newsFeed_item_title')][:5]
    link = [link_item.get('href') for link_item in soup.find_all('a', class_='newsFeed_item_link')][:5]
    img = [img_item.get('src') for img_item in soup.find_all('img', loading='lazy')][:5]
    
    return title, link, img
