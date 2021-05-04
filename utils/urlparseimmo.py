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

    # PRICE: Directly pick from the dataLayer

    # Type of SALE -> string
    h2 = soup.find_all(string='Public sale')
    print(h2)
    if "Public sale" in h2:
        type_of_sale = "public"
    else:
        type_of_sale = "private"

    # TODO: Number of rooms -> int Jess

    # TODO: Area -> int Jess

    # Fully equipped kitchen -> boolean (Directly pick from the dataLayer)

    # TODO: Furnished -> boolean

    # TODO: Open fire -> boolean

    # TODO: Terrace -> Boolean if True: Area -> int
    if dataLayer["classified"]["outdoor"]["terrace"]["exists"]:
        th_terrace = soup.find('th', string='Terrace surface')
        terrace_surface = th_terrace.find_next_sibling(
            'td').contents[0].strip()

        terrace = int(terrace_surface)
    else:
        terrace = None
    # TODO: Garden -> Boolean if True: Area -> int

    # TODO: Surface of the land -> int

    # TODO: Surface area of the plot of land -> int

    # TODO: Number of facades -> int Jess

    # Swimming pool -> boolean
    if dataLayer["classified"]["wellnessEquipment"]["hasSwimmingPool"]:
        hasSwimmingPool = True
    else:
        hasSwimmingPool = False

    # State of the building (New, to be renovated, ...) -> string

    # TODO: Cleaning

    # TODO: Finalizing

    # MERGE ALL INFOS in a DICT to return
    d = {
        'id': int(dataLayer["classified"]["id"]),
        'locality': int(dataLayer["classified"]["zip"]),
        'subtype_of_property': dataLayer["classified"]["subtype"],
        'type_of_property': dataLayer["classified"]["type"],
        'price': int(dataLayer["classified"]["price"]),
        'type_of_sale': type_of_sale,
        'hasSwimmingPool': hasSwimmingPool,
        'condition': dataLayer["classified"]["building"]["condition"],
        'equipped_kitchen': dataLayer["classified"]["kitchen"]["type"],
        'terrace': terrace
    }
    driver.quit()
    return d


# example

url = 'https://www.immoweb.be/en/classified/triplex/for-sale/buizingen/1501/9309298?searchId=60915769a0d6e'

infos_in_url = urlparseimmo(url)

print(infos_in_url)
