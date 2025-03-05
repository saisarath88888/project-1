
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
print(0)
#driver.get("https://www.linkedin.com/jobs/")
driver.get("https://in.indeed.com/jobs?q=data+analyst&fromage=3&pp=gQAAAAABkC7dtIAAAAACLGcYGgADAAABAAA")

#driver.maximize_window()
        
#j=driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/section/button')
#j.click()
#time.sleep(2)
#b=driver.find_element(By.XPATH,'//*[@id="job-search-bar-keywords"]')#//*[@id="job-search-bar-keywords"]
#for i in range(1):
 #       b.send_keys(Keys.BACKSPACE)
#b.send_keys('is')
#k=driver.find_element(By.XPATH,'//*[@id="job-search-bar-location"]')#//*[@id="job-search-bar-location"]
#for i in range(13):
#        k.send_keys(Keys.BACKSPACE)
#k.send_keys('India')
#k.send_keys(Keys.ENTER)
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")



#actions = ActionChains(driver)



#s=driver.find_element(By.XPATH,'//*[@id="main-content"]/section[2]/ul/li[6]/div/a')

#time.sleep(3)

#actions.double_click(s).perform()
#time.sleep(2)

#l=driver.find_element(By.XPATH,'//*[@id="main-content"]/section[2]/ul/li[1]/div/a')
#link=l.get_attribute("href")
#print(link)




#time.sleep(60)


#driver.find_element(By.TAG_NAME,'body').send_keys(Keys.CONTROL + 'r')
#for i in range(5):
        #driver.refresh()
        #driver.get(driver.current_url)
#        time.sleep(2)
#        current_height = driver.execute_script("return document.body.scrollHeight;")
 #       
  #      driver.execute_script("window.scrollTo(current_height,document.body.scrollHeight);")
   #     time.sleep(2)
        
#j=driver.find_element(By.CLASS_NAME,"infinite-scroller__show-more-button infinite-scroller__show-more-button--visible")
#j.click()

#description__job-criteria-listl==[]

        #html_content = driver.page_source
        #soup = BeautifulSoup(html_content, 'lxml')
        #target_aria_label = "3"
        
print(1)

unordered_list= driver.find_elements(By.CLASS_NAME,"css-zu9cdh eu4oa1w0")
for ul in unordered_list:
    list_items = ul.find_elements(By.TAG_NAME, "li")
                
'''       
        for item in list_items:
                try:
                        hiring_item= item.find_element(By.CLASS_NAME,"css-5lfssm eu4oa1w0")
                        copy_items = hiring_item.find_element(By.TAG_NAME, "li")
                        print(hiring_item.text)
                except:
                        print("")
'''
         

job_title = driver.find_elements(By.CLASS_NAME,"jcs-JobTitle css-jspxzf eu4oa1w0")
print(job_title)
company_name = driver.find_elements(By.CLASS_NAME,"base-search-card__subtitle")
location = driver.find_elements(By.CLASS_NAME,"job-search-card__location")
hiring_information = driver.find_elements(By.CLASS_NAME,"job-posting-benefits__text")    
posted_when = driver.find_elements(By.CLASS_NAME,"job-search-card__listdate--new")

                #a=str(i+2)
        #link=driver.find_element(By.DATA-TEST-PAGINATION-PAGE-BTN_NAME,"a")
job_title1=[]
company_name1=[]
location1=[]
hiring_information1=[]
posted_when1=[]
Seniority_level1=[]
Employment_type1=[]
Job_function1=[]
Industries1=[]

print(len(job_title))
a=len(job_title)
'''for i in range(a):
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
'''
#list_items = driver.find_elements(By.TAG_NAME, "li")
unordered_list= driver.find_element(By.CLASS_NAME,"css-zu9cdh eu4oa1w0")
ula=unorderde_list
#for ul in unordered_list:
list_items = ula.find_elements(By.CLASS_NAME,"css-5lfssm eu4oa1w0")

for item in list_items:
        print(item.text )
        print(5)
        try:
                job_title= item.find_element(By.CLASS_NAME,"jcs-JobTitle css-jspxzf eu4oa1w0")
                job_title1.append(job_title.text)
                print(job_title.text)
                print(11)
        except:
                job_title1.append("---------")
        try:
               
                company_name= item.find_element(By.CLASS_NAME,"base-search-card__subtitle")
                company_name1.append(company_name.text)
        except:
                company_name1.append("---------")
        try:
                
                location= item.find_element(By.CLASS_NAME,"job-search-card__location")
                location1.append(location.text)
        except:
                location1.append("---------")
        try:
                
                hiring_item= item.find_element(By.CLASS_NAME,"job-posting-benefits__text")
                hiring_information1.append(hiring_item.text)
        except:
                hiring_information1.append("---------")
        try:
                
                posted_item= item.find_element(By.CLASS_NAME,"job-search-card__listdate--new")
                posted_when1.append(posted_item.text)
        except:
                posted_when1.append("---------")


#l=driver.find_elements(By.CLASS_NAME,'base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]')
print(16)
print(len(job_title1))
print(len(company_name1))
print(len(location1))
print(len(hiring_information1))
print(len(posted_when1))
print(len(Seniority_level1))
print(len(Employment_type1))
print(len(Job_function1))
print(len(Industries1))


mydataset = {
'job_title':job_title1,'company_name':company_name1,'location':location1,'hiring_information':hiring_information1,'posted_when':posted_when1,'Employment_type':Employment_type1,'Job_function':Job_function1,
        'Seniority_level':Seniority_level1,'Industries':Industries1}
#a=str(j+1)
myvar = pd.DataFrame(mydataset)
print(21)
a=myvar
print(a)
#l.append(a)
#a=(j+1)*25
#b=str(a)
#print(b)
#print(b)
#url="https://www.linkedin.com/jobs/search/?currentJobId=3939432016&f_TPR=r604800&keywords=data%20analyst&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R&spellCorrectionEnabled=true&start=50"
#print(url)
#driver.get(url)
#time.sleep(1)





#link=driver.find_elements_by_css_selector(f'[aria-label="{page3}"]')
#link= soup.find(attrs={aria-label: target_aria_label})
#driver.get(link)
#print(myvar)











with pd.ExcelWriter('linkedin19.xlsx') as writer:#,mode='a',engine='openpyxl',if_sheet_exists='replace'
    #i=7
    #sheet_name = 'Sheet'+str(i)
    myvar.to_excel(writer, sheet_name='sheet1')



