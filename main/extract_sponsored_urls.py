import requests
import csv
import time
from selenium import webdriver
from parsel import Selector
import concurrent.futures

from functions_extract_url import * #personnal function


with open("sponsored_url_202105051158.csv", "r") as file:
    csv_file = csv.reader(file)
    PATH = "/opt/chromedriver" 
    driver = webdriver.Chrome(PATH)

    for line in csv_file:
        liste_url = []
        
        url = line[0]
        #An implicit wait tells WebDriver to poll the DOM for a certain amount of time when trying to find any element (or elements) not immediately available. 
        # For the documentation: https://selenium-python.readthedocs.io/waits.html
        driver.implicitly_wait(10)
            
        driver.get(url)

        #For the documentation: https://parsel.readthedocs.io/en/latest/usage.html
        sel = Selector(text=driver.page_source) #Initialize the Selector

        xpath = "/html/body/div[1]/div[2]/div/div/main/div[3]/section[2]/div/div/div/div/div/div[3]/ul//li/a/@href"

        page_url = sel.xpath(xpath).getall() #returns a list with all results

        liste_url.append(page_url)

    driver.close()
    
    print(liste_url)