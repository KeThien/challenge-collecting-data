from urllib.parse import urlparse


def urlparseimmo(url) -> dict:
    parsed = urlparse(url)
    subtype_apt = [
        'ground-floor', 'triplex', 'duplex', 'studio', 'penthouse', 'loft', 'kot', 'service-flat'
    ]
    segments = parsed.path[1:-1].split("/")
    d = {
        'locality': segments[5],
        'subtype_of_property': segments[2],
        'type_of_property': "apartment" if segments[2] in subtype_apt else "house",
        'id': segments[6]
    }

    return d


# example

url = 'https://www.immoweb.be/en/classified/triplex/for-sale/buizingen/1501/9309298?searchId=608fb627c45c6'

infos_in_url = urlparseimmo(url)

print(infos_in_url)
