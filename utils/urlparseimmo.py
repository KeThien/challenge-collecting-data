from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests


def urlparseimmo(url) -> dict:
    '''
    Function to parse all info into a dict
    '''
    # Parse element in the URL
    parsed = urlparse(url)
    # Subtypes to know if apartment else house
    subtype_apt = [
        'ground-floor', 'triplex', 'duplex', 'studio', 'penthouse', 'loft', 'kot', 'service-flat'
    ]
    # parsing split segment from the URL
    segments = parsed.path[1:-1].split("/")

    # Beautifulsoup to get the rest of the info
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')

    # PRICE:
    price = int(soup.select('p.classified__price .sr-only')[0].text[:-1])

    # TODO: Type of SALE -> string

    # TODO: Number of rooms -> int

    # TODO: Area -> int

    # TODO: Fully equipped kitchen -> boolean

    # TODO: Furnished -> boolean

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
        'id': int(segments[6]),
        'locality': int(segments[5]),
        'subtype_of_property': segments[2],
        'type_of_property': "apartment" if segments[2] in subtype_apt else "house",
        'price': price
    }

    return d


# example

url = 'https://www.immoweb.be/en/classified/house/for-sale/sint-pieters-leeuw/1600/9310259?searchId=609000ddc3e3d'

infos_in_url = urlparseimmo(url)

print(infos_in_url)
