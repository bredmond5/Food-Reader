
from urllib.request import urlopen as ureq 	#use this one if you're running it as python3 priceScrape.py
#from urllib2 import urlopen as ureq			#use this one if you're running it as python priceScrape.py
from bs4 import BeautifulSoup as soup
from xlwt import Workbook


wb = Workbook()								#creating an xls file
sheet1 = wb.add_sheet("Sheet 1")			#creating the columns and setting widths for writing info
sheet1.col(0).width = 14000
sheet1.col(1).width = 2500
sheet1.col(2).width = 3500
sheet1.col(3).width = 4000
sheet1.col(4).width = 4000

groceryUrlBeginning = "https://www.mygrocerydeals.com/deals?utf8=%E2%9C%93&authenticity_token=KFo1qPeErMj0RspD%2F8AhWJlc9BChi8x8L6irKF9pfCDTL4%2B7TkK0EgkeC85l933qffsBAuiYEHhOFgqQUy0nJg%3D%3D&remove%5B%5D=chains&remove%5B%5D=categories&remove%5B%5D=collection&remove%5B%5D=collection_id&q="
groceryUrlEnd = "&supplied_location=93107&latitude=34.42&longitude=-119.69999999999999"

walmartUrlBeginning = "https://www.walmart.com/search/?cat_id=0&query="

targetUrlBeginning = "https://www.target.com/s?searchTerm="

amazonUrlBeginning = "https://www.amazon.com/s?k="



product = input("Please enter the product: ")
fileName = product.title().replace(" ", "") + ".xls"
product = product.replace(" ", "+")





############################################################Searches mygrocerydeals.com############################################################


url = groceryUrlBeginning + product + groceryUrlEnd 	#page URL

uclient = ureq(url) 					#opening connection to website	
pageHTMl = uclient.read()				#reading HTML
uclient.close()
content = soup(pageHTMl, "html.parser")

#grabs each product
itemContainers = content.findAll("div", {"data-type":"special"})


count = 0 																			#counter for going row by row
for container in itemContainers:
	productNameContainer = container.findAll("p", {"class":"deal-productname"})		#Finding product name
	productName = productNameContainer[0].text
	sheet1.write(count, 0, productName)

	sizeContainer = container.findAll("div", {"class":"uom"})						#Finding size/count of product
	size = sizeContainer[0].text
	sheet1.write(count, 1, size)

	priceContainer = container.findAll("span", {"class":"pricetag"})				#Finding Price
	price = priceContainer[0].text
	sheet1.write(count, 2, price)

	dealEndContainer = container.findAll("div", {"class":"expirydate"})				#Finding deal end date
	dealEnd = dealEndContainer[0].text
	sheet1.write(count, 3, dealEnd)

	storeNameContainer = container.findAll("p", {"class":"deal-storename"})			#Finding store of sale
	storeName = storeNameContainer[0].text
	sheet1.write(count, 4, storeName)

	count+=1

###################################################################################################################################################


############################################################Searches amazon.com#############################################################

# url = amazonUrlBeginning + product

# uclient = ureq(url) 					#opening connection to website	
# pageHTMl = uclient.read()				#reading HTML
# uclient.close()
# content = soup(pageHTMl, "html.parser")

# priceContainer = content.findAll("span", {"class":"a-price"})
# price = price[0].span.text


wb.save(fileName)
