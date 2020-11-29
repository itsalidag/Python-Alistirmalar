# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 20:25:27 2020

@author: alida
"""

#weeklyosm scraper

import requests
from bs4 import BeautifulSoup
import os
from gtts import gTTS

def osmspeaker(pagenum):
    base_url = 'https://weeklyosm.eu/tr/page/'
    url = base_url + str(pagenum)
    response = requests.get(url)
    soup = BeautifulSoup(response.text ,features="lxml")

    metin = soup.find_all("ul")
    mesaj = ""
    for i in metin:
        icerik = i.find("li")
        a = icerik.text
        mesaj += str(a)
    obje = gTTS(text = mesaj, lang="tr",slow = False)
    obje.save("weeklyosmpage{}.mp3".format(str(pagenum)))




for i in range(2,30):
    osmspeaker(i)

