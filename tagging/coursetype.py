import datetime, xlrd
from collections import OrderedDict
import simplejson as json
import os
 
# Open the workbook and select the first worksheet
wb = xlrd.open_workbook(os.path.join('coursedesc.xlsx'))
sh = wb.sheet_by_index(0)
 
# List to hold dictionaries
tag_list = []

def RepresentsInt(s):
    try: 
        int(s)
        return int(s)
    except ValueError:
        return 0


def RepresentsBool(s):
    try: 
        a = True if s == 1 else False
        return a
    except ValueError:
        return True


# Iterate through each row in worksheet and fetch values into dict
for rownum in range(2, sh.nrows):
    tag = OrderedDict()
    row_values = sh.row_values(rownum)
    tag['Comp Codes'] = RepresentsInt(row_values[0])
    tag['Course Code'] = row_values[1]
    tag['Tag'] = row_values[2]
    tag['Course Name'] = row_values[3]
    tag['Project'] = RepresentsBool(row_values[4])
    tag['Units'] = RepresentsInt(row_values[5])

 
    tag_list.append(tag)
 
# Serialize the list of dicts to JSON
j = json.dumps(tag_list)
 
# Write to file
with open('coursedesc.json', 'w') as f:
    f.write(j)

print(json.dumps(json.loads(j)[0], indent=4, sort_keys=True))