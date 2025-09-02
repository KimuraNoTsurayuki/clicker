import sys
import infogetter as info
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QTextEdit, QPlainTextEdit,QPushButton,QGridLayout,QHBoxLayout,QComboBox

building_type_to_send = str()
building_location_to_send = str()
purchase_type = str()
search_text = str()
area_to_send_lower = 0
area_to_send_upper = 0
price_to_send_lower = 0
price_to_send_upper = 0
filter_strength = 0
rooms = 0
bedrooms_min = 0
bedrooms_max = 0

class BasicGUI(QWidget):
	def __init__(self):
		super().__init__()

		self.layout = QVBoxLayout()
		self.layout2 = QHBoxLayout()
		self.layout3 = QHBoxLayout()
		self.layout4 = QHBoxLayout()
		self.layout5 = QHBoxLayout()


		self.minsurf = QLineEdit()
		self.maxsurf = QLineEdit()
		self.minamount = QLineEdit()
		self.maxamount = QLineEdit()
		self.amountrooms = QLineEdit()
		self.minamountbedrooms = QLineEdit()
		self.maxamountbedrooms = QLineEdit()
		self.filterstrength = QLineEdit()
		self.textsearch = QLineEdit()
		self.locations = QComboBox()
		
		self.locations.addItem("Vake Only")
		self.locations.addItem("Saburtalo Only")
		self.locations.addItem("Both Vake and Saburtalo")
		self.locations.addItem("Isani-Samgori")
		self.locations.addItem("Gldani-Nadzaladevi")
		self.locations.addItem("Didube-Chugureti")
		self.locations.addItem("Old Tbilisi")
		
		


		self.enter_button = QPushButton("Enter")
		self.new_building_button = QPushButton("New Building")
		self.old_building_button = QPushButton("Old Building")
		self.being_constructed = QPushButton("In Construction")
		self.for_sale = QPushButton("For Sale")
		self.for_rent = QPushButton("For Rent")
	
	
		self.minsurf.setPlaceholderText("Minimum Surface Area")
		self.maxsurf.setPlaceholderText("Maximum Surface Area")
		self.minamount.setPlaceholderText("Price Minimum")
		self.maxamount.setPlaceholderText("Price Maximum")
		self.textsearch.setPlaceholderText("Enter text for search")
		self.filterstrength.setPlaceholderText("Set Filter Strength. Lower number filters more. 2 <= str <= 7")	
		self.amountrooms.setPlaceholderText("Amount Of Rooms")
		self.minamountbedrooms.setPlaceholderText("Minimum bedroom count")
		self.maxamountbedrooms.setPlaceholderText("Maximum bedroom count")
		
		

		self.new_building_button.clicked.connect(self.setNewBuilding)
		self.old_building_button.clicked.connect(self.setOldBuilding)
		self.being_constructed.clicked.connect(self.setInConstruction)
		self.for_sale.clicked.connect(self.setForSale)
		self.for_rent.clicked.connect(self.setForRent)
		self.enter_button.clicked.connect(self.setNumericalValues)
		
		
		self.layout.addWidget(self.minsurf)
		self.layout.addWidget(self.maxsurf)
		self.layout.addWidget(self.minamount)
		self.layout.addWidget(self.maxamount)
		self.layout.addWidget(self.amountrooms)
		self.layout.addWidget(self.minamountbedrooms)
		self.layout.addWidget(self.maxamountbedrooms)
		self.layout.addWidget(self.textsearch)
		self.layout.addWidget(self.filterstrength)
		self.layout.addWidget(self.locations)
		self.layout3.addWidget(self.new_building_button)
		self.layout3.addWidget(self.old_building_button)
		self.layout3.addWidget(self.being_constructed)
		self.layout4.addWidget(self.for_sale)	
		self.layout4.addWidget(self.for_rent)
		self.layout5.addWidget(self.enter_button)
	
		self.layout.addLayout(self.layout2)
		self.layout.addLayout(self.layout3)
		self.layout.addLayout(self.layout4)
		self.layout.addLayout(self.layout5)
		self.setLayout(self.layout)
		self.setWindowTitle(QApplication.translate("toplevel","Clicker"))
		

	def getComboTextPlaces(self):
		global building_location_to_send
		text = self.locations.currentText()
		match text:
			case "Saburtalo Only":
				building_location_to_send = "1"
			case "Vake Only":
				building_location_to_send = "2"
			case "Both Vake and Saburtalo":
				building_location_to_send = "3"
			case "Isani-Samgori":
				building_location_to_send = "4"
			case "Gldani-Nadzaladevi":
				building_location_to_send = "5"
			case "Didube-Chugureti":
				building_location_to_send = "6"
			case "Old Tbilisi":
				building_location_to_send = "7"
		
	def setNumericalValues(self):
		self.setLowerAreaBound()
		self.setUpperAreaBound()
		self.setLowerPriceBound()
		self.setUpperPriceBound()
		self.setTextSearch()
		self.setFilterStrength()
		self.getComboTextPlaces()
		self.setRoomAmount()
		self.setMinBedroomAmount()
		self.setMaxBedroomAmount()
		QApplication.quit()		
		
	def setNewBuilding(self):
		global building_type_to_send 
		building_type_to_send =  "1"
	
	def setOldBuilding(self):
		global building_type_to_send 
		building_type_to_send = "2"

	def setInConstruction(self):
		global building_type_to_send
		building_type_to_send = "3"
		
	def setForSale(self):
		global purchase_type
		purchase_type = "1"

	def setForRent(self):
		global purchase_type
		purchase_type = "2"	
	
	def setLowerAreaBound(self):
		global area_to_send_lower
		area_to_send_lower = int(self.minsurf.text())

	def setUpperAreaBound(self):
		global area_to_send_upper
		area_to_send_upper =  int(self.maxsurf.text())
	
	def setLowerPriceBound(self):
		global price_to_send_lower
		price_to_send_lower = int(self.minamount.text())

	def setUpperPriceBound(self):
		global price_to_send_upper
		price_to_send_upper = int(self.maxamount.text())
	
	def setFilterStrength(self):
		global filter_strength
		filter_strength = int(self.filterstrength.text())
		
	def setTextSearch(self):
		global search_text
		search_text = self.textsearch.text()	
	def setRoomAmount(self):
		global rooms
		rooms = int(self.amountrooms.text())
	def setMinBedroomAmount(self):
		global bedrooms_min
		bedrooms_min = int(self.minamountbedrooms.text())
	def setMaxBedroomAmount(self):
		global bedrooms_max
		bedrooms_max = int(self.maxamountbedrooms.text())	
