# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 22:23:32 2020

@author: alida
"""

import requests
from bs4 import BeautifulSoup


url= "https://twitter.com/search?q=%23kpssonlisans2020&src=trend_click&vertical=trends"

response = requests.get(url)
soup = BeautifulSoup(response, "html.parser")

article = soup.find("span", {"class":"css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"})
print(article)