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

    # Extract window.dataLayer json from head / script K Y
    rawdataLayer = soup.head.find('script').find_next_sibling(
        'script').find_next_sibling('script').string

    # Clean the json and convert to dict
    rawdataLayer = rawdataLayer.replace(
        'window.dataLayer = [', '').replace('];', '')
    dataLayer = json.loads(rawdataLayer)
    print(rawdataLayer)

    # PRICE: Directly pick from the dataLayer K

    # Type of SALE -> string K
    h2 = soup.find_all(string='Public sale')
    if "Public sale" in h2:
        type_of_sale = "public"
    else:
        type_of_sale = "private"

    # Number of rooms -> int J
    rooms_and_area = soup.select('p.classified__information--property')[0].text
    rooms = re.findall("([0-9]+)", rooms_and_area)[0]

    # Area -> int J
    area = re.findall("([0-9]+)", rooms_and_area)[1]

    # Fully equipped kitchen -> boolean (Directly pick from the dataLayer) K

    # TODO: Furnished -> boolean

    # Open fire -> boolean K
    th_fire = soup.find('th', string='How many fireplaces?')
    nb_fire = th_fire.find_next_sibling('td').contents[0]
    open_fire = nb_fire if th_fire else 0

    # Terrace -> Boolean if True: Area -> int K
    if dataLayer["classified"]["outdoor"]["terrace"]["exists"]:
        th_terrace = soup.find('th', string='Terrace surface')
        terrace_surface = th_terrace.find_next_sibling(
            'td').contents[0].strip()
        terrace = int(terrace_surface)
    else:
        terrace = 0

    # Garden -> Boolean if True: Area -> int K
    garden_surface = dataLayer["classified"]["outdoor"]["garden"]["surface"]
    if garden_surface:
        garden = int(garden_surface)
    else:
        garden = 0

    # Surface of the land -> int K J
    surface_land = None
    if dataLayer["classified"]["land"]["surface"]:
        surface_land = int(dataLayer["classified"]["land"]["surface"])

    # surface_land = soup.select('span.overview__text')[3].text
    # surface_land = re.findall("([0-9]+)", surface_land)[0]

    # TODO: Number of facades -> int Jess

    # Swimming pool -> boolean K
    if dataLayer["classified"]["wellnessEquipment"]["hasSwimmingPool"]:
        hasSwimmingPool = True
    else:
        hasSwimmingPool = False

    # State of the building (New, to be renovated, ...) -> string (dataLayer)

    # TODO: Cleaning

    # TODO: Finalizing

    # MERGE ALL INFOS in a DICT to return

    d = {
        'id': int(dataLayer["classified"]["id"]),
        'type_of_property': dataLayer["classified"]["type"],
        'subtype_of_property': dataLayer["classified"]["subtype"],
        'locality': int(dataLayer["classified"]["zip"]),
        'price': int(dataLayer["classified"]["price"]),
        'type_of_sale': type_of_sale,
        'rooms': int(rooms),
        'condition': dataLayer["classified"]["building"]["condition"],
        'equipped_kitchen': dataLayer["classified"]["kitchen"]["type"],
        'terrace': terrace,
        'garden': garden,
        'open_fire': open_fire,
        'hasSwimmingPool': hasSwimmingPool,
        'living_area_m2': int(area),
        'surface_of_land_m2': surface_land
    }
    driver.quit()
    return d

# example


# url = 'https://www.immoweb.be/en/classified/penthouse/for-sale/ixelles/1050/9311762?searchId=6092970dc6b31'
url = 'https://www.immoweb.be/en/classified/house/for-sale/elst/9660/9314233?searchId=60929b83865c1'
infos_in_url = urlparseimmo(url)

print(infos_in_url)
