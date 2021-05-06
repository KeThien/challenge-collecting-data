import requests
import csv
import time
from selenium import webdriver
from parsel import Selector
import concurrent.futures
import pandas as pd

from utils.urlparseimmo import urlparseimmo


# https://www.youtube.com/watch?v=IEEhzQoKtQU

PATH = '/opt/chromedriver'

liste_threading=[0,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9
]

def fulldata_extraction(start_index):

    try:
        df = pd.read_csv("./data_set/clean_url_202105051158.csv")
        max_iteration = (len(df)) #55944
        print(max_iteration)

        driver = webdriver.Chrome(PATH)

        with open("./data_set/clean_url_202105051158.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_list = list(csv_reader)
            liste_dic_infos = []
            
            for i in range(start_index, max_iteration, 10):
                
                url = csv_list[i][0]
                driver.implicitly_wait(10)
                driver.get(url)

                html = driver.page_source
                infos_in_url = urlparseimmo(html)

                print(url)
                liste_dic_infos.append(infos_in_url)
            

            try:
                keys = liste_dic_infos[0].keys()

                with open(f"temp{start_index}.csv", "w") as init_file:
                    writer = csv.DictWriter(init_file, keys)
                    writer.writeheader()
                
                with open(f"temp{start_index}.csv", "a") as temp_file:
                    writer = csv.DictWriter(temp_file, keys)

                    for data in liste_dic_infos:
                        try: 
                            writer.writerow(data)
                        except:
                            continue
            except:
                print("Go to next link")

        driver.close()
    
    except:
        raise Exception
# https://www.tutorialspoint.com/How-to-save-a-Python-Dictionary-to-CSV-file

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(fulldata_extraction, liste_threading)


# fulldata_extraction(0)



    # csv_header = [
    #     'id',
    #     'type_of_property', 
    #     'subtype_of_property',
    #     'locality',
    #     'price',
    #     'type_of_sale',
    #     'rooms',
    #     'condition',
    #     'equipped_kitchen',
    #     'furnished',
    #     'terrace',
    #     'garden',
    #     'open_fire',
    #     'hasSwimmingPool',
    #     'living_area_m2',
    #     'surface_of_land_m2',
    #     'number_frontage'
    #     ]