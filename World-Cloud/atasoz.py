#basic scraper
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://tr.wikiquote.org/wiki/Mustafa_Kemal_Atat%C3%BCrk"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

sozler = soup.find_all("ul")
atasoz = []
for i in sozler:
    atasoz.append(i.text)
    
kelime = []
for i in atasoz:
    spli = i.split(" ")
    for i in spli:
        kelime.append(i)
        
        
#kel = pd.DataFrame(data = kelime, columns = ["kelime"])
#kel.to("kelimeler.xlsx", sheet_name='Sheet_name_1')

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt #to display our wordcloud
from PIL import Image #to load our image
import numpy as np #to get the color of our image


StopWords = ["için", "çok", "en","ne","de","ile","gibi"]
mask = np.array(Image.open("ata.png"))
file = open("kelimeler.txt", encoding="utf8").read()
wc = WordCloud(background_color="white",
               mask=mask, stopwords= StopWords,
               height=10000,width=15000)
wc.generate(file)   
image_colors = ImageColorGenerator(mask)
wc.recolor(color_func=image_colors)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.savefig("test2.pdf")
plt.show()
