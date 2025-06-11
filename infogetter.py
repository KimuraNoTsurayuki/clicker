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
	#1 for new, 2 for old, 3 for construction
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

def chooseLocation(driver,building_location):
	driver.find_element(By.CSS_SELECTOR,"div.sc-dbb89033-0:nth-child(2)").click()
	driver.find_element(By.CSS_SELECTOR,"div.sc-3cdbea70-0:nth-child(1)").click()
	match building_location:
		case "1":
			property_location = driver.find_element(By.CSS_SELECTOR,".sc-dbb89033-39 > div:nth-child(1) > div:nth-child(3)")
		case "2":
			property_location = driver.find_element(By.CSS_SELECTOR, ".sc-dbb89033-39 > div:nth-child(1) > div:nth-child(11)")
	property_location.click()
	driver.find_element(By.CSS_SELECTOR,".ieRIPq").click()

def chooseSurfaceArea(driver,lower_area_bound,upper_area_bound):
	driver.find_element(By.CSS_SELECTOR, "div.sc-dbb89033-0:nth-child(3) > span:nth-child(2)").click()
	driver.find_element(By.CSS_SELECTOR, "div.sc-dbb89033-46:nth-child(1) > input:nth-child(1)").send_keys(lower_area_bound)
	driver.find_element(By.CSS_SELECTOR, "div.sc-dbb89033-46:nth-child(2) > input:nth-child(1)").send_keys(upper_area_bound)
	driver.find_element(By.CSS_SELECTOR, ".sc-dbb89033-49 > button:nth-child(2)").click()


def choosePriceRange(driver,lower_price_bound,upper_price_bound):
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
	print("Creating list")
	html_list = []
	url_list = []
	limit_getter = driver.find_element(By.CSS_SELECTOR,".sc-1384a2b8-9")
	limit_elements = limit_getter.find_elements(By.TAG_NAME,"div")
	print(len(limit_elements))
	lim = limit_elements[-2].get_attribute("innerHTML")
	print("limit is " + lim)
	url = driver.current_url
	l = 0
	if (int(lim) > 0):
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
	else:
		response = requests.get(url)
		ht = BeautifulSoup(response.text,"lxml")
		html_list.append()
	return html_list

def getInformation(html_list):
	print("In getinfo")
	info_list = []
	for i in html_list:
		price_elements = i.find_all("span", class_="sc-6e54cb25-2 cikpcz listing-detailed-item-price")
		address_elements = i.find_all("h5",class_="sc-bc0f943e-12 kIDemC listing-detailed-item-address")
		baf_elements = i.find_all("div",class_="sc-bc0f943e-13 bbhwop")
		url_elements_div = i.find("div",class_="sc-1384a2b8-6 jlmink")
		url_elements = url_elements_div.find_all("a")
		img_url_div = i.find_all("div",class_="sc-4bb73884-5 hUtkPJ")
		for j in range(0,len(price_elements)):
			elem_dict = dict()
			pr = price_elements[j].decode_contents()
			address = address_elements[j].get_text(strip = True)
			baf_tag = baf_elements[j]
			area = baf_tag.select("div:first-child")[0].get_text(strip=True)
			bedrooms = baf_tag.select("div:nth-of-type(2)")[0].get_text(strip=True)
			floor = baf_tag.select("div:nth-of-type(3)")[0].get_text(strip=True)
			url = url_elements[j].get("href")
			img_urls = img_url_div[0].find_all("img")
			elem_dict.update({"url": "https://home.ss.ge" + url})
			elem_dict.update({"identifier": createIdentifier(url)})
			elem_dict.update({"price":cleanInnerHTML(pr)})
			elem_dict.update({"address":address})
			elem_dict.update({"area (m^2)":cleanInnerHTML(area)})
			elem_dict.update({"bedrooms":bedrooms})
			elem_dict.update({"floor":floor})
			for k in range(0,len(img_urls)):
				elem_dict.update({f"Img{k+1}":img_urls[k]["src"]})
			info_list.append(elem_dict)
	return info_list
	
def infoEquality(info1, info2,filter_strength):
	lim = 0

	if(info1["price"] == info2["price"]):
		lim = lim + 1
	if(info1["area (m^2)"] == info2["area (m^2)"]):
		lim = lim + 1
	if(info1["bedrooms"] == info2["bedrooms"]):
		lim = lim + 1
	if(info1["floor"] == info2["floor"]):
		lim = lim + 1
	if(info1["Img1"] == info2["Img1"]):
		lim = lim + 1
	if(info1["Img2"] == info2["Img2"]):
		lim = lim + 1
	if(info1["Img3"] == info2["Img3"]):
		lim = lim + 1
	if (lim >= filter_strength and info1["address"] == info2["address"]):
		return True
	else:
		return False	
	
def filterInfoList(info_list,filter_strength):
	res = []
	take_out = set()
	for i in range(0,len(info_list)):
		for j in range(i+1,len(info_list)):
			if(infoEquality(info_list[i],info_list[j],filter_strength)):
				take_out.add(j)
	for k in range(0,len(info_list)):
		if k not in take_out:
			res.append(info_list[k])
	return res
		
		
		
