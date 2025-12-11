from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import threading
import concurrent.futures
import functools
from requests.exceptions import ChunkedEncodingError
from lxml import etree
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date

def reformatDateString(s):
	res = str()
	res += s[0:2]
	month = s[3:6]
	year = s[7:11]
	match month:
		case "იან":
			res += f"/01/{year}"
		case "თებ":
			res += f"/02/{year}"
		case "მარ":
			res += f"/03/{year}"
		case "აპრ":
			res += f"/04/{year}"
		case "მაი":
			res += f"/05/{year}"
		case "ივნ":
			res += f"/06/{year}"
		case "ივლ":
			res += f"/07/{year}"
		case "აგვ":
			res += f"/08/{year}"
		case "სექ":
			res += f"/09/{year}"
		case "ოქტ":
			res += f"/10/{year}"
		case "ნოე":
			res += f"/11/{year}"
		case "დეკ":
			res += f"/12/{year}"
		case "საა":
			res = date.today().strftime("%d/%m/%Y")
	return res

def cleanInnerHTML(s):
	r = str()
	for i in s:
		if (i.isnumeric() or i == '.'):
			r += i
		if(i == 'მ'):
			break
	return r

def numbersOnly(s):
	r = str()
	for i in s:
		if(i.isnumeric()):
			r += i
	return r
	
def choosePurchaseType(driver, pt):
	match pt:
		#1 is sale. 2 is rent.
		case "1":
			print("For Sale")
		case "2":
			driver.find_element(By.CSS_SELECTOR,"div.sc-dbb89033-53:nth-child(2)").click()
			print("Purchase type ok")

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
	print("Building Type OK")


def chooseLocation(driver,building_location):
	driver.find_element(By.CSS_SELECTOR,"div.sc-d0e1139e-0:nth-child(2)").click()
	match building_location:
		case "1":
			driver.find_element(By.CSS_SELECTOR,"div.sc-3cdbea70-0:nth-child(1)").click()
			driver.find_element(By.CSS_SELECTOR,".sc-d0e1139e-39 > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > svg:nth-child(1)").click()
			
		case "2":
			driver.find_element(By.CSS_SELECTOR,"div.sc-3cdbea70-0:nth-child(1)").click()
			driver.find_element(By.CSS_SELECTOR,".sc-d0e1139e-39 > div:nth-child(1) > div:nth-child(11) > div:nth-child(1) > svg:nth-child(1)").click()
			
		case "3":
			driver.find_element(By.CSS_SELECTOR,"div.sc-3cdbea70-0:nth-child(1)").click()
			driver.find_element(By.CSS_SELECTOR,".sc-d0e1139e-39 > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > svg:nth-child(1)").click()
			driver.find_element(By.CSS_SELECTOR,".sc-d0e1139e-39 > div:nth-child(1) > div:nth-child(11) > div:nth-child(1) > svg:nth-child(1)").click()
			
		case "4":
			driver.find_element(By.CSS_SELECTOR,"div.sc-3cdbea70-0:nth-child(1)").click()
			driver.find_element(By.CSS_SELECTOR,".sc-d0e1139e-39 > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)").click()
			
		case "5":
			driver.find_element(By.CSS_SELECTOR,"div.sc-3cdbea70-0:nth-child(1)").click()
			driver.find_element(By.CSS_SELECTOR,".sc-d0e1139e-39 > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)").click()
			
		case "6":
			driver.find_element(By.CSS_SELECTOR,"div.sc-3cdbea70-0:nth-child(1)").click()
			driver.find_element(By.CSS_SELECTOR,".sc-d0e1139e-39 > div:nth-child(4) > div:nth-child(1) > div:nth-child(1)").click()
			
		case "7":
			driver.find_element(By.CSS_SELECTOR,"div.sc-3cdbea70-0:nth-child(1)").click()
			driver.find_element(By.CSS_SELECTOR,".sc-d0e1139e-39 > div:nth-child(5) > div:nth-child(1) > div:nth-child(1)").click()
			
		case "8":
			driver.find_element(By.CSS_SELECTOR,"div.sc-3cdbea70-0:nth-child(1)").click()
			driver.find_element(By.CSS_SELECTOR,".sc-d0e1139e-39 > div:nth-child(1) > div:nth-child(9) > div:nth-child(1)").click()
			driver.find_element(By.CSS_SELECTOR,".sc-d0e1139e-39 > div:nth-child(1) > div:nth-child(10) > div:nth-child(1)").click()
			
		case "9":
			driver.find_element(By.CSS_SELECTOR,"div.sc-3cdbea70-0:nth-child(1)").click()
			driver.find_element(By.CSS_SELECTOR,".sc-d0e1139e-39 > div:nth-child(1) > div:nth-child(6) > div:nth-child(1)").click()
			
		case "10":
			driver.find_element(By.CSS_SELECTOR,"div.sc-3cdbea70-0:nth-child(2)").click()
			driver.find_element(By.CSS_SELECTOR,".sc-d0e1139e-35 > div:nth-child(1)").click()
			
		case "11":
			driver.find_element(By.CSS_SELECTOR,"div.sc-3cdbea70-0:nth-child(2)").click()
			driver.find_element(By.CSS_SELECTOR,"div.sc-d0e1139e-34:nth-child(9) > div:nth-child(1)").click()
			
		case "12":
			driver.find_element(By.CSS_SELECTOR,"div.sc-3cdbea70-0:nth-child(2)").click()
			driver.find_element(By.CSS_SELECTOR,"div.sc-d0e1139e-34:nth-child(12)").click()
			
		case "13":
			driver.find_element(By.CSS_SELECTOR,"div.sc-3cdbea70-0:nth-child(2)").click()
			driver.find_element(By.CSS_SELECTOR,"div.sc-d0e1139e-34:nth-child(5) > div:nth-child(1)").click()
			
		case "14":
			driver.find_element(By.CSS_SELECTOR,"div.sc-3cdbea70-0:nth-child(2)").click()
			driver.find_element(By.CSS_SELECTOR,"div.sc-d0e1139e-34:nth-child(8) > div:nth-child(1)").click()
			
		case "15":
			driver.find_element(By.CSS_SELECTOR,"div.sc-3cdbea70-0:nth-child(2)").click()
			driver.find_element(By.CSS_SELECTOR,"div.sc-d0e1139e-34:nth-child(10) > div:nth-child(1)").click()
			
	driver.find_element(By.CSS_SELECTOR,".ifgFgM").click()
	print("Location OK")

def chooseSurfaceArea(driver,lower_area_bound,upper_area_bound,rooms = 0):
	driver.find_element(By.CSS_SELECTOR, "div.sc-d0e1139e-0:nth-child(3)").click()
	driver.find_element(By.CSS_SELECTOR, "div.sc-d0e1139e-47:nth-child(1) > input:nth-child(1)").send_keys(lower_area_bound)
	driver.find_element(By.CSS_SELECTOR, "div.sc-d0e1139e-47:nth-child(2) > input:nth-child(1)").send_keys(upper_area_bound)
	print("Surface area partly ok")
	a = (rooms == 6)
	if(rooms > 0):
		match a:
			case True:
				driver.find_element(By.CSS_SELECTOR,"div.sc-dbb89033-48:nth-child(6)").click()
			case False:
				driver.find_element(By.CSS_SELECTOR,f"div.sc-dbb89033-48:nth-child({rooms})").click()
	driver.find_element(By.CSS_SELECTOR, ".sc-d0e1139e-50 > button:nth-child(2)").click()
	print("Surface Area OK")


def choosePriceRange(driver,lower_price_bound,upper_price_bound):
	driver.find_element(By.CSS_SELECTOR,"div.sc-d0e1139e-0:nth-child(4)").click()
	driver.find_element(By.CSS_SELECTOR,"div.sc-d0e1139e-47:nth-child(1) > input:nth-child(1)").send_keys(lower_price_bound)
	driver.find_element(By.CSS_SELECTOR,"div.sc-d0e1139e-47:nth-child(2) > input:nth-child(1)").send_keys(upper_price_bound)
	driver.find_element(By.CSS_SELECTOR,".sc-d0e1139e-50 > button:nth-child(2)").click()
	print("Price range OK")


def selectOnlyRefurbished(driver,bedrooms_min = 0, bedrooms_max = 0):
	driver.find_element(By.CSS_SELECTOR,".hnQkWA").click()
	print(bedrooms_min)
	print(bedrooms_max)
	if(bedrooms_min > 0):
		b = driver.find_element(By.CSS_SELECTOR,"div.sc-d0e1139e-24:nth-child(15) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)")
		ActionChains(driver)\
			.scroll_to_element(b)\
			.perform()	
		b.send_keys(bedrooms_min)
	if(bedrooms_max > 0):	
		driver.find_element(By.CSS_SELECTOR,"div.sc-d0e1139e-24:nth-child(15) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > input:nth-child(1)").send_keys(bedrooms_max)
	driver.find_element(By.CSS_SELECTOR,".ifgFgM").click()

def insertTextString(driver,text):
	if(len(text) > 0):
		driver.find_element(By.CSS_SELECTOR,".sc-dbb89033-3").send_keys(text)

def searchApartments(driver):
	driver.find_element(By.CSS_SELECTOR,"button.hMWxyW:nth-child(1)").click()
#-------------------
def writeInfoInFile(data,name):
	f = open(name,"w")
	f.write(data)
	f.close()
	
def createIdentifier(url):
	return url[url.rfind("-")+1:]

#-------------------------------------------	
def testHTML(driver,html,page_num):
	rets = 20
	res = None
	url_elements = []
	for i in range(0,rets):
		try:
			url_elements_div = html.find("div",class_="sc-1384a2b8-6 jlmink")
			url_elements = url_elements_div.find_all("a")
		except AttributeError:
			response = requests.get(driver.current_url + f"&page={page_num + 1}")
			print("Caught html")
			html = BeautifulSoup(response.text,"lxml")
	#print(type(url_elements))
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
	attempts = 10
	for i in range(0,attempts):
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
	for index,i in enumerate(html_list):
		print(index)
		price_elements = i.find_all("span", class_="sc-6e54cb25-2 cikpcz listing-detailed-item-price")
		address_elements = i.find_all("h5",class_="sc-6a44cedd-12 otbuX listing-detailed-item-address")
		baf_elements = i.find_all("div",class_="sc-6a44cedd-14 kWMcbj")
		url_elements = testHTML(driver,i,index)
		room_elements = i.find_all("h2",class_="sc-6e54cb25-3 gxoxbm listing-detailed-item-title")
		date_elements = i.find_all("div", class_= "create-date")
		for j in range(0,len(price_elements)):
			elem_dict = dict()
			pr = price_elements[j].decode_contents()
			address = address_elements[j].get_text(strip = True)
			baf_tag = baf_elements[j]
			room_num = room_elements[j].get_text(strip = True)
			date = reformatDateString(date_elements[j].get_text())
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
			try:	
				url = url_elements[j].get("href")
				elem_dict.update({"url": "https://home.ss.ge" + url})
				elem_dict.update({"identifier": createIdentifier(url)})
				elem_dict.update({"date": date})
				elem_dict.update({"price_usd":cleanInnerHTML(pr)})
				elem_dict.update({"address":address})
				elem_dict.update({"rooms":numbersOnly(room_num)})
				elem_dict.update({"area_m2":cleanInnerHTML(area)})
				elem_dict.update({"bedrooms":bedrooms})
				elem_dict.update({"floor_raw":floor})
				info_list.append(elem_dict)
			except:
				print("one omitted")
				
	return info_list

def getUrlsForImages(info_list):
	url_list = []
	print("Getting URLs for images")
	for apartment in info_list:
		url = apartment["url"]
		url_list.append(url)
	return url_list
	"""
def collectImages(url):
	a = dict()	
	options = webdriver.ChromeOptions()
	options.add_argument('--headless=new')
	dr = webdriver.Chrome(options = options)
	try:
		dr.get(url)
		images = dr.find_element(By.CSS_SELECTOR,".lg-react-element")
		img_list = images.find_elements(By.TAG_NAME,"img")
		for i in range(0,len(img_list)):
			a.update({f"Img{i+1}":img_list[i].get_attribute("src")})
	except:
		print("No images")
	return a 
	"""
def getImages(url_list):
	res = []
	with concurrent.futures.ThreadPoolExecutor(max_workers = 2) as executor:
		futures = [executor.submit(collectImages,url) for url in url_list]
		for f in futures:
			res.append(f.result())
	return res
def mergeLists(info_list,image_dicts_list):
	res = []
	if(len(info_list) == len(image_dicts_list)):
		for i in range(0,len(info_list)):
			z = info_list[i] | image_dicts_list[i]
			res.append(z)
	else:
		res = info_list	
	return res
	
def infoEquality(info1, info2,filter_strength):
	lim = 0
	if(info1["price_usd"] == info2["price_usd"]):
		lim = lim + 1
	if(info1["area_m2"] == info2["area_m2"]):
		lim = lim + 1
	if(info1["bedrooms"] == info2["bedrooms"]):
		lim = lim + 1
	if(info1["floor_raw"] == info2["floor_raw"]):
		lim = lim + 1
	"""
	for i in range(0,len(info1)-4):
		try:
			a = info1[f"Img{i+1}"]
			b = info2[f"Img{i+1}"]
			if (a == b):
				slim = lim + 1		
		except:
			print("No Comparison")
	"""
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
		
#async def getAndSearch():
	
