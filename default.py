import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

import matplotlib.font_manager as fm
import re
import collections

def data_create(width=0, hight=0, user=None, mask=''):
    url = f'https://www.google.com/search?q={user}'
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    text = soup.text

    # wordcloud excute code
    if mask == '':
        wc = WordCloud(max_font_size=200, font_path='./font/malgun.ttf',
                        background_color='white', width=width, height=hight)
    else:
        wc =WordCloud(max_font_size=200, font_path='./font/malgun.ttf',
                        background_color='white', width=width, height=hight
                        , mask=mask)

    wc.generate(text)
    return wc

def image_show(wc=None):
    # image create and show to window
    plt.figure(figsize=(10,8))
    plt.imshow(wc)
    plt.tight_layout(pad=0)
    plt.axis('off')
    plt.show()
