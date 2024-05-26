import requests
from bs4 import BeautifulSoup

page_to_scrap = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(page_to_scrap.text, "html.parser")
quotes = soup.findAll("span", attrs={"class":"text"})
authors = soup.findAll("small", attrs={"class":"author"})


for quote,author in zip(quotes, authors):
    print(f"{quote.text} - {author.text}")