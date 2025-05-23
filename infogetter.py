from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def chooseBuildingType(driver):
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
	
def writeInfoInFile(data,name):
	f = open(name,"w")
	f.write(data)
	f.close()
	
def createIdentifier(url):
	return url[url.rfind("-")+1:]
	
def nextPageCSSSelector(current_page):
	next_page_css_number = current_page + 2
	return f"div.sc-1384a2b8-10:nth-child({next_page_css_number})"
		
def pageTurner(driver, next_page):
	driver.find_element(By.CSS_SELECTOR,next_page).click()
	

def createDictionary(driver):
	rset = dict()
	for i in range(1,17):
		url_address = f"/html/body/div[1]/main/div[2]/div[3]/div[1]/a[{i}]"
		location_address = f"/html/body/div[1]/main/div[2]/div[3]/div[1]/a[{i}]/div/div[4]/h5"
		price_address = f"/html/body/div[1]/main/div[2]/div[3]/div[1]/a[{i}]/div/div[4]/div[1]/span[1]"
		area_address = f"/html/body/div[1]/main/div[2]/div[3]/div[1]/a[{i}]/div/div[4]/div[2]/div[1]"
		floor_address = f"/html/body/div[1]/main/div[2]/div[3]/div[1]/a[{i}]/div/div[4]/div[2]/div[3]"
		url = driver.find_element(By.XPATH,url_address).get_attribute('href')
		identifier = createIdentifier(url)
		address = driver.find_element(By.XPATH,location_address).get_attribute('innerHTML').removeprefix("<span class=\"icon-location_on-fill\" style=\"max-width: 1em; overflow: hidden;\"></span>")
		price = driver.find_element(By.XPATH,price_address).get_attribute('innerHTML')
		area = driver.find_element(By.XPATH,area_address).get_attribute('innerHTML').removeprefix("<span class=\"icon-crop_free\" style=\"max-width: 1em; overflow: hidden;\"></span>")
		floor = driver.find_element(By.XPATH,floor_address).get_attribute('innerHTML').removeprefix("<span class=\"icon-stairs\" style=\"max-width: 1em; overflow: hidden;\"></span>")
		rset.update({"Identifier" : identifier})
		rset.update({"url" : url})
		rset.update({"price" : price})
		rset.update({"address" : address})
		rset.update({"area" : area})
		rset.update({"floor" : floor})
		url = None
		identifier = None
		address = None 
		price = None 
		area = None
		floor = None
	return rset

def getInformation(driver):
	rset = dict()
	arrdicts = []
	current_page = 1
	next_page = nextPageCSSSelector(current_page)
	while(driver.find_element(By.CSS_SELECTOR,next_page).is_enabled()):
			a = createDictionary(driver) #Gives
			arrdicts.append(a)
			pageTurner(driver,next_page) #page changes here
			current_page = current_page + 1
			next_page = nextPageCSSSelector(current_page)
			WebDriverWait(driver,5).until()
	arrdicts.append(createDictionary(driver))
	return arrdicts
		


