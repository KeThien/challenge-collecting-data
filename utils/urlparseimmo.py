from selenium import webdriver
from bs4 import BeautifulSoup
import json
import requests
import re

PATH = "/opt/chromedriver"
driver = webdriver.Chrome(PATH)


def urlparseimmo(url) -> dict:
    '''
    Function to parse all info into a dict
    '''
    # Beautifulsoup to get the rest of the info
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Extract window.dataLayer json from head / script K Y
    try:
        rawdataLayer = soup.head.find('script').find_next_sibling('script').find_next_sibling('script').string

        # Clean the json and convert to dict
        rawdataLayer = rawdataLayer.replace(
            'window.dataLayer = [', '').replace('];', '')
        dataLayer = json.loads(rawdataLayer)


        # PRICE: Directly pick from the dataLayer K

        # Type of SALE -> string K
        try:
            h2 = soup.find_all(string='Public sale')
            if "Public sale" in h2:
                type_of_sale = "public"
            else:
                type_of_sale = "private"
        except:
            type_of_sale = None

        # Number of rooms -> int J
        try:
            rooms_and_area = soup.select('p.classified__information--property')[0].text
            rooms = re.findall("([0-9]+)", rooms_and_area)[0]
        except:
            rooms = None
        # Area -> int J
        area = re.findall("([0-9]+)", rooms_and_area)[1]

        # Fully equipped kitchen -> boolean (Directly pick from the dataLayer) K

        # Furnished -> boolean
        try:
            furnished = soup.find("th", string="Furnished")  # None
            furnished = furnished.find_next_sibling().contents[0].strip()
            if furnished == "No":
                furnished = 0
            elif furnished == "Yes":
                furnished = 1
        except:
            furnished = None

        # Open fire -> boolean K
        try:
            h_fire = soup.find('th', string='How many fireplaces?')
            nb_fire = th_fire.find_next_sibling('td').contents[0]
            open_fire = nb_fire
        except:
            open_fire = None

        # Terrace -> Boolean if True: Area -> int K
        try:
            th_terrace = soup.find('th', string='Terrace surface')
            terrace_surface = th_terrace.find_next_sibling(
                'td').contents[0].strip()
            terrace = int(terrace_surface)
        except:
            terrace = None

        # Garden -> Boolean if True: Area -> int K
        try:
            garden_surface = dataLayer["classified"]["outdoor"]["garden"]["surface"]
            garden = int(garden_surface)
        except:
            garden = None

        # Surface of the land -> int K J
        try:
            surface_land = int(dataLayer["classified"]["land"]["surface"])
        except:
            surface_land = None

        # Number of facades -> int Jess
        try:
            th_facades = soup.find('th', string=re.compile('Number of frontages'))
            number_frontage = th_facades.find_next_sibling('td').contents[0].strip()
        except:
            number_frontage = None

        # Swimming pool -> boolean
        try:
            
            if dataLayer["classified"]["wellnessEquipment"]["hasSwimmingPool"]:
                hasSwimmingPool = True
            else:
                hasSwimmingPool = False
        except:
            hasSwimmingPool = None

        # State of the building (New, to be renovated, ...) -> string (dataLayer)

        # TODO: Cleaning

        # TODO: Finalizing

        # MERGE ALL INFOS in a DICT to return

        d = {
            'id': int(dataLayer["classified"]["id"]) if dataLayer["classified"]["id"] else None,
            'type_of_property': dataLayer["classified"]["type"] if dataLayer["classified"]["type"] else None,
            'subtype_of_property': dataLayer["classified"]["subtype"] if dataLayer["classified"]["subtype"] else None,
            'locality': int(dataLayer["classified"]["zip"]) if dataLayer["classified"]["zip"] else None,
            'price': int(dataLayer["classified"]["price"]) if dataLayer["classified"]["price"] else None,
            'type_of_sale': type_of_sale,
            'rooms': int(rooms),
            'condition': dataLayer["classified"]["building"]["condition"] if dataLayer["classified"]["building"]["condition"] else None,
            'equipped_kitchen': dataLayer["classified"]["kitchen"]["type"] if dataLayer["classified"]["kitchen"]["type"] else None,
            'furnished': furnished,
            'terrace': terrace,
            'garden': garden,
            'open_fire': open_fire,
            'hasSwimmingPool': hasSwimmingPool,
            'living_area_m2': int(area),
            'surface_of_land_m2': int(surface_land),
            'number_frontage': int(number_frontage)
        }
        
        driver.quit()
        return d
    
    except:
        print("not valid")