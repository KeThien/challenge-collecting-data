import requests
import csv
import time
from selenium import webdriver
from parsel import Selector
import concurrent.futures
from bs4 import BeautifulSoup
from functions_extract_url import * 
from utils.urlparsimmo.py import urlparseimmo

PATH = "/opt/chromedriver" 
# driver = webdriver.Chrome(PATH)

url = "https://www.immoweb.be/en/classified/mixed-use-building/for-sale/liege/4000/9316691?"

infos_in_url = urlparseimmo(url)

print(infos_in_url)

# driver.get(url)
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')

# # Number of rooms -> int
# rooms_and_area = soup.select('p.classified__information--property')[0].text
# rooms = re.findall("([0-9]+)", rooms_and_area)[0]
# print(rooms)



# #Furnished -> boolean
# furnished = soup.find("th", string = "Furnished")
# furnished = furnished.find_next_sibling().contents[0].strip()
# print(furnished)

