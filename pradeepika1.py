import time
import traceback
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
#import pandas as pd

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
#from nselib import capital_market
#import matplotlib.pyplot as plt
#import openpyxl

chrome_driver_path = r"D:/internshipwork/webscraping/chrome-win64/chrome.exe"

stockcode = "WIPRO"
print(stockcode)
stock_url = "https://www.nseindia.com/get-quotes/equity?symbol=" + str(stockcode)

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
response = requests.get(stock_url, headers=headers)
print(response)


driver = webdriver.Chrome()

driver.get("https://www.nseindia.com/get-quotes/equity?symbol=ADANIENT")
time.sleep(3)

action_chains = ActionChains(driver)


element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="historic_data"]')))
action_chains.click(element).perform()
time.sleep(2)


element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="threeM"]')))
action_chains.click(element).perform()
time.sleep(2)


# Wait for the body to be present
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# Click on the dropdown element to open the options
dropdown_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.multiselect.dropdown-toggle')))
dropdown_button.click()
time.sleep(1)  # Wait for the dropdown to open

eq_checkbox = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="checkbox" and @value="EQ"]')))
eq_checkbox.click()

# Add a longer sleep period to ensure the checkbox stays checked
time.sleep(5)  # Adjust the duration as needed

# Click on the download CSV button
download = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dwldcsv"]')))
action_chains.click(download).perform()
time.sleep(3)
