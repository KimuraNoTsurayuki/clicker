from selenium import webdriver
import time
import infogetter
import jsonwriter

		
driver = webdriver.Chrome()
ws = driver.get("https://home.ss.ge")
driver.implicitly_wait(5)
infogetter.chooseBuildingType(driver)
infogetter.chooseLocation(driver)
infogetter.chooseSurfaceArea(driver)
infogetter.choosePriceRange(driver)
infogetter.searchApartments(driver)
a = infogetter.createHTMLList(driver)
infogetter.getInformation(a)
time.sleep(10)
driver.close()


