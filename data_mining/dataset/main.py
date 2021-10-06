print("Scrape the dataset from...")
# import the necessary library 
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Request to website and download HTML contents
url='https://www.gadgetbytenepal.com/category/laptop-price-in-nepal/'


# write data in a file.
file1 = open("alldata.txt","w")


req=requests.get(url)
htmlcontent=req.content
# print(content)


# Format the downloadable content
soup=BeautifulSoup(htmlcontent, 'html.parser')
# print(soup.prettify())

desired_content = soup.find(class_='td-category-description')
print("############################################################")
# print(desired_content.prettify())
print("############################################################")


data_header = desired_content.find_all('h2')
print("############################################################")
#print(data_header)
print("############################################################")
print("############################################################")
#for item in data_header:
	#print(item.get_text())
print("############################################################")


data_items = desired_content.find_all('div', class_ = 'su-table su-table-alternate')
print("############################################################")
# print(data_items)
print("############################################################")


print("############################################################")
i=0
for item in data_items:
	print("############################################################")
	# print(item)
	eachrow = item.find_all('tr')
	for tabledata in eachrow:
		print(tabledata.get_text())
		file1.writelines(tabledata.get_text())
		i=i+1
		print("\n",i)

print("############################################################")

file1.close()
































