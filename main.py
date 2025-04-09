import requests
from bs4 import BeautifulSoup
import csv

def scrape_quotes():
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to retrieve the page")
        return

    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='quote')

    with open('quotes.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Quote', 'Author'])

        for quote in quotes:
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            writer.writerow([text, author])
            print(f"{text} — {author}")

if __name__ == "__main__":
    scrape_quotes()
