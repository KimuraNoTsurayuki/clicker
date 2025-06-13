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
	res += "</head>" + "\n"
	res += "<body>" + "\n"
	res += listToDivs(ls)
	res += "</body>" + "\n"
	res += "</html>"
	return res
	
def listToDivs(ls):
	res = str()
	for dc in ls:
		res += "<div> \n \t"
		res += dictTool(dc) + "\n"
		res += "</div> \n"
	return res

def valuesToli(dc):
	res = str()
	res += '\t' + '\t' + urlToli(dc) + "\n"
	res += '\t' + '\t' + addressToli(dc) + "\n"
	res += '\t' + '\t' + priceToli(dc) + "\n"
	res += '\t' + '\t' + areaToli(dc) + "\n"
	res += '\t' + '\t' + bedroomsToli(dc) + "\n"
	res += '\t' + '\t' + floorToli(dc) + "\n"
	return res

def dictTool(dc):
	res = str()
	for i in range(0,3):
		img_url = dc[f"Img{i+1}"]
		a = '\t' + '\t' + f"<img src=\"{img_url}\" alt = \"placeholder\"　style = \"width:200px;length:200px\">" + "\n"	
		print(a)
		res += a
	res = "<ol> \n"
	res += valuesToli(dc)
	res += " \t </ol>"
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
