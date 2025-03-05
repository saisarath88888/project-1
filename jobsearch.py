import numpy as np
import pandas as pd
import lxml
from bs4 import BeautifulSoup
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Specify the URL of the website you want to scrape
url = 'https://www.glassdoor.co.in/Job/data-analyst-jobs-SRCH_KO0,12.htm'

# Initialize the Chrome web driver
driver = webdriver.Chrome()

# Open the URL in a headless browser
driver.get(url)

# Allow the page to load
time.sleep(2)

# Find an element on the page
element = driver.find_element_by_id('job-location-1009304920577')

# Get the text of the element
text = element.text
print(text)

# You can also interact with the page by clicking a button, filling a form, etc.
# For example, let's fill a form and submit it
search_box = driver.find_element_by_name('q')
search_box.send_keys('Selenium')
search_box.send_keys(Keys.RETURN)

# Close the browser
driver.close()

#html_text=requests.get("https://www.glassdoor.co.in/Job/data-analyst-jobs-SRCH_KO0,12.htm")
#print(html_text)
#soup=BeautifulSoup(html_text.content,'lxml')
#job=soup.find("li", class_ ="css-5lfssm eu4oa1w0")
#print(job)
#print(soup.text.strip())


