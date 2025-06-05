from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

r = requests.get('https://home.ss.ge/ka/udzravi-qoneba/l/bina/iyideba?realEstateStatuses=2&cityIdList=95&subdistrictIds=47&areaFrom=50&areaTo=70&currencyId=2&priceType=1&priceFrom=100000&priceTo=150000&page=1')
soup = BeautifulSoup(r.text,'html.parser')
pretty_soup = soup.prettify()
print(type("1"))
