print("Scrape the dataset from...")
print("https://bigbyte.com.np/laptops/?product-page=*")

# import the necessary library 
from bs4 import BeautifulSoup
import requests
import pandas as pd




# write data in a file.
# file1 = open("alldatabigbyte.txt","w")


# req=requests.get(url)
# htmlcontent=req.content
# print(content)


# Format the downloadable content
# soup=BeautifulSoup(htmlcontent, 'html.parser')
# print(soup.prettify())

# desired_content = soup.find(class_='td-category-description')
# print("############################################################")
# print(desired_content.prettify())
# print("############################################################")


# data_header = desired_content.find_all('h2')
# print("############################################################")
# print(data_header)
# print("############################################################")
# print("############################################################")
# for item in data_header:
	# print(item.get_text())
# print("############################################################")


#data_items = desired_content.find_all('div', class_ = 'su-table su-table-alternate')
# print("############################################################")
# print(data_items)
# print("############################################################")


# print("############################################################")
# i=0
# for item in data_items:
# 	print("############################################################")
	# print(item)
#	eachrow = item.find_all('tr')
#	for tabledata in eachrow:
#		print(tabledata.get_text())
#		i=i+1
#		print("\n",i)




# print("############################################################")
# file1.writelines(tabledata.get_text())
# file1.close()



def getdata(url):
	req=requests.get(url)
	htmlcontent=req.content
	soup=BeautifulSoup(htmlcontent, 'html.parser')
	return soup

def findnextpage(soup):
	currentpage = soup.find('span', {'class':'page-numbers current'}).get_text()
	nextpage =  int(currentpage)+ 1
	if nextpage <= 16:
		newurl ="https://bigbyte.com.np/laptops/?product-page="+str(nextpage) 
		print("returned url = ",newurl)
		return newurl
	else:
		return




# Request to website and download HTML contents
url='https://bigbyte.com.np/laptops/?product-page=1'

# write data in a file.
file1 = open("alldatabigbyte.txt","w")

while True:
	soup = getdata(url)
	desired_data = soup.find('ul', {'class':'products columns-3'})
	for item in desired_data:
		description = item.find('h2', {'class':'woocommerce-loop-product__title'})
		price = item.find('span', {'class': 'woocommerce-Price-amount amount'})
		print("############################################################")
		# print(description)
		print("############################################################")
		print("############################################################")
		# print(price)
		print("############################################################")
		print("############################################################")
		print("\n description=",description.get_text())
		file1.writelines(description.get_text())

		print("############################################################")
		print("\n prize=",price)
		if not price == None:
			print("\n prize=",price.get_text())	
			file1.writelines(price.get_text())
		else:
			print('Comming soon')
			file1.writelines("comming soon")
			
		file1.writelines("\n\n")
			
		
	
	
	
	
	
	
	url = findnextpage(soup)
	if not url:
		break
	print(url)
	
file1.close()
	








