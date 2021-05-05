import requests
import csv
import time
from selenium import webdriver
from parsel import Selector
import concurrent.futures

from functions_extract_url import * #personnal function

provinces = [
    "anvers/province",
    "limbourg/province",
    "flandre-orientale/province",
    "flandre-occidentale/province",
    "brabant-flamand/province",
    "brabant-wallon/province",
    "hainaut/province",
    "liege/province",
    "luxembourg/province",
    "bruxelles/province",
    "namur/province"
]

def urls_province(province):
    ######################## WARNING ################################
    PATH = "/opt/chromedriver"  #TO CHANGE SET THE PATH FOR YOUR DRIVER
    #################################################################
    
    #List in which we will append the results
    links = []
    url =f"https://www.immoweb.be/en/search/house-and-apartment/for-sale/{province}?countries=BE&page=1&orderBy=newest"
    max_page = get_last_page(url, PATH)
    print(max_page)

    driver = webdriver.Chrome(PATH)
    for page in range(1, max_page + 1):

        url =f"https://www.immoweb.be/en/search/house-and-apartment/for-sale/{province}?countries=BE&page={page}&orderBy=newest"

        #An implicit wait tells WebDriver to poll the DOM for a certain amount of time when trying to find any element (or elements) not immediately available. 
        # For the documentation: https://selenium-python.readthedocs.io/waits.html
        driver.implicitly_wait(10)
            
        driver.get(url)

        #For the documentation: https://parsel.readthedocs.io/en/latest/usage.html
        sel = Selector(text=driver.page_source) #Initialize the Selector

        xpath_houses = '//*[@id="main-content"]/li//h2//a/@href' #for a sheet cheat: https://devhints.io/xpath

        page_url = sel.xpath(xpath_houses).getall() #returns a list with all results

        links.append(page_url)

    ######### REMOVE SERACH ID #######
    rm_search_id(page_url)

    ######### PERSISTING DATA IN THE CSV ########
    with open(f"list_links_{province[:4]}.csv", "a") as csv_file:
        csv_writer = csv.writer(csv_file)
        for page in links:
            for url in page:
                csv_writer.writerow([url])

t1 = time.perf_counter()
#### MULTI THREADIND ####
# Source: https://www.youtube.com/watch?v=IEEhzQoKtQU
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(urls_province,provinces)

t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds')