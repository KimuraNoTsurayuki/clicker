url = "url"
address = "address"
area = "area (m^2)"
price = "price($)"
bedrooms = "bedrooms"
floor = "floor"

def listToValidHTML(ls):
	res = str()
	res += "<!DOCTYPE html>" + "\n"
	res += "<html lang = \"en\">" + "\n"
	res += "<head>" + "\n"
	res += "<title>" + "\n"
	res += "placeholder" + "\n"
	res += "</title>" + "\n"
	res += "<style>" + "\n"
	res += "img{\n \t width:150px; \n \theight:150px; \n}\n"
	res += addContainerSettings()
	res += ".text{\n \t font-family: \"Arial\";\n}\n"
	res += addContainerOverlay()
	res += addContainerHover()
	res += "</style>" + "\n"
	res += "</head>" + "\n"
	res += "<body>" + "\n"
	res += listToDivs(ls)
	res += "</body>" + "\n"
	res += "</html>"
	return res
	
def listToDivs(ls):
	res = str()
	for dc in ls:
		res += "<div class = \"container\"> \n"
		res += dictTool(dc) + "\n"
		res += "</div> \n"
	return res

def valuesToli(dc):
	res = str()
	res += "\t <div class = \"text\">" "\n"
	res += "\t <ol> \n"
	res += '\t' + '\t' + urlToli(dc) + "\n"
	res += '\t' + '\t' + addressToli(dc) + "\n"
	res += '\t' + '\t' + priceToli(dc) + "\n"
	res += '\t' + '\t' + areaToli(dc) + "\n"
	res += '\t' + '\t' + bedroomsToli(dc) + "\n"
	res += '\t' + '\t' + floorToli(dc) + "\n"
	res += "\t </ol> \n"
	res += "\t </div>"
	return res

def dictTool(dc):
	res = str()
	res += "\t <div class = \"images\">" +"\n"
	for i in range(0,len(dc) - 7):
		img_url = dc[f"Img{i+1}"]
		a = '\t' + '\t' + f"<img src=\"{img_url}\" alt = \"placeholder\">" + "\n"
		res += a
	res += "<button class=\"overlay\">Click Me!</button>" + "\n"
	res += "\t </div> \n"
	res += valuesToli(dc)
	return res
	

def addressToli(dc):
	res = "<li> "
	res += address + ": " + dc[address]
	res += " </li>"
	return res	

def urlToli(dc):
	res = "<li> "
	res += url + ": " + dc[url]
	res += " </li>"
	return res
	
def areaToli(dc):
	res = "<li> "
	res += area + ": " + dc[area]
	res += " </li>"
	return res
	
def priceToli(dc):
	res = "<li> "
	res += price + ": " + dc[price]
	res += " </li>"
	return res
	
def bedroomsToli(dc):
	res = "<li> "
	res += bedrooms + ": " + dc[bedrooms]
	res += " </li>"
	return res

def floorToli(dc):
	res = "<li> "
	res += floor + ": " + dc[floor]
	res += " </li>"
	return res
	
def addContainerOverlay():
	return ".overlay {\n \tposition: relative;\n \ttop: 0;\n\tbottom: 0;\n\tleft: 0;\n\tright: 0;\n\topacity: 0; \n\ttransition: .5s ease;\n\tbackground-color: #008CBA;\n}\n"
	
def addContainerHover():
	return ":hover .overlay {\n \t opacity: 1;\n}\n"

def addContainerSettings():
	return ".container{\n \tborder: 2px;\n \t border-style: solid;\n\t border-radius: 3px;\n \tdisplay: flex; \n \t align-items: left;\n \t justify-content: left;\n}\n"
