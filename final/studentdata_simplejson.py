import datetime, xlrd
from collections import OrderedDict
import simplejson as json
import os
import sys

filename = sys.argv[1]
 
# Open the workbook and select the first worksheet
wb = xlrd.open_workbook(os.path.join(filename))
sh = wb.sheet_by_index(0)
 
# List to hold dictionaries
tag_list = []
 
# Iterate through each row in worksheet and fetch values into dict
for rownum in range(2, sh.nrows):
    tag = OrderedDict()
    row_values = sh.row_values(rownum)
    tag['Empl Id'] = int(row_values[0])
    tag['Campus Id'] = row_values[1]
    tag['Name'] = row_values[2]
    tag['Description'] = row_values[3]
    tag['Course Id'] = int(row_values[4])
    tag['Subject'] = row_values[5]
    tag['Catalog No'] = row_values[6]
    tag['Unit Taken'] = row_values[7]
    tag['Course Grade'] = row_values[8]
 
    tag_list.append(tag)
 
# Serialize the list of dicts to JSON
j = json.dumps(tag_list)
 
# Write to file
with open(os.path.join('json', 'studentdata_simple.json'), 'w') as f:
    f.write(j)
