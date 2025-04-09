import schedule
import time
import subprocess

def run_scraper():
    print("Running scraper now...")
    subprocess.run(["python", "selenium_login.py"])

# For quick testing (runs every 1 minute)
schedule.every(1).minutes.do(run_scraper)

while True:
    schedule.run_pending()
    time.sleep(1)
