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

url="https://www.immoweb.be/en/classified/mixed-use-building/for-sale/liege/4000/9316691?"

driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Number of rooms -> int
rooms_and_area = soup.select('p.classified__information--property')[0].text
rooms = re.findall("([0-9]+)", rooms_and_area)[0]
print(rooms)

# TODO: Furnished -> boolean
furnished = soup.select('td.classified-table__data')[15].text.strip()
if furnished == "No":
    furnished = 0
elif furnished =="Yes":
    furnished = 1
else:
    furnished = None

print(furnished)
driver.close()