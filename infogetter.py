from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
from lxml import etree
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def cleanInnerHTML(s):
	r = str()
	for i in s:
		if (i.isnumeric() or i == '$'):
			r += i
		if(i == 'მ'):
			break
	return r

def chooseBuildingType(driver,building_type):
	driver.find_element(By.CLASS_NAME, "icon-chair").click()
	building_type = input("1 for new, 2 for old, 3 for construction: ")
	match building_type:
		case "1":
			building_elements = driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]")
		case "2":
			building_elements = driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[3]")
		case "3":
			building_elements = driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[2]")
	building_elements.click()
	b = driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div[2]/div/div[2]/div/div/div[2]/div[3]/button[2]")
	b.click()

def chooseLocation(driver):
	location = input("1 for Vake, 2 for Saburtalo: ")
	driver.find_element(By.CSS_SELECTOR,"div.sc-dbb89033-0:nth-child(2)").click()
	driver.find_element(By.CSS_SELECTOR,"div.sc-3cdbea70-0:nth-child(1)").click()
	match location:
		case "1":
			property_location = driver.find_element(By.CSS_SELECTOR,".sc-dbb89033-39 > div:nth-child(1) > div:nth-child(3)")
		case "2":
			property_location = driver.find_element(By.CSS_SELECTOR, ".sc-dbb89033-39 > div:nth-child(1) > div:nth-child(11)")
	property_location.click()
	driver.find_element(By.CSS_SELECTOR,".ieRIPq").click()

def chooseSurfaceArea(driver):
	driver.find_element(By.CSS_SELECTOR, "div.sc-dbb89033-0:nth-child(3) > span:nth-child(2)").click()
	lower_area_bound = input("Area lower bound: ")
	upper_area_bound = input("Area upper bound: ")
	driver.find_element(By.CSS_SELECTOR, "div.sc-dbb89033-46:nth-child(1) > input:nth-child(1)").send_keys(lower_area_bound)
	driver.find_element(By.CSS_SELECTOR, "div.sc-dbb89033-46:nth-child(2) > input:nth-child(1)").send_keys(upper_area_bound)
	driver.find_element(By.CSS_SELECTOR, ".sc-dbb89033-49 > button:nth-child(2)").click()


def choosePriceRange(driver):
	lower_price_bound = input("Lower price bound: ")
	upper_price_bound = input("Upper price bound: ")
	driver.find_element(By.CSS_SELECTOR,"div.sc-dbb89033-0:nth-child(4) > span:nth-child(2)").click()
	driver.find_element(By.CSS_SELECTOR,".currency-box > span:nth-child(3)").click()
	driver.find_element(By.CSS_SELECTOR,"div.sc-dbb89033-46:nth-child(1) > input:nth-child(1)").send_keys(lower_price_bound)
	driver.find_element(By.CSS_SELECTOR,"div.sc-dbb89033-46:nth-child(2) > input:nth-child(1)").send_keys(upper_price_bound)
	driver.find_element(By.CSS_SELECTOR,".sc-dbb89033-49 > button:nth-child(2)").click()

def searchApartments(driver):
	driver.find_element(By.CSS_SELECTOR,"button.dICGws:nth-child(1)").click()
#-------------------
def writeInfoInFile(data,name):
	f = open(name,"w")
	f.write(data)
	f.close()
	
def createIdentifier(url):
	return url[url.rfind("-")+1:]
	
#------------------------------------
def createHTMLList(driver):
	html_list = []
	url_list = []
	time.sleep(3)
	lim = driver.find_element(By.CSS_SELECTOR,"div.sc-1384a2b8-10:nth-child(6)").get_attribute('innerHTML')
	l = 0
	url = driver.current_url
	for i in range (0,int(lim)):
		app_str = f"&page={i+1}"
		if i >= 1:
			url = url[0:url.rfind('&')]	
		url += app_str
		url_list.append(url)
	for i in url_list:
		response = requests.get(i)
		ht = BeautifulSoup(response.text,"lxml")
		html_list.append(ht)
		print(l)
		l = l + 1
	return html_list

def getInformation(html_list):
	print("In getinfo")
	#url_address = f"/html/body/div[1]/main/div[2]/div[3]/div[1]/a[{i}]"
	#location_address = f"/html/body/div[1]/main/div[2]/div[3]/div[1]/a[{i}]/div/div[4]/h5"
	#price_address = f"/html/body/div[1]/main/div[2]/div[3]/div[1]/a[{i}]/div/div[4]/div[1]/span[1]"
	#area_address = f"/html/body/div[1]/main/div[2]/div[3]/div[1]/a[{i}]/div/div[4]/div[2]/div[1]"
	#floor_address = f"/html/body/div[1]/main/div[2]/div[3]/div[1]/a[{i}]/div/div[4]/div[2]/div[3]"
	info_list = []
	for i in html_list:
		price_elements = i.find_all("span", class_="sc-6e54cb25-2 cikpcz listing-detailed-item-price")
		address_elements = i.find_all("h5",class_="sc-bc0f943e-12 kIDemC listing-detailed-item-address")
		baf_elements = i.find_all("div",class_="sc-bc0f943e-13 bbhwop")
		for j in range(0,len(price_elements)):
			elem_dict = dict()
			pr = price_elements[j].decode_contents()
			address = address_elements[j].get_text(strip = True)
			baf_tag = baf_elements[j]
			area = baf_tag.select("div:first-child")[0].get_text(strip=True)
			bedrooms = baf_tag.select("div:nth-of-type(2)")[0].get_text(strip=True)
			floor = baf_tag.select("div:nth-of-type(3)")[0].get_text(strip=True)
			print(type(bedrooms))
			print(bedrooms)
			elem_dict.update({"price":cleanInnerHTML(pr)})
			elem_dict.update({"address":address})
			elem_dict.update({"area (m^2)":cleanInnerHTML(area)})
			elem_dict.update({"bedrooms":bedrooms})
			elem_dict.update({"floor":floor})
			info_list.append(elem_dict)
	return info_list
		
		

