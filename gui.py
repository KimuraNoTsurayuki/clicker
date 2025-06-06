import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QTextEdit, QPlainTextEdit,QPushButton,QGridLayout

def startGUI():
	app = QApplication(sys.argv)
	window = QWidget()
	window.resize(500,500)
	layout = QGridLayout()


	minsurf = QLineEdit()
	maxsurf = QLineEdit()
	minamount = QLineEdit()
	maxamount = QLineEdit()

	enter_button = QPushButton("Enter")
	vake_button = QPushButton("Vake")
	saburtalo_button = QPushButton("Saburtalo")	
	new_building_button = QPushButton("New Building")
	old_building_button = QPushButton("Old Building")

	minsurf.setPlaceholderText("Minimum Surface Area")
	maxsurf.setPlaceholderText("Maximum Surface Area")
	minamount.setPlaceholderText("Price Minimum")
	maxamount.setPlaceholderText("Price Maximum")	

	layout.addWidget(minsurf)
	layout.addWidget(maxsurf)
	layout.addWidget(minamount)
	layout.addWidget(maxamount)
	layout.addWidget(vake_button)
	layout.addWidget(saburtalo_button)
	layout.addWidget(new_building_button)
	layout.addWidget(old_building_button)
	layout.addWidget(enter_button)


	window.setLayout(layout)
	window.setWindowTitle(QApplication.translate("toplevel","AIC"))
	window.show()
	app.exec()
