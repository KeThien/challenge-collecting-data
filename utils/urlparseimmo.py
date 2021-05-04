from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
import json
import requests
import re

driver = webdriver.Chrome()


def urlparseimmo(url) -> dict:
    '''
    Function to parse all info into a dict
    '''

    # Beautifulsoup to get the rest of the info
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Extract window.dataLayer json from head / script
    rawdataLayer = soup.head.find('script').find_next_sibling(
        'script').find_next_sibling('script').string

    # Clean the json and convert to dict
    rawdataLayer = rawdataLayer.replace(
        'window.dataLayer = [', '').replace('];', '')
    dataLayer = json.loads(rawdataLayer)
    print(rawdataLayer)
    # Parse element in the URL
    parsed = urlparse(url)

    # parsing split segment from the URL
    segments = parsed.path[1:-1].split("/")

    # PRICE: Directly pick from the dataLayer

    # TODO: Type of SALE -> string
    h2 = soup.find_all(string='Public sale')
    print(h2)
    if "Public sale" in h2:
        print("Yes public sale")
    else:
        print("No private")
    # TODO: Number of rooms -> int
    rooms_and_area = soup.select('p.classified__information--property')[0].text
    rooms = re.findall("([0-9]+)",rooms_and_area)[0]
    
   
    # TODO: Area -> int
    area = re.findall("([0-9]+)",rooms_and_area)[1]
    

    # TODO: Fully equipped kitchen -> boolean
   

    # TODO: Furnished -> boolean
    interior = soup.find('table', class_="classified-table")
    print(interior.prettify() )
    

    # TODO: Open fire -> boolean

    # TODO: Terrace -> Boolean if True: Area -> int

    # TODO: Garden -> Boolean if True: Area -> int

    # TODO: Surface of the land -> int

    # TODO: Surface area of the plot of land -> int

    # TODO: Number of facades -> int

    # TODO: Swimming pool -> boolean

    # TODO: State of the building (New, to be renovated, ...) -> string

    # TODO: Cleaning

    # TODO: Finalizing

    # MERGE ALL INFOS in a DICT to return
 
    d = {
        'id': int(dataLayer["classified"]["id"]),
        'locality': int(dataLayer["classified"]["zip"]),
        'subtype_of_property': dataLayer["classified"]["subtype"],
        'type_of_property': dataLayer["classified"]["type"],
        'price': int(dataLayer["classified"]["price"])
    }
    driver.quit()
    return d


# example

url = 'https://www.immoweb.be/en/classified/house/for-sale/couthuin/4218/9312278?searchId=60910580c4321'

infos_in_url = urlparseimmo(url)

print(infos_in_url)
