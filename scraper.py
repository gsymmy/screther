import requests
from bs4 import BeautifulSoup
import csv


def scrape_ether():
    response = requests.get("https://www.coinbase.com/price/ethereum")
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    tweet = soup.find(class_="ChartPriceHeader__BigAmount-sc-9ry7zl-4 dKeshi")
    return tweet.get_text()

scrape_ether()