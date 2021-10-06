from os import name
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://lds.com.np/laptop?limit=100'
extract_file = "../../extracted-data/ids.txt"
data = []

req = requests.get(url)
htmlcontent = req.content

soup = BeautifulSoup(htmlcontent, 'html.parser')
desired_content_name = soup.find_all(class_='name')
desired_content_desc = soup.find_all(class_='description')
desired_content_price = soup.find_all(class_='price-new')

for i in range(0,len(desired_content_name)):
    title = desired_content_name[i].get_text()
    description = desired_content_desc[i].get_text()
    price = desired_content_price[i].get_text()
    data.append(title + ","+ description + "," + price + '\n')

with open(extract_file,'w') as file:
    for row in data:
        file.write(row)




