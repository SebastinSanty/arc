import xlwt
import simplejson as json

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Filtered")
sheet.write(0, 0, 'Empl Id')
sheet.write(0, 1, 'Campus Id')
sheet.write(0, 2, 'Name')
sheet.write(0, 3, 'Description')
sheet.write(0, 4, 'Course ID')
sheet.write(0, 5, 'Subject')
sheet.write(0, 6, 'Catalog No')
sheet.write(0, 7, 'Unit Taken')
sheet.write(0, 8, 'Course Grade')

acceptable = ['', 'A', 'A-','B','B-','C','C-','D','E']

with open("data.json") as json_file:
	json_data = json.load(json_file)
u = json_data
c = 0
for i in u:
	if (i['Course Grade'] in acceptable):
		c = c + 1
		sheet.write(c, 0, i['Empl Id'])
		sheet.write(c, 1, i['Campus Id'])
		sheet.write(c, 2, i['Name'])
		sheet.write(c, 3, i['Description'])
		sheet.write(c, 4, i['Course Id'])
		sheet.write(c, 5, i['Subject'])
		sheet.write(c, 6, i['Catalog No'])
		sheet.write(c, 7, i['Unit Taken'])
		sheet.write(c, 8, i['Course Grade'])

sheet.col(0).width = 256 * 10
sheet.col(1).width = 256 * 20
sheet.col(2).width = 256 * 30
sheet.col(2).width = 256 * 20
workbook.save("filtered.xls")