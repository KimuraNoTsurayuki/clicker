import sys
import infogetter as info
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QTextEdit, QPlainTextEdit,QPushButton,QGridLayout

building_type_to_send = str()
building_location_to_send = str()
area_to_send_lower = 0
area_to_send_upper = 0
price_to_send_lower = 0
price_to_send_upper = 0

class BasicGUI(QWidget):
	def __init__(self):
		super().__init__()

		self.layout = QGridLayout()


		self.minsurf = QLineEdit()
		self.maxsurf = QLineEdit()
		self.minamount = QLineEdit()
		self.maxamount = QLineEdit()

		self.enter_button = QPushButton("Enter")
		self.vake_button = QPushButton("Vake")
		self.saburtalo_button = QPushButton("Saburtalo")	
		self.new_building_button = QPushButton("New Building")
		self.old_building_button = QPushButton("Old Building")
		self.being_constructed = QPushButton("In Construction")
	
	
		self.minsurf.setPlaceholderText("Minimum Surface Area")
		self.maxsurf.setPlaceholderText("Maximum Surface Area")
		self.minamount.setPlaceholderText("Price Minimum")
		self.maxamount.setPlaceholderText("Price Maximum")	
		
		self.vake_button.clicked.connect(self.setVake)
		self.saburtalo_button.clicked.connect(self.setSaburtalo)
		self.new_building_button.clicked.connect(self.setNewBuilding)
		self.old_building_button.clicked.connect(self.setOldBuilding)
		self.being_constructed.clicked.connect(self.setInConstruction)
		self.enter_button.clicked.connect(self.setNumericalValues)
		
		
		self.layout.addWidget(self.minsurf)
		self.layout.addWidget(self.maxsurf)
		self.layout.addWidget(self.minamount)
		self.layout.addWidget(self.maxamount)
		self.layout.addWidget(self.vake_button)
		self.layout.addWidget(self.saburtalo_button)
		self.layout.addWidget(self.new_building_button)
		self.layout.addWidget(self.old_building_button)
		self.layout.addWidget(self.being_constructed)
		self.layout.addWidget(self.enter_button)
	

		self.setLayout(self.layout)
		self.setWindowTitle(QApplication.translate("toplevel","AIC"))
		
	def setVake(self):
		global building_location_to_send
		building_location_to_send = "1"
	
	def setSaburtalo(self):
		global building_location_to_send
		building_location_to_send = "2"

	def setNumericalValues(self):
		area_to_send_lower = self.setLowerAreaBound()
		area_to_send_upper = self.setUpperAreaBound()
		price_to_send_lower = self.setLowerPriceBound()
		price_to_send_upper = self.setUpperPriceBound()
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
