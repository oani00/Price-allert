from bs4 import BeautifulSoup
from lxml import etree
import requests

# Make a request to the website
r = requests.get("https://www.udemy.com/course/automate-your-life-with-python/?referralCode=7FA8B361D7A92B03A8C3")
soup = BeautifulSoup(r.content, 'html.parser')

# Convert the soup object to an lxml etree object
dom = etree.HTML(str(soup))

# Use the .xpath method to find elements
elements = dom.xpath('/html/body/div[1]/div[2]/div/div/main/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div/div[2]/div/div/div/span[2]/span')

# Print the text content of each element
for element in elements:
    print(element.text)
