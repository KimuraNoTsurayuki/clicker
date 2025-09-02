from selenium import webdriver
import time
import infogetter as info
import jsonwriter
import datatohtml as dh
import sys
import gui as g
import os
from datetime import datetime

if __name__ == '__main__':
	options = webdriver.ChromeOptions()
	options.add_argument('--headless=new')
	driver = webdriver.Chrome()
	app = g.QApplication(sys.argv)
	window = g.BasicGUI()
	window.resize(500,500)
	window.show()
	app.exec()
	building_type = g.building_type_to_send
	building_location = g.building_location_to_send
	area_lower_bound = g.area_to_send_lower
	area_upper_bound = g.area_to_send_upper
	price_lower_bound = g.price_to_send_lower
	price_upper_bound = g.price_to_send_upper
	filter_strength = g.filter_strength
	type_of_purchase = g.purchase_type
	rooms_amount = g.rooms
	min_bedrooms = g.bedrooms_min
	max_bedrooms = g.bedrooms_max
	dt = datetime.now().date()
	hr = datetime.now().time()
	dt = dt.strftime("%Y-%m-%d")
	hr = hr.strftime("%H:%M:%S")
	date_str = dt + "_" + hr
	print("type of purchase: " + type_of_purchase)
	text_search_str = g.search_text
	print("building type: " + building_type)
	print("building location: " + building_location)
	print("area lower: " + str(area_lower_bound))
	print("area upper: " + str(area_upper_bound))
	print("price lower: " + str(price_lower_bound))
	print("price upper: " + str(price_upper_bound))
	print("filter strength: " + str(filter_strength))
	print("type of purchase: " + type_of_purchase)
	print("Search Text: " + text_search_str)
	ws = driver.get("https://home.ss.ge")
	driver.implicitly_wait(5)
	info.choosePurchaseType(driver,type_of_purchase)
	info.chooseBuildingType(driver,building_type)
	info.chooseLocation(driver,building_location)
	info.chooseSurfaceArea(driver,area_lower_bound,area_upper_bound,rooms_amount)
	info.choosePriceRange(driver,price_lower_bound,price_upper_bound)
	info.insertTextString(driver,text_search_str)
	info.selectOnlyRefurbished(driver,min_bedrooms,max_bedrooms)
	info.searchApartments(driver)
	html_list = info.createHTMLList(driver)
	info_list = info.getInformation(driver,html_list)
	refined_info_list = info.filterInfoList(info_list,filter_strength)
	#url_list = info.getUrlsForImages(refined_info_list)
	#image_dicts_list = info.getImages(url_list)
	#new_info_list = info.mergeLists(refined_info_list,image_dicts_list)
	#display_html = dh.listToValidHTML(refined_info_list)
	#fl = open("test.html","w")
	#fl.write(display_html)
	#fl.close()
	os.chdir('./databases')
	jsonwriter.setName(date_str,type_of_purchase,building_location,filter_strength,price_lower_bound,price_upper_bound,area_lower_bound,area_upper_bound,"filtered")
	jsonwriter.writeJSONFile(refined_info_list)
	#jsonwriter.setName(type_of_purchase,building_location,filter_strength,price_lower_bound,price_upper_bound,area_lower_bound,area_upper_bound,"unfiltered")
	#jsonwriter.writeJSONFile(info_list)
	driver.close()
