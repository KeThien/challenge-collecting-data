import csv
import concurrent.futures
from utils.urlparseimmo import urlparseimmo
import pandas as pd

# https://www.youtube.com/watch?v=IEEhzQoKtQU


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
    df = pd.read_csv("./data_set/clean_url_202105051158.csv")
    max_iteration = (len(df)) #55944

    with open("./data_set/clean_url_202105051158.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_list = list(csv_reader)
        liste_dic_infos = []
        
        for i in range(start_index, 100, 10):
            
            url = csv_list[i][0]
            infos_in_url = urlparseimmo(url)
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
                    writer.writerow(data)
        except:
            print("Go to next link")

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