import requests
import csv
import time
from selenium import webdriver
from parsel import Selector
import concurrent.futures
from functions_extract_url import * #personnal function
from bs4 import BeautifulSoup

PATH = "/opt/chromedriver" 
driver = webdriver.Chrome(PATH)

url = "https://www.immoweb.be/en/classified/mixed-use-building/for-sale/liege/4000/9316691?"
# url = "https://www.immoweb.be/en/classified/house/for-sale/sint-pieters-leeuw/1600/9310259?searchId=60929f813c19a" 

driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# # Number of rooms -> int
# rooms_and_area = soup.select('p.classified__information--property')[0].text
# rooms = re.findall("([0-9]+)", rooms_and_area)[0]
# print(rooms)

#Furnished -> boolean
try:
    furnished = soup.find("th", string = "Furnished")
    furnished = furnished.find_next_sibling().contents[0].strip()
    if furnished == "No":
        furnished = 0
    else:
        furnished = 1
except:
    furnished = None

# TODO: Number of facades -> int Jess
# facades = soup.find("th", string = "Furnished")
# facades = facades.find_next_sibling().contents[0].strip()
# print(furnished)


driver.close()