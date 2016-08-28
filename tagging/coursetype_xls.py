import datetime, xlrd
from collections import OrderedDict
import simplejson as json
import os
 
# Open the workbook and select the first worksheet
wb = xlrd.open_workbook(os.path.join('data.xls'))
sh = wb.sheet_by_index(0)


with open("coursedesc_arr.json") as json_file:
    coursedesc_arr = json.load(json_file)

def getcoursetype(coursecode, branch):
    if (coursecode == 'MGTS F211') or (coursecode == 'ECON F211'):
        return 'Other'
    try:
        coursedesc_arr[coursecode]
    except:
        return 'OPEN'
    branch1 = branch[0:2]
    tag1 = list(filter(lambda x: branch1 in x, coursedesc_arr[coursecode]['Tag']))
    branch2 = ''
    tag2 = []
    if len(branch) == 4:
        branch2 = branch[2:4]
        tag2 = list(filter(lambda x: branch2 in x, coursedesc_arr[coursedesc_arr]['Tag']))
    tag3 = list(filter(lambda x: 'HUM' in x, coursedesc_arr[coursecode]['Tag']))
    if not tag1 and not tag2 and not tag3:
        return 'OPEN'
    elif tag3:
        return 'HUM'
    elif tag1 and tag1[0][2:4] == 'EL':
        return 'DEL1'
    elif tag2 and tag2[0][2:4] == 'EL':
        return 'DEL2'
    elif ('CDC' in z for z in tag1[0]) or ('CDC' in y for y in tag2[0]):
        return 'CDC'
    else:
        return 'OPEN'

def branch(s):
    btype = s[4:8]
    if btype[2:4] == 'PS':
        return btype[0:2]
    else:
        return btype
 
# List to hold dictionaries
tag_list = []
 
# Iterate through each row in worksheet and fetch values into dict
for rownum in range(1, sh.nrows):
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
    tag['Type'] = getcoursetype(row_values[5] + " " + row_values[6], branch(row_values[1]))
    tag_list.append(tag)
 
# Serialize the list of dicts to JSON
j = json.dumps(tag_list)
 
# Write to file
with open('studentdata_course.json', 'w') as f:
    f.write(j)

print(json.dumps(json.loads(j)[0], indent=4, sort_keys=True))