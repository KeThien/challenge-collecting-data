import requests
import csv
from selenium import webdriver
import pandas as pd
import time
import re
from parsel import Selector
import os
import glob


def rm_search_id(page_url):
    '''
    Remove the end of the url; that is, the searchId
    Takes a list as argument
    Returns a list
    '''
    try:
        liste=[]
        for url in page_url:
            pattern = "(searchId\=[0-9a-zA-Z]+)"
            x = re.sub(pattern,"", url)
            liste.append(x)
        return liste
    except:
        raise Exception("Make sure you entered a valide url (string)")


def get_last_page(url, PATH):
    '''
    Return the last page available
    Example: page: 1,2,3...120 -> return 120
    Takes an url (string) and the PATH for the driver (Chrome)
    Returns an Int
    '''
    try:
        driver = webdriver.Chrome(PATH)
        driver.implicitly_wait(10)
        driver.get(url)
        sel = Selector(text=driver.page_source) #Initialize the Selector
        xpath_last_page='/html/body/div[1]/div[2]/div/main/div/div[2]/div/div[3]/div/div/div[1]/div/div/div[1]/div/nav/ul/li[4]/a/span[2]/text()' #Path to the number of the last page
        last_page = sel.xpath(xpath_last_page).get() #to get the value
        driver.close()
        return int(last_page)
    except:
        raise Exception("Please make sure you initialised the driver and sent a correct url (string)")

def check_in_csv(page_url, csv):
    '''
    Check if url already in the list; if not append it to it
    page_url should be a list
    csv should be the csv file as string
    '''
    try:
        with open(csv, 'r') as fp:
            s = fp.read()
    except:
        raise ValueError("Arguments not valid; Make sure to send a list and csv file (as a string) as arguments.")
    
    missing = []
    for url in page_url:
        if url not in s:
            missing.append(url + '\n')
            print("not in it")
        else:
            print("in it")

    if missing:
        with open(csv, 'a+') as fp:
            fp.writelines(missing)


def sort_merge_urls(folder):
    '''
    Takes the path of the folder (string) as argument
    
    Sort all the links into two categorie:
        - clean_url: ready to be extracted
        - sponsored_url : url needing some more url extraction work
    The Path File must be changed to your directory specification
    '''
    try:
        all_files = glob.glob(os.path.join(folder, "*.csv"))
        date = time.strftime("%Y%m%d%H%M")

        for file in all_files:
            with open(file, "r") as csv_file:
                csv_reader = csv.reader(csv_file)

                with open(f"clean_url_{date}.csv", "a") as clean_file:
                    clean_csv_writer = csv.writer(clean_file)
                    
                    with open(f"sponsored_url_{date}.csv", "a") as sponsored_file:
                        sponsored_csv_writer = csv.writer(sponsored_file)

                        for line in csv_reader:              
                            if "new-real-estate-project" in line[0]:
                                sponsored_csv_writer.writerow(line)
                            else:
                                clean_csv_writer.writerow(line)
    except :
        raise Exception

