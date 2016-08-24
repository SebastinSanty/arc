import datetime, xlrd
from collections import OrderedDict
import simplejson as json
import os
 
# Open the workbook and select the first worksheet
wb = xlrd.open_workbook(os.path.join('data.xls'))
sh = wb.sheet_by_index(0)
 
# List to hold dictionaries
tag_list = []
name = ''
# Iterate through each row in worksheet and fetch values into dict
for rownum in range(2, sh.nrows):
    row_values = sh.row_values(rownum)
    if (name = row_values[1]):
        course = OrderedDict()
        tag[row_values[3]]['courses'] =  
    else:
        tag = OrderedDict()
        tag['Campus Id'] = row_values[2]
        tag['Empl Id'] = int(row_values[0])
        tag['Name'] = row_values[1]
    

    name = row_values[2]


    
    tag['courseid'] = int(row_values[4])
    tag['subject'] = row_values[5]
    tag['catalogno'] = row_values[6]
    tag['unittaken'] = row_values[7]
    tag['coursegrade'] = row_values[8]
 
    tag_list.append(tag)
 
# Serialize the list of dicts to JSON
j = json.dumps(tag_list)
 
# Write to file
with open('data.json', 'w') as f:
    f.write(j)

print(json.dumps(json.loads(j)[0], indent=4, sort_keys=True))