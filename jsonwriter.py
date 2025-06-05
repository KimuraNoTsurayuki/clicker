import json

def writeJSONFile(arr):
	json_object = json.dumps(arr,indent =4)
	with open("database.json","w",encoding="utf-8") as outfile:
		outfile.write(json_object)
	
