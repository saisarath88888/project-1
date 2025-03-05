from selenium import webdriver


path="D:/chrome-win64"
# Create an instance of the web browser
driver = webdriver.Chrome(path)

# Navigate to a website
driver.get("https://www.example.com")

# Verify the title of the page
expected_title = "Example Domain"
actual_title = driver.title
if expected_title in actual_title:
    print("Title verification passed")
else:
    print(f"Title verification failed. Expected: {expected_title}, Actual: {actual_title}")

# Close the web browser
