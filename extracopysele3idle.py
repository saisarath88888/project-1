from bs4 import BeautifulSoup 

from selenium import webdriver

from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait

import pandas as pd

import time

from openpyxl.workbook import Workbook

from openpyxl import load_workbook
   
import os


path=r"D:/internshipwork/webscraping/chrome-win64/chrome.exe"
driver=webdriver.Chrome()

#driver.get("https://in.linkedin.com/")
driver.get("https://in.linkedin.com/")
signin=driver.find_element(By.XPATH,"/html/body/nav/div/a[2]")
signin.click()
email=driver.find_element(By.XPATH,'//*[@id="username"]')
email.send_keys("saisarath88888@gmail.com")
password=driver.find_element(By.XPATH,'//*[@id="password"]')
password.send_keys("6281366918")
signin2=driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')
signin2.click()

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3944082025&f_TPR=r604800&keywords=data%20analyst&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=DD")

driver.maximize_window()
      

l=[]


for i in range(4):
        j=i
        #html_content = driver.page_source
        #soup = BeautifulSoup(html_content, 'lxml')
        #target_aria_label = "3"
        
        unordered_list= driver.find_elements(By.CLASS_NAME,"jobs-search__results-list")
        for ul in unordered_list:
        
                list_items = ul.find_elements(By.TAG_NAME, "li")
                
                
                for item in list_items:
                    try:
                        hiring_item= item.find_element(By.CLASS_NAME,"job-posting-benefits__text")
                        
                    except:
                        print("")

        job_title = driver.find_elements(By.CLASS_NAME,"full-width artdeco-entity-lockup__title ember-view")
        company_name = driver.find_elements(By.CLASS_NAME,"artdeco-entity-lockup__subtitle ember-view")
        location = driver.find_elements(By.CLASS_NAME,"job-card-container__metadata-wrapper")
        #hiring_information = driver.find_elements(By.CLASS_NAME,"")    
        #posted_when = driver.find_elements(By.CLASS_NAME,"")

                #a=str(i+2)
        #link=driver.find_element(By.DATA-TEST-PAGINATION-PAGE-BTN_NAME,"a")
        job_title1=[]
        company_name1=[]
        location1=[]
        hiring_information1=[]
        posted_when1=[]

        print(len(job_title))
        print(len(company_name))
        print(len(location))
        a=len(job_title)
        for i in range(a):
            #print(i+1)
            try:
                job_title1.append(job_title[i].text)
            except:
                job_title1.append("---------")
            try:
                company_name1.append(company_name[i].text)
            except:
                company_name1.append("----------")
            try:
                location1.append(location[i].text)
            except:
                location1.append("--------")
        unordered_list= driver.find_elements(By.CLASS_NAME,"jobs-search__results-list")
        for ul in unordered_list:   
            list_items = ul.find_elements(By.TAG_NAME, "li")
        
            for item in list_items:
                try:
                    hiring_item= item.find_element(By.CLASS_NAME,"job-posting-benefits__text")
                    hiring_information1.append(hiring_item.text)
                except:
                    hiring_information1.append("---------")

            list_items = ul.find_elements(By.TAG_NAME, "li")

            for item in list_items:
                try:
                    posted_item= item.find_element(By.CLASS_NAME,"job-search-card__listdate--new")
                    posted_when1.append(posted_item.text)
                except:
                    posted_when1.append("---------")



        mydataset = {
        'job_title':job_title1,'company_name':company_name1,'location':location1}#,'hiring_information':hiring_information1,'posted_when':posted_when1}
        a=str(j+1)
        myvar = pd.DataFrame(mydataset)
        a=myvar
        print(a)
        l.append(a)
        a=(j+1)*25
        b=str(a)
        print(b)
        print(b)
        url="https://www.linkedin.com/jobs/search/?currentJobId=3944082025&f_TPR=r604800&keywords=data%20analyst&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=DD&start="+b
        driver.get(url)
        time.sleep(10)





#link=driver.find_elements_by_css_selector(f'[aria-label="{page3}"]')
#link= soup.find(attrs={aria-label: target_aria_label})
#driver.get(link)
#print(myvar)











with pd.ExcelWriter('linkedin19.xlsx') as writer:#,mode='a',engine='openpyxl',if_sheet_exists='replace') as writer:
    #i=7
    #sheet_name = 'Sheet'+str(i)
    myvar.to_excel(writer, sheet_name='sheet7')



