import requests
from bs4 import BeautifulSoup
import csv

page_to_scrap = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(page_to_scrap.text, "html.parser")
quotes = soup.findAll("span", attrs={"class":"text"})
authors = soup.findAll("small", attrs={"class":"author"})


with open("scrapped_data.csv", 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Quotes", "Author"])

    for quote,author in zip(quotes, authors):
        print(f"{quote.text} - {author.text}")
        writer.writerow([quote.text, author.text])
