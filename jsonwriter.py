import json

filename = str()

def setName(date, type_purchase, place, building_age ,filter_strength, lower_price, upper_price, lower_area, upper_area, disc = str()):
	global filename 
	filename = f"database_{date}_"
	match type_purchase:
		case "1":
			filename += "sale_"
		case "2":
			filename += "rent_"
	match place:
		case "1":
			filename += "Saburtalo_"
		case "2":
			filename += "Vake_"
		case "3":
			filename += "Vake-Saburtalo_"
		case "4":
			filename += "Isani-Samgori_"
		case "5":
			filename += "Gldani-Nadzaladevi_"
		case "6":
			filename += "Didube-Chugureti_"
		case "7":
			filename += "Old-Tbilisi_"
		case "8":
			filename += "Dighomi_"
		case "9":
			filename += "Lisi_"
		case "10":
			filename += "Batumi-All_"
		case "11":
			filename += "Old-Batumi_"
		case "12":
			filename += "Makhinjauri_"
		case "13":
			filename += "Boni-Gorodoki_"
		case "14":
			filename += "Rustaveli-Batumi_"
		case "15":
			filename += "Khimshiashvili"
	match building_age:
		case "1":
			filename += "New_"
		case "2": 
			filename += "Old_"
		case "3":
			filename += "Construction_"
	filename += str(filter_strength) + "_"+ str(lower_price) + "_" + str(upper_price) + "_" + str(lower_area) + "_" + str(upper_area) + "_" + disc + ".json"

def writeJSONFile(arr):
	json_object = json.dumps(arr,indent =4)
	with open(filename,"w",encoding="utf-8") as outfile:
		outfile.write(json_object)
