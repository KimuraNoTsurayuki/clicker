import json

def writeJSONFile(array):
	json_object = json.dumps(array,indent=4)
	with open("database.json","w",encoding="utf-8") as outfile:
		outfile.write(json_object)
