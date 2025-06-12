import json

filename = str()

def setName(type_purchase,place, filter_strength,lower_price, upper_price, lower_area, upper_area):
	global filename 
	filename = "database_" + type_purchase + "_" + place + "_" + str(filter_strength) + "_"+ str(lower_price) + "_" + str(upper_price) + "_" + str(lower_area) + "_" + str(upper_area) + ".json"

def writeJSONFile(arr):
	json_object = json.dumps(arr,indent =4)
	with open(filename,"w",encoding="utf-8") as outfile:
		outfile.write(json_object)
