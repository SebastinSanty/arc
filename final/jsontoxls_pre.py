import xlwt
import simplejson as json
import os

with open(os.path.join('json',"coursedesc.json")) as json_file:
    print('hello')
    coursedesc_arr = json.load(json_file)

#Get the branch from the Campus ID given
def branch(s):
    btype = s[4:8]
    if (btype[2:4] == 'PS') or (btype[2:4] == 'TS'):
        return btype[0:2]
    if (btype[0] == 'A') and (btype[2] == 'B'):
        return (btype[2:4] + btype[0:2])
    else:
        return btype

def psts(s):
    btype = s[4:8]
    if (btype[2:4] == 'TS'):
        return True
    else:
        return False

#Check for Reverse Dual/ BE Dual Cases
def specialcase(s):
    btype = s[4:8]
    if btype[2:3] == 'B':
        return True


#Get the course type by comparing it with the branch, like whether it is an elective/CDC
def getcoursetype(compcode, cid, branch):
    if (compcode == '21024') or (compcode == '21023'):
        return 'Other'
    if (compcode == '21591') and (psts(cid)):
        return 'OPEN'
    try:
        coursedesc_arr[compcode]
    except:
        return 'OPEN'
    branch1 = branch[0:2]
    tag1 = list(filter(lambda x: branch1 in x, coursedesc_arr[compcode]['Tag']))
    branch2 = ''
    tag2 = []
    if len(branch) == 4:
        branch2 = branch[2:4]
        # print(branch2)
        tag2 = list(filter(lambda x: branch2 in x, coursedesc_arr[compcode]['Tag']))
        # print(tag2)
    tag3 = list(filter(lambda x: 'HUM' in x, coursedesc_arr[compcode]['Tag']))
    # print(tag1)
    if not tag1 and not tag2 and not tag3:
        return 'OPEN'
    elif tag3:
        return 'HUM'
    elif tag1 and tag1[0][2:4] == 'EL':
        return 'DEL1'
    elif tag2 and tag2[0][2:4] == 'EL':
        return 'DEL2'
    elif tag1:
        if ('CDC' in z for z in tag1[0]):
            return 'CDC'
    elif tag2:
         if ('CDC' in y for y in tag2[0]):
            return 'CDC'
    else:
        return 'OPEN'




sheetno = 1

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Sheet " + str(sheetno))
sheet.write(0, 0, 'Empl Id')
sheet.write(0, 1, 'Campus Id')
sheet.write(0, 2, 'Name')
sheet.write(0, 3, 'Description')
sheet.write(0, 4, 'Course Id')
sheet.write(0, 5, 'Subject')
sheet.write(0, 6, 'Catalog No')
sheet.write(0, 7, 'Unit Taken')
sheet.write(0, 8, 'Course Grade')
sheet.write(0, 9, 'Tag')

with open(os.path.join('json',"studentdata_simple.json")) as json_file:
    json_data = json.load(json_file)

u = json_data
c = 0
emplid = ''
for i in u:
    c = c + 1
    sheet.write(c, 0, i['Empl Id'])
    sheet.write(c, 1, i['Campus Id'])
    sheet.write(c, 2, i['Name'])
    sheet.write(c, 3, i['Description'])
    sheet.write(c, 4, i['Course Id'])
    sheet.write(c, 5, i['Subject'])
    sheet.write(c, 6, i['Catalog No'].split())
    sheet.write(c, 7, i['Unit Taken'])
    sheet.write(c, 8, i['Course Grade'])
    compcode = str(i['Course Id'])
    print(compcode)
    coursetype = getcoursetype(compcode, i['Campus Id'], branch(i['Campus Id']))

    sheet.write(c, 9, coursetype)
    if c>=65535:
        c=0
        print("New sheet")
        sheetno = sheetno + 1
        sheet.col(0).width = 256 * 15
        sheet.col(1).width = 256 * 15
        sheet.col(2).width = 256 * 40
        sheet.col(3).width = 256 * 5
        sheet.col(4).width = 256 * 6
        sheet.col(5).width = 256 * 10
        sheet.col(6).width = 256 * 7
        sheet.col(7).width = 256 * 5
        sheet.col(8).width = 256 * 5
        sheet = workbook.add_sheet("Sheet " + str(sheetno))
        sheet.write(0, 0, 'Empl Id')
        sheet.write(0, 1, 'Campus Id')
        sheet.write(0, 2, 'Name')
        sheet.write(0, 3, 'Description')
        sheet.write(0, 4, 'Course Id')
        sheet.write(0, 5, 'Subject')
        sheet.write(0, 6, 'Catalog No')
        sheet.write(0, 7, 'Unit Taken')
        sheet.write(0, 8, 'Course Grade')
        sheet.write(0, 9, 'Tag')

sheet.col(0).width = 256 * 15
sheet.col(1).width = 256 * 15
sheet.col(2).width = 256 * 40
sheet.col(3).width = 256 * 5
sheet.col(4).width = 256 * 6
sheet.col(5).width = 256 * 10
sheet.col(6).width = 256 * 7
sheet.col(7).width = 256 * 5
sheet.col(8).width = 256 * 5

workbook.save(os.path.join('result',"final_tag.xls"))