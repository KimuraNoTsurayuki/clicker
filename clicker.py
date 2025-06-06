from selenium import webdriver
import time
import infogetter as info
import jsonwriter
import sys
import gui as g



if __name__ == '__main__':
	options = webdriver.ChromeOptions()
	options.add_argument('--headless=new')
	driver = webdriver.Chrome(options = options)
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
	print("building type: " + building_type)
	print("building location: " + building_location)
	print("area lower: " + str(area_lower_bound))
	print("area upper: " + str(area_upper_bound))
	print("price lower: " + str(price_lower_bound))
	print("price upper: " + str(price_upper_bound))
	ws = driver.get("https://home.ss.ge")
	driver.implicitly_wait(5)
	info.chooseBuildingType(driver,building_type)
	info.chooseLocation(driver,building_location)
	info.chooseSurfaceArea(driver,area_lower_bound,area_upper_bound)
	info.choosePriceRange(driver,price_lower_bound,price_upper_bound)
	info.searchApartments(driver)
	html_list = g.info.createHTMLList(driver)
	info_list = g.info.getInformation(html_list)
	jsonwriter.writeJSONFile(info_list)
	time.sleep(10)
	driver.close()


