from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
from requests.exceptions import ChunkedEncodingError
from lxml import etree
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def cleanInnerHTML(s):
	r = str()
	for i in s:
		if (i.isnumeric() or i == '.'):
			r += i
		if(i == 'მ'):
			break
	return r

def choosePurchaseType(driver, pt):
	match pt:
		#1 is sale. 2 is rent.
		case "1":
			driver.find_element(By.CSS_SELECTOR,"div.sc-dbb89033-53:nth-child(1)").click()
		case "2":
			driver.find_element(By.CSS_SELECTOR,"div.sc-dbb89033-53:nth-child(2)").click()


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

def insertTextString(driver,text):
	if(len(text) > 0):
		driver.find_element(By.CSS_SELECTOR,".sc-dbb89033-3").send_keys(text)

def searchApartments(driver):
	driver.find_element(By.CSS_SELECTOR,"button.dICGws:nth-child(1)").click()
#-------------------
def writeInfoInFile(data,name):
	f = open(name,"w")
	f.write(data)
	f.close()
	
def createIdentifier(url):
	return url[url.rfind("-")+1:]

#-------------------------------------------	
def testHTML(driver,html,page_num):
	rets = 5
	res = None
	for i in range(0,rets):
		try:
			url_elements_div = html.find("div",class_="sc-1384a2b8-6 jlmink")
			url_elements = url_elements_div.find_all("a")
		except AttributeError:
			response = requests.get(driver.current_url + f"&page={page_num + 1}")
			print("Caught html")
			html = BeautifulSoup(response.text,"lxml")
	print(type(url_elements))
	return url_elements
	
def tryRequesting(url):
	rets = 5
	response = None
	for i in range(0,rets):
		try:
			response = requests.get(url)
			if(str(type(response)) == '<class \'requests.models.Response\'>'):
				break
		except ChunkedEncodingError:
			print("Caught chunks")
	return response
#------------------------------------
def createHTMLList(driver):
	print("Creating list")
	html_list = []
	url_list = []
	try:
		limit_getter = driver.find_element(By.CSS_SELECTOR,".sc-1384a2b8-9")
		limit_elements = limit_getter.find_elements(By.TAG_NAME,"div")
		lim = limit_elements[-2].get_attribute("innerHTML")
	except:
		lim = '0'
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
			response = tryRequesting(i)
			ht = BeautifulSoup(response.text,"lxml")
			html_list.append(ht)
			print(l)
			l = l + 1
	else:
		response = tryRequesting(url)
		ht = BeautifulSoup(response.text,"lxml")
		html_list.append(ht)
	return html_list


def getInformation(driver,html_list):
	print("In getinfo")
	info_list = []
	l = 0
	for i in html_list:
		print(l)
		price_elements = i.find_all("span", class_="sc-6e54cb25-2 cikpcz listing-detailed-item-price")
		address_elements = i.find_all("h5",class_="sc-bc0f943e-12 kIDemC listing-detailed-item-address")
		baf_elements = i.find_all("div",class_="sc-bc0f943e-13 bbhwop")
		url_elements = testHTML(driver,i,l)
		l = l + 1
		for j in range(0,len(price_elements)):
			elem_dict = dict()
			pr = price_elements[j].decode_contents()
			address = address_elements[j].get_text(strip = True)
			baf_tag = baf_elements[j]
			try:
				area = baf_tag.select("div:first-child")[0].get_text(strip=True)
			except:
				print("no area")
				area = '0'
			try:
				bedrooms = baf_tag.select("div:nth-of-type(2)")[0].get_text(strip=True)
			except:
				print("no bedrooms")
				bedrooms = '0'
			try:
				floor = baf_tag.select("div:nth-of-type(3)")[0].get_text(strip=True)
			except:
				print("no floors")
				floor = '0/0'
			url = url_elements[j].get("href")
			elem_dict.update({"url": "https://home.ss.ge" + url})
			elem_dict.update({"identifier": createIdentifier(url)})
			elem_dict.update({"price($)":cleanInnerHTML(pr)})
			elem_dict.update({"address":address})
			elem_dict.update({"area (m^2)":cleanInnerHTML(area)})
			elem_dict.update({"bedrooms":bedrooms})
			elem_dict.update({"floor":floor})
			info_list.append(elem_dict)
	return info_list

def getImages(driver,info_list):
	print("In getimages")
	for apartment in info_list:
		url = apartment["url"]
		print(url)
		driver.get(url)
		try:
			print("Fine 1")
			images = driver.find_element(By.CSS_SELECTOR,".lg-react-element")
			print("Fine 2")
		except:
			print("No images")
		img_list = images.find_elements(By.TAG_NAME,"img")
		print("Fine 3")
		for i in range(0,len(img_list)):
			print(len(img_list))
			apartment.update({f"Img{i+1}":img_list[i].get_attribute("src")})
	
def infoEquality(info1, info2,filter_strength):
	lim = 0
	if(info1["price($)"] == info2["price($)"]):
		lim = lim + 1
	if(info1["area (m^2)"] == info2["area (m^2)"]):
		lim = lim + 1
	if(info1["bedrooms"] == info2["bedrooms"]):
		lim = lim + 1
	if(info1["floor"] == info2["floor"]):
		lim = lim + 1
	for i in range(0,len(info1)-4):
		try:
			a = info1[f"Img{i+1}"]
			b = info2[f"Img{i+1}"]
			if (a == b):
				slim = lim + 1		
		except:
			print("No Comparison")
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
		
		
		
