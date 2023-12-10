import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

class Target:
    def __init__(self, nickname, url, selector):
        self.nickname = nickname
        self.url = url
        self.selector = selector

def get_price(target):
    response = requests.get(target.url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Use the CSS selector to get the price tag
    price_tag = soup.select_one(target.selector)

    # Extract the price
    price = price_tag.text if price_tag else "Price not found"
    return price

def save_price(target, price):
    # Get today's date
    today = datetime.today().strftime("%Y-%m-%d")

    # The data to save
    data = [target.nickname, today, price]

    # The name of the CSV file
    filename = "prices.csv"

    # Open the file in append mode ('a')
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data)

    

def print_prices():
    # Open the file in read mode ('r')
    with open("prices.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

# Define your targets
targets = [
    Target("Samsung TV___", "https://www.amazon.com.br/Samsung-Smart-Crystal-UHD-CU7700/dp/B0C1538ZJ4?ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147", '#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center.aok-relative > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span:nth-child(2) > span.a-price-whole'),
    Target("Python Course", "https://www.udemy.com/course/automate-your-life-with-python/?referralCode=7FA8B361D7A92B03A8C3", 'body > table > tbody > tr:nth-child(132) > td.line-content > span:nth-child(15) > span:nth-child(4)')
]

# Get and save prices for all targets
for target in targets:
    price = get_price(target)
    save_price(target, price)

# This line will print "Preços salvos" to the console
print("Precos salvos")

# Print all prices
print_prices()
