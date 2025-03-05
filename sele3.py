from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

website="https://www.webscraper.io/test-sites"
#path=r"D:/internshipwork/webscraping/chrome-win64/chrome.exe"
driver=webdriver.Chrome()

website="https://www.webscraper.io/test-sites"
driver.get("https://www.linkedin.com/jobs/")
driver.maximize_window()

driver.find_element_by_xpath('//*[@id="session_key"]').send_keys("saisarath88888@gmail.com")
time.sleep(200)
#driver.get_element_by_xpath("")
#driver=webdriver.Chrome()
#driver.get("https://youtube.com")
#time.sleep(115)
# soup=BeautifulSoup()
