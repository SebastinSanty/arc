import simplejson as json

with open("studentdata.json") as json_file:
	studentdata = json.load(json_file)

with open("coursetype.json") as json_file:
	coursetype = json.load(json_file)

with open("noofcourse.json") as json_file:
	noofcourse = json.load(json_file)

