import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

url = "https://www.udemy.com/course/automate-your-life-with-python/?referralCode=7FA8B361D7A92B03A8C3"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Use find method to get the meta tag with property 'udemy_com:price'
price_tag = soup.find("meta", {"property": "udemy_com:price"})

# Extract the price
price = price_tag["content"] if price_tag else "Price not found"


# The nickname for the URL
nickname = "Python Course"

# Get today's date
today = datetime.today().strftime("%Y-%m-%d")

# The data to save
data = [nickname, today, price]

# The name of the CSV file
filename = "prices.csv"

# Open the file in append mode ('a')
with open(filename, "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(data)


# Open the file in read mode ('r')
with open(filename, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
