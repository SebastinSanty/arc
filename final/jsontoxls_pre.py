import xlwt
import simplejson as json
import os
from logic import branch, psts, getcoursetype, proj

with open(os.path.join('json',"coursedesc.json")) as json_file:
    coursedesc_arr = json.load(json_file)

with open(os.path.join('json',"noofcourse.json")) as json_file:
    noofcourse = json.load(json_file)

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
    coursecode = i['Subject'] + " " + ''.join(i['Catalog No'].split())
    coursetype = getcoursetype(coursecode, i['Campus Id'], branch(i['Campus Id']))
    if (emplid != i['Empl Id']):
        for j in noofcourse:
            if (j['Discipline'] == branch(i['Campus Id'])):
                CDC_REQ = j['No of Courses']['CDC']
                DEL1_REQ = j['No of Courses']['DEL1']
                DEL2_REQ = j['No of Courses']['DEL2']
                HUM_REQ = j['No of Courses']['HUM']
                OPEN_REQ = j['No of Courses']['OPEN']
                break
        CDC_LEFT = CDC_REQ
        DEL1_LEFT = DEL1_REQ
        DEL2_LEFT = DEL2_REQ
        HUM_LEFT = HUM_REQ
        OPEN_LEFT = OPEN_REQ
        print(CDC_REQ)
    FINAL = 'Not parse'
    emplid = i['Empl Id']
    if coursetype == 'CDC':
        CDC_LEFT = CDC_LEFT - 1
    elif (coursetype == 'HUM' and HUM_LEFT <=0) or (coursetype == 'DEL1' and DEL1_LEFT<=0) or (coursetype == 'DEL2' and DEL2_LEFT<=0 and DEL2_REQ!=0) or (coursetype == 'OPEN'):
        OPEN_LEFT = OPEN_LEFT - 1
    elif coursetype == 'DEL1':
        DEL1_LEFT = DEL1_LEFT - 1
    elif coursetype == 'DEL2':
        DEL2_LEFT = DEL2_LEFT - 1
    elif coursetype == 'HUM':
        HUM_LEFT = HUM_LEFT - 1
    try:
        tag[coursetype].append(coursecode)
    except:
        tag[coursetype] = [coursecode]
    
    #Extra Flags as mentioned by ARC
    if proj(coursecode):
        try:
            PROJ_LIST[coursecode] = PROJ_LIST[coursecode] + 1
        except:
            PROJ_LIST[coursecode] = 1
    
    if (ELEC_FLAG==0) and ((coursetype == 'HUM') or (coursetype == 'DEL1') or (coursetype == 'DEL2')) and coursedesc_arr[coursecode]['Units'] < 3:
        ELEC_FLAG = 1

    if ((coursecode == 'MGTS F211') or (coursecode == 'ECON F211')) and branch(i['Campus Id'])[0:2]!='B3':
        if POMPOE == 1:
            OPEN_LEFT = OPEN_LEFT - 1
        else:
            POMPOE = 1

    # print(coursecode)
    sheet.write(c, 9, FINAL)
    if c>=65535:
        c=0
        print("New sheet")
        sheetno = sheetno + 1
        sheet.col(0).width = 256 * 15
        sheet.col(1).width = 256 * 15
        sheet.col(2).width = 256 * 35
        sheet.col(3).width = 256 * 25
        sheet.col(4).width = 256 * 6
        sheet.col(5).width = 256 * 5
        sheet.col(6).width = 256 * 6
        sheet.col(7).width = 256 * 3
        sheet.col(8).width = 256 * 3
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
sheet.col(2).width = 256 * 35
sheet.col(3).width = 256 * 25
sheet.col(4).width = 256 * 6
sheet.col(5).width = 256 * 5
sheet.col(6).width = 256 * 6
sheet.col(7).width = 256 * 3
sheet.col(8).width = 256 * 3

workbook.save(os.path.join('result',"final_tag.xls"))