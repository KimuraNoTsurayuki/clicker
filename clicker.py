from selenium import webdriver
import time
import infogetter
import jsonwriter

		
driver = webdriver.Chrome()
ws = driver.get("https://home.ss.ge")
driver.explicitly_wait(5)
infogetter.chooseBuildingType(driver)
infogetter.chooseLocation(driver)
infogetter.chooseSurfaceArea(driver)
infogetter.choosePriceRange(driver)
infogetter.searchApartments(driver)
jsonwriter.writeJSONFile(infogetter.getInformation(driver))
time.sleep(10)
driver.close()


