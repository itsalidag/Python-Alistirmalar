import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame

url = "https://tr.wiktionary.org/wiki/Vikis%C3%B6zl%C3%BCk:T%C3%BCrk%C3%A7e_temel_s%C3%B6zl%C3%BCk"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

#get the words

word = soup.find("div", attrs={"class": "mw-parser-output"})

liler = []

li=  word.find_all("li")
for li in li:
    print(li.text)
    print("+"*50)
    liler.append(li.text)

df = DataFrame(liler)
print(df.colums)