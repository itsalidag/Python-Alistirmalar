from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
import requests

url = 'http://instagram.com/natgeo6/'
driver = webdriver.Firefox()
driver.get(url)

soup = BeautifulSoup(driver.page_source, features="lxml")
a = 0
for x in soup.findAll('div'):
    print(a)
    print(x)
    a +=1
