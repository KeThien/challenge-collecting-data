from bs4 import BeautifulSoup
import requests
import csv
from selenium import webdriver
import pandas as pd
import time

from parsel import Selector

# To retrieve all results via postal codes
# path_csv = "./data_set/full_cp.csv"
# l = pd.read_csv(path_csv, header= None)
# liste_cp = l[0].tolist()

#To retrieve all results via provinces
province = ["anvers/province","limbourg/province","flandre-orientale/province","flandre-occidentale/province","brabant-flamand/province","brabant-wallon/province","hainaut/province","liege/province","luxembourg/province","namur/province"]

#Set up of the driver
PATH = "/opt/chromedriver"
driver = webdriver.Chrome(PATH)

#List in which we will append the results
links = []

for i in province:
# Iterate through all result pages (i) and get the url of each of them
    
    try:
        for j in range(1, 334):
            if len(links) <3 :
                sorting = "&orderBy=newest" #[cheapest, relevance, most_expensive, postal_code, newest]
                region = i #loop over the list of all provinces codes in Belgium
                pagination = j #temporarily hard codes but then with a loop and a range with max pagination for the specific postal code
                url =f"https://www.immoweb.be/en/search/house-and-apartment/for-sale/{region}?countries=BE&page={pagination}{sorting}"

                #An implicit wait tells WebDriver to poll the DOM for a certain amount of time when trying to find any element (or elements) not immediately available. 
                # For the documentation: https://selenium-python.readthedocs.io/waits.html
                driver.implicitly_wait(10)
                    
                driver.get(url)

                #For the documentation: https://parsel.readthedocs.io/en/latest/usage.html
                sel = Selector(text=driver.page_source) #Initialize the Selector

                xpath_houses = '//*[@id="main-content"]/li//h2//a/@href' #for a sheet cheat: https://devhints.io/xpath

                page_url = sel.xpath(xpath_houses).getall() #returns a list with all results
                
                # There are approximately 30 houses in each page.
                # Add each page url list to houses_url, like in a matrix.
                links.append(page_url)
    except:
            continue

######### PERSISTING DATA IN THE CSV ########

#Setting up the writer for the final file
csv_file = open("list_links.csv", "a")
csv_writer = csv.writer(csv_file)

#Append the results to the final CSV
for page in links:
    for url in page:
        csv_writer.writerow([url])

csv_file.close()
driver.close()
print("ok")