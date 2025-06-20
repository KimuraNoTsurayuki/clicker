import sys
import infogetter as info
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QTextEdit, QPlainTextEdit,QPushButton,QGridLayout,QHBoxLayout

building_type_to_send = str()
building_location_to_send = str()
purchase_type = str()
search_text = str()
area_to_send_lower = 0
area_to_send_upper = 0
price_to_send_lower = 0
price_to_send_upper = 0
filter_strength = 0

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
		self.filterstrength = QLineEdit()
		self.textsearch = QLineEdit()

		self.enter_button = QPushButton("Enter")
		self.vake_button = QPushButton("Vake")
		self.saburtalo_button = QPushButton("Saburtalo")	
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
		self.filterstrength.setPlaceholderText("Set Filter Strength. Lower number filters more. 2<= str <= 7")	
		
		self.vake_button.clicked.connect(self.setVake)
		self.saburtalo_button.clicked.connect(self.setSaburtalo)
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
		self.layout.addWidget(self.textsearch)
		self.layout.addWidget(self.filterstrength)
		self.layout2.addWidget(self.vake_button)
		self.layout2.addWidget(self.saburtalo_button)
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
		self.setWindowTitle(QApplication.translate("toplevel","AIC"))
		
	def setVake(self):
		global building_location_to_send
		building_location_to_send = "2"
	
	def setSaburtalo(self):
		global building_location_to_send
		building_location_to_send = "1"

	def setNumericalValues(self):
		self.setLowerAreaBound()
		self.setUpperAreaBound()
		self.setLowerPriceBound()
		self.setUpperPriceBound()
		self.setTextSearch()
		self.setFilterStrength()
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
		
