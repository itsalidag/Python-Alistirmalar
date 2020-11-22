import pandas as pd
import requests
from bs4 import BeautifulSoup

url = r"https://twitter.com/search?q=Be%C5%9Fikta%C5%9F&src=trend_click&vertical=trends"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

tweets = soup.find_all("span", class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")

for tweet in tweets:
    each = tweet.text
    print(each)