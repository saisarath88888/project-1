from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import mysql.connector
import time


path=r"D:/internshipwork/webscraping/chrome-win64/chrome.exe"
driver=webdriver.Chrome()



driver.get("https://www.glassdoor.co.in/Job/data-engineer-jobs-SRCH_KO0,13.htm?fromAge=1")
url="https://www.glassdoor.co.in/Job/data-engineer-jobs-SRCH_KO0,13.htm?fromAge=1"

driver.implicitly_wait(4)


connection = mysql.connector.connect(host='localhost',user='root',password='Sarath@1',database='etl')

if connection.is_connected:
    print("success")
else:
    print("failure")
cursor = connection.cursor()

query = "show databases;"
cursor.execute(query) 
database = cursor.fetchall() 
      
for db in database: 
    print(db)
query = "use etl;"
cursor.execute(query)

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS job_listings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    jobTitle VARCHAR(255),
    jobLocation VARCHAR(255),
    jobSkills TEXT
)
""")

query = "show tables;"
cursor.execute(query) 
table = cursor.fetchall() 
      
for tab in table: 
    print(tab)
    
title1=[]
location1=[]
skills1=[]


# Iterate through a predefined number of pages and extract job listings
page_limit = 10  # Define how many pages you want to scrape
for start in range(1, page_limit + 1):
    driver.get(url + "&pg=" + str(start))
    
    # Wait a bit for the page to load completely

    # Find all job cards
    #all_jobs = driver.find_elements(By.CLASS_NAME, "react-job-listing")
    unordered_list= driver.find_elements(By.CLASS_NAME,"JobsList_jobsList__lqjTr")
    for ul in unordered_list:
        
        list_items = ul.find_elements(By.TAG_NAME, "li")

      
    all_jobs = ul.find_elements(By.TAG_NAME, "li")
    for item in all_jobs:
        
        #result_html = job.get_attribute('innerHTML')
        #soup = BeautifulSoup(result_html, 'html.parser')
        # Extract job title
        try:
            title = item.find_element(By.CLASS_NAME,"JobCard_jobTitle___7I6y").text
            title1.append(title)
            print(title)
            
        except AttributeError:
            title = 'None'
            title1.append(title)

        # Extract job location
        try:
            location = item.find_element(By.CLASS_NAME,"JobCard_location__rCz3x").text
            print(location)
            location1.append(location)
        except AttributeError:
            location = 'None'
            location1.append(location)
            
        # Extract job skils
        try:
            skills= item.find_element(By.CLASS_NAME,"JobCard_jobDescriptionSnippet__yWW8q").text
            print(skills)
            skills1.append(skills)
        except AttributeError:
            skills = 'None'
            skills1.append(skills)
        row=(title,location,skills)
mydataset = {'title':title1,'location':location1,'skills':skills1}
myvar = pd.DataFrame(mydataset)
        
try:
    # Iterate over DataFrame rows
    for index, row in df.iterrows():
        # SQL query to insert row into 'company_data' table
        sql = "INSERT INTO job_listings(title,location,skills ) VALUES (%s, %s , %s)"
        # Execute the SQL query
        cursor.execute(sql, tuple(row))
        # Commit changes to the database
        connection.commit()
    print("Data inserted successfully!")
    
except Exception as e:
    print(f"Error inserting data: {str(e)}")
    # Rollback changes if an error occurs
    connection.rollback()

finally:
    # Close cursor and connection
    cursor.close()
    connection.close()

