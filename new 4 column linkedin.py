from bs4 import BeautifulSoup 

from selenium import webdriver

from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

import time

from openpyxl.workbook import Workbook

from openpyxl import load_workbook
   
import os


path=r"D:/internshipwork/webscraping/chrome-win64/chrome.exe"
driver=webdriver.Chrome()

driver.get("https://www.glassdoor.co.in/Job/data-engineer-jobs-SRCH_KO0,13.htm?fromAge=1")
url="https://www.glassdoor.co.in/Job/data-engineer-jobs-SRCH_KO0,13.htm?fromAge=1"

title1=[]
location1=[]
skills1=[]
page_limit = 10
for start in range(1, page_limit + 1):
    driver.get(url + "&pg=" + str(start))
    unordered_list= driver.find_elements(By.CLASS_NAME,"JobsList_jobsList__lqjTr")
    for ul in unordered_list:
        list_items = ul.find_elements(By.TAG_NAME, "li")                        

    list_items = ul.find_elements(By.TAG_NAME, "li")


    for item in list_items:

        try:
            title= item.find_element(By.CLASS_NAME,"JobCard_jobTitle___7I6y").text
            print(title)
            title1.append(title)
        except:
            title1.append("None")

        try:
            location= item.find_element(By.CLASS_NAME,"JobCard_location__rCz3x").text
            print(location)
            location1.append(location)
        except:
            location1.append("None")

        try:
            skills= item.find_element(By.CLASS_NAME,"JobCard_jobDescriptionSnippet__yWW8q").text
            print(skills)
            skills1.append(skills)
        except:
            skills1.append("None")
        

mydataset = {'title':title1,'location':location1,'skills':skills1}
myvar = pd.DataFrame(mydataset)
        
a=myvar
print(a)





with pd.ExcelWriter('linkedin37.xlsx') as writer:#,mode='a',engine='openpyxl',if_sheet_exists='replace'
    #i=7
    #sheet_name = 'Sheet'+str(i)
    myvar.to_excel(writer, sheet_name='sheet1')



