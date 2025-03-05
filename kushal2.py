from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import re

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# URL to scrape
#url = "https://www.glassdoor.co.in/Job/data-engineer-jobs-SRCH_KO0,13.htm?fromAge=1"
#url="https://www.glassdoor.co.in/Job/india-python-developer-jobs-SRCH_IL.0,5_IN115_KO6,22.htm?fromAge=1"
url="https://www.glassdoor.co.in/Job/india-python-developer-jobs-SRCH_IL.0,5_IN115_KO6,22.htm?fromAge=1&sortBy=date_desc"



title1 = []
location1 = []
skills1 = []
page_limit = 1


def extract_skills(description):
    # Use regex to find text after "Skills:"
    match = re.search(r'Skills:\s*(.*)', description)
    if match:
        return match.group(1).strip()
    return "None"


for start in range(1, page_limit + 1):
    driver.get(url + "&pg=" + str(start))
    time.sleep(60)  # Wait for the page to load
    unordered_list = driver.find_elements(By.CLASS_NAME, "JobsList_jobsList__lqjTr")
    
    for ul in unordered_list:
        list_items = ul.find_elements(By.TAG_NAME, "li")
        
        for item in list_items:
            try:
                title = item.find_element(By.CLASS_NAME, "JobCard_jobTitle___7I6y").text.strip()
            except:
                title = "None"

            try:
                location = item.find_element(By.CLASS_NAME, "JobCard_location__rCz3x").text.strip()
            except:
                location = "None"

            try:
                description = item.find_element(By.CLASS_NAME, "JobCard_jobDescriptionSnippet__yWW8q").text.strip()
                skills_text = extract_skills(description)
            except:
                skills_text = "None"

            # Append data only if all fields are successfully retrieved and skills are found
            if title != "None" and location != "None" and skills_text != "None":
                title1.append(title)
                location1.append(location)
                skills1.append(skills_text)

# Create DataFrame
mydataset = {'skills': skills1}
myvar = pd.DataFrame(mydataset)

# Print and save to Excel
print(myvar)

with pd.ExcelWriter('linkedin36.xlsx') as writer:
    myvar.to_excel(writer, sheet_name='sheet1', index=False)

# Quit the WebDriver
driver.quit()
