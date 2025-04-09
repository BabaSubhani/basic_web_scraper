from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

# Set path to ChromeDriver (it should be in the same folder)
driver_path = os.path.join(os.getcwd(), 'chromedriver.exe')

# Set up Chrome with Service
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Open the quotes website
#driver.get("https://www.amazon.in/")
driver.get("https://quotes.toscrape.com/")

# Wait for 2 seconds to let page load
time.sleep(2)

# Print the page title
print("Page title is:", driver.title)

# Close the browser
driver.quit()
