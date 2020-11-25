#basic scraper
from bs4 import BeautifulSoup
import requests

url = "https://tr.wikiquote.org/wiki/Mustafa_Kemal_Atat%C3%BCrk"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

sozler = soup.find_all("ul")

for i in sozler:
    print(i.text)