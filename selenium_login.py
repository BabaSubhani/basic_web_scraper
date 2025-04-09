from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import csv

# Path to your chromedriver.exe
CHROMEDRIVER_PATH = "D:/Python Projects/basic_web_scraper/chromedriver.exe"

# Set up Chrome options
options = webdriver.ChromeOptions()
service = Service(executable_path=CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

# Go to the login page
driver.get("http://quotes.toscrape.com/login")
print("DevTools listening...")

# Wait a bit for the page to load
time.sleep(2)

# Fill out the login form
username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")

username_input.send_keys("admin")
password_input.send_keys("admin")
password_input.send_keys(Keys.RETURN)

# Wait for the page to log in and load
time.sleep(2)

# Scrape quotes
quotes_elements = driver.find_elements(By.CLASS_NAME, "text")

# Save to CSV
with open("selenium_quotes.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote"])  # header

    for quote in quotes_elements[:5]:  # Scraping first 5 quotes
        quote_text = quote.text
        print(quote_text)
        writer.writerow([quote_text])

# Close the browser
driver.quit()
