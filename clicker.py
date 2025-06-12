from selenium import webdriver
import time
import infogetter as info
import jsonwriter
import sys
import gui as g
import os

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
	info.chooseSurfaceArea(driver,area_lower_bound,area_upper_bound)
	info.choosePriceRange(driver,price_lower_bound,price_upper_bound)
	info.insertTextString(driver,text_search_str)
	info.searchApartments(driver)
	time.sleep(5)
	html_list = info.createHTMLList(driver)
	info_list = info.getInformation(html_list)
	refined_info_list = info.filterInfoList(info_list,filter_strength)
	os.chdir('./databases')
	jsonwriter.setName(type_of_purchase,building_location,filter_strength,price_lower_bound,price_upper_bound,area_lower_bound,area_upper_bound)
	jsonwriter.writeJSONFile(refined_info_list)
	driver.close()
