import datetime, xlrd
from collections import OrderedDict
import simplejson as json
import os
 
# Open the workbook and select the first worksheet
wb = xlrd.open_workbook(os.path.join('data.xls'))
sh = wb.sheet_by_index(0)
 
# List to hold dictionaries
tag_list = []
backlog_list = []
 
# Iterate through each row in worksheet and fetch values into dict
rowsleft = sh.nrows - 1
row_values = sh.row_values(1)
rowsleft = rowsleft - 1
acceptable = ['', 'A', 'A-','B','B-','C','C-','D','E']
while(rowsleft):
    tag = OrderedDict()
    tagN= OrderedDict()
    tag['Empl Id'] = row_values[0]
    tag['Campus Id'] = row_values[1]
    tag['Name'] = row_values[2]
    tagN['Empl Id'] = row_values[0]
    tagN['Campus Id'] = row_values[1]
    tagN['Name'] = row_values[2]
    name = row_values[2]
    courses_list = []
    courses = OrderedDict()
    logs = OrderedDict()
    while(name == row_values[2] and rowsleft):
        desc = row_values[3]
        course_list = []
        log_list = []
        while (desc == row_values[3] and rowsleft):
            course = OrderedDict()
            course['Course Id'] = row_values[4]
            course['Subject'] = row_values[5]
            course['Catalog No'] = row_values[6].strip()
            course['Unit Taken'] = row_values[7]
            course['Course Grade'] = row_values[8]

            if row_values[8] in acceptable:
                course_list.append(course)
            else:
                log_list.append(course)
            row_values = sh.row_values(sh.nrows-rowsleft)
            rowsleft = rowsleft - 1
        courses[desc] = course_list
        if log_list:
            logs[desc] = log_list


    tag['Courses'] = courses
    tag_list.append(tag)
    tagN['Courses'] = logs
    if logs:
        backlog_list.append(tagN)
 
# Serialize the list of dicts to JSON
j = json.dumps(tag_list)
k = json.dumps(backlog_list)
 
# Write to file
with open('studentdatarf.json', 'w') as f:
    f.write(j)

with open('studentdatalog.json', 'w') as f:
    f.write(k)

# print(json.dumps(json.loads(j)[0], indent=4, sort_keys=True))