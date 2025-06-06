from selenium import webdriver
import time
import infogetter
import jsonwriter


gui.startGUI()
options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
driver = webdriver.Chrome(options = options)
ws = driver.get("https://home.ss.ge")
driver.implicitly_wait(5)
infogetter.chooseBuildingType(driver)
infogetter.chooseLocation(driver)
infogetter.chooseSurfaceArea(driver)
infogetter.choosePriceRange(driver)
infogetter.searchApartments(driver)
html_list = infogetter.createHTMLList(driver)
info_list = infogetter.getInformation(html_list)
jsonwriter.writeJSONFile(info_list)
time.sleep(10)
driver.close()


