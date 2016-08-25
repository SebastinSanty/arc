import datetime, xlrd
from collections import OrderedDict
import simplejson as json
import os
 
# Open the workbook and select the first worksheet
wb = xlrd.open_workbook(os.path.join('data.xls'))
sh = wb.sheet_by_index(0)
 
# List to hold dictionaries
tag_list = []
 
# Iterate through each row in worksheet and fetch values into dict
rowsleft = sh.nrows - 1
row_values = sh.row_values(1)
rowsleft = rowsleft - 1
while(rowsleft):
    tag = OrderedDict()
    tag['Empl Id'] = row_values[0]
    tag['Campus Id'] = row_values[1]
    tag['Name'] = row_values[2]
    name = row_values[2]
    while(name == row_values[2] and rowsleft):
        desc = row_values[3]
        course_list = []
        while (desc == row_values[3] and rowsleft):
            course = OrderedDict()
            course['Course Id'] = row_values[4]
            course['Subject'] = row_values[5]
            course['Catalog No'] = row_values[6]
            course['Unit Taken'] = row_values[7]
            course['Course Grade'] = row_values[8]
            course_list.append(course)
            row_values = sh.row_values(sh.nrows-rowsleft)
            rowsleft = rowsleft - 1
            print(desc, row_values[6], name)
        tag[str(desc)] = course_list

    tag_list.append(tag)
 
# Serialize the list of dicts to JSON
j = json.dumps(tag_list)
 
# Write to file
with open('studentdatarf.json', 'w') as f:
    f.write(j)

print(json.dumps(json.loads(j)[0], indent=4, sort_keys=True))