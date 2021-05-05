import requests
import csv
import time
from selenium import webdriver
from parsel import Selector
import concurrent.futures

from functions_extract_url import * #personnal function


##### Lists used for the MultiThreading ######
provinces_house = [
    ["house","anvers/province"],
    ["house","limbourg/province"],
    ["house","flandre-orientale/province"],
    ["house","flandre-occidentale/province"],
    ["house","brabant-flamand/province"],
    ["house","brabant-wallon/province"],
    ["house","hainaut/province"],
    ["house","liege/province"],
    ["house","luxembourg/province"],
    ["house","bruxelles/province"],
    ["house","namur/province"]
]

province_apptmnt = [
    ["house","namur/province"],
    ["apartment","anvers/province"],
    ["apartment","limbourg/province"],
    ["apartment","flandre-orientale/province"],
    ["apartment","flandre-occidentale/province"],
    ["apartment","brabant-flamand/province"],
    ["apartment","brabant-wallon/province"],
    ["apartment","hainaut/province"],
    ["apartment","liege/province"],
    ["apartment","luxembourg/province"],
    ["apartment","bruxelles/province"],
    ["apartment","namur/province"]
]


def urls_province(province):
    try:
        ######################## WARNING ################################
        PATH = "/opt/chromedriver"  #TO CHANGE SET THE PATH FOR YOUR DRIVER
        #################################################################
        regio = province[1]
        house_aptmnt = province[0]
        #### SCRAPPING ALL THE URLs #######
        links = []
        url =f"https://www.immoweb.be/en/search/{house_aptmnt}/for-sale/{regio}?countries=BE&page=1&orderBy=newest"
        max_page = get_last_page(url, PATH)

        driver = webdriver.Chrome(PATH)
        for page in range(1, max_page + 1):

            url =f"https://www.immoweb.be/en/search/{house_aptmnt}/for-sale/{regio}?countries=BE&page={page}&orderBy=newest"

            #An implicit wait tells WebDriver to poll the DOM for a certain amount of time when trying to find any element (or elements) not immediately available. 
            # For the documentation: https://selenium-python.readthedocs.io/waits.html
            driver.implicitly_wait(10)
                
            driver.get(url)

            #For the documentation: https://parsel.readthedocs.io/en/latest/usage.html
            sel = Selector(text=driver.page_source) #Initialize the Selector

            xpath_houses = '//*[@id="main-content"]/li//h2//a/@href' #for a sheet cheat: https://devhints.io/xpath

            page_url = sel.xpath(xpath_houses).getall() #returns a list with all results

            clean_page_urls = rm_search_id(page_url) # Remove Search ID

            links.append(clean_page_urls)


        ######### PERSISTING URLs IN THE CSV ########

        with open(f"list_links_{house_aptmnt}_{regio[:5]}.csv", "a") as csv_file:
            csv_writer = csv.writer(csv_file)
            for page in links:
                for url in page:
                    csv_writer.writerow([url])

        driver.close()
    
    except:
        raise Exception

t1 = time.perf_counter()
#### MULTI THREADIND ####
# Source: https://www.youtube.com/watch?v=IEEhzQoKtQU
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(urls_province,provinces_house)

t2 = time.perf_counter()
print(f'Houses finished in {t2-t1} seconds')

t1 = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(urls_province,province_apptmnt)

t2 = time.perf_counter()
print(f'Appartments finished in {t2-t1} seconds')


### SORTING AND MERGING OF THE FILES #####
Makes sure we keep only the valid urls
Why? The sponsored links contain sub urls.
To check: are those sublinks present in the original database

folder = ""
sort_merge_urls(folder)