import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime


class Target:
    def __init__(self, nickname, url, tag, property):
        self.nickname = nickname
        self.url = url
        self.tag = tag
        self.property = property


def fetch_price(target):
    response = requests.get(target.url)
    soup = BeautifulSoup(response.text, "html.parser")
    price_tag = soup.find("meta", {"property": target.property})
    return price_tag["content"] if price_tag else "Price not found"


def save_price(target, price):
    today = datetime.today().strftime("%Y-%m-%d")
    with open("prices.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([target.nickname, today, price])


def scrape_prices(targets):
    for target in targets:
        price = fetch_price(target)
        save_price(target, price)


targets = [
    Target(
        "Python Course",
        "https://www.udemy.com/course/automate-your-life-with-python/?referralCode=7FA8B361D7A92B03A8C3",
        ".your-css-selector",
    ),
    # Add more Target objects here...
]

scrape_prices(targets)
