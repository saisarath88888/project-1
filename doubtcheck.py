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
print(1)
job_title = driver.find_element(By.CLASS_NAME,"full-width artdeco-entity-lockup__title ember-view")
print(job_title.text)
print(1)
#print(len(job_title))






