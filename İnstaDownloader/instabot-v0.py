#instaphotodown.
import requests
from bs4 import BeautifulSoup

base_url = "https://www.instagram.com/@"
userin = input("Username to get images: ")
goto = base_url + userin
response = requests.get(goto)
soup = BeautifulSoup(response.content, "html.parser")

images = soup.find("div", attrs={"class" : " _2z6nI"})
print(images)