# -*- coding: utf-8 -*-
__author__ = 'SirHades696'
__email__ = 'djnonasrm@gmail.com'

import pandas as pd
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

__headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
__url = "https://pokemondb.net/pokedex/all"
__table = Request(url=__url,headers=__headers)
__url_open = urlopen(__table).read()
__data = pd.read_html(__url_open)
__data_pokemon = __data[0]
values = __data_pokemon.values.tolist()
__soup = BeautifulSoup(__url_open,"html.parser")
__imgs = __soup.find_all('span',{"class": "img-fixed icon-pkmn"})
# Replacing whitespace to 2 types
for __value in values:
    __value[2] = __value[2].replace(' ', '/')
# Extracting the img
__src = [__img['data-src'] for __img in __imgs]
# adding img to values
for __i, __value in enumerate(values):
    __value.append(__src[__i])
