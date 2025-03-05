from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pandas as pd
import re
import time
import undetected_chromedriver.v2 as uc

path=r"D:/internshipwork/webscraping/chrome-win64/chrome.exe"
driver=webdriver.Chrome()


def parse_posted_date(posted_date_str, reference_date):
    try:
        if 'day' in posted_date_str:
            days_ago = int(posted_date_str.split()[0])
            return reference_date - timedelta(days=days_ago)
        elif 'hour' in posted_date_str:
            hours_ago = int(posted_date_str.split()[0])
            return reference_date - timedelta(hours=hours_ago)
        elif 'minute' in posted_date_str:
            minutes_ago = int(posted_date_str.split()[0])
            return reference_date - timedelta(minutes=minutes_ago)
        elif 'second' in posted_date_str:
            seconds_ago = int(posted_date_str.split()[0])
            return reference_date - timedelta(seconds=seconds_ago)
        else:
            if 'Just' in posted_date_str or 'Today' in posted_date_str:
                return reference_date
            return reference_date  # Default fallback
    except Exception as e:
        print(f"Error parsing date: {e}, original date string: {posted_date_str}")
        return None

def extract_skills(description):
    match = re.search(r'Skills:\s*(.*)', description)
    if match:
        return match.group(1).strip()
    return "None"

def scrape_glassdoor_jobs():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    titles = []
    skills_list = []

    now = datetime.now()
    last_24_hours = now - timedelta(hours=24)

    page = 1
    while True:
        url = f"https://www.glassdoor.co.in/Job/india-python-developer-jobs-SRCH_IL.0,5_IN115_KO6,22.htm?fromAge=1&pg={page}"
        driver.get(url)
        time.sleep(2)  

        body = driver.find_element(By.CSS_SELECTOR, 'body')
        for _ in range(10):
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.5)  

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        job_elements = soup.find_all('div', class_='Page_fullHeight__QlatA')

        if not job_elements:
            print("No job elements found, ending scrape.")
            break

        for job_elem in job_elements:
            try:
                title_elem = job_elem.find('a', class_='JobCardFooter_created__7U1Ns')
                date_elem = job_elem.find('div', class_='css-qvloho eu4oa1w0')
                description_elem = job_elem.find('div', class_='JobCard_jobDescriptionSnippet__yWW8q')

                if not all([title_elem, date_elem, description_elem]):
                    print("Missing one or more elements, skipping job.")
                    continue 

                title = title_elem.text.strip()
                description = description_elem.text.strip()
                posted_date = date_elem.text.strip()

                skills = extract_skills(description)
                posted_datetime = parse_posted_date(posted_date, now)

                if posted_datetime and posted_datetime >= last_24_hours:
                    titles.append(title)
                    skills_list.append(skills)

                    print(f"Job Title: {title}")
                    print(f"Skills: {skills}")
                    print()

                    if len(titles) >= 60:
                        break
            except Exception as e:
                print(f"Error processing job element: {e}")

        if len(titles) >= 60:
            break

        page += 1

    driver.quit()

    df = pd.DataFrame({
        'Job Title': titles,
        'Skills': skills_list
    })

    # Save the DataFrame to an Excel file
    df.to_excel('scraped_glassdoor_jobs.xlsx', index=False)

    return df

# Example usage:
if _name_ == "_main_":
    try:
        job_df = scrape_glassdoor_jobs()
        print("\nDataFrame Output:")
        print(job_df)
    except Exception as e:
        print(f"An error occurred: {e}")
