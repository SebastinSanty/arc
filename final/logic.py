import simplejson as json
from collections import OrderedDict
import os
import sys

#Getting the argument from the commandline
arg = sys.argv[1]

#Open the JSON file containing description of courses arranged
with open(os.path.join('json',"coursedesc.json")) as json_file:
	coursedesc_arr = json.load(json_file)

#Open the JSON file containing number of courses in a particular discipline
with open(os.path.join('json',"noofcourse.json")) as json_file:
	noofcourse = json.load(json_file)

#Open the JSON file containing the student data
with open(os.path.join('json','studentdatarf.json')) as json_file:
	studentdatarf = json.load(json_file)

#Get the branch from the Campus ID given
def branch(s):
	btype = s[4:8]
	if (btype[2:4] == 'PS') or (btype[2:4] == 'TS'):
		return btype[0:2]
	if (btype[0] == 'A') and (btype[2] == 'B'):
		print(btype[0], btype[2])
		return (btype[2:4] + btype[0:2])
	else:
		return btype

#Check for Reverse Dual/ BE Dual Cases
def specialcase(s):
	btype = s[4:8]
	if btype[2:3] == 'B':
		return True


#Get the course type by comparing it with the branch, like whether it is an elective/CDC
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
		# print(branch2)
		tag2 = list(filter(lambda x: branch2 in x, coursedesc_arr[coursecode]['Tag']))
		# print(tag2)
	tag3 = list(filter(lambda x: 'HUM' in x, coursedesc_arr[coursecode]['Tag']))
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

#Get whether the particular subject is a project or not
def proj(coursecode):
	try:
		coursedesc_arr[coursecode]
	except:
		return False
	return coursedesc_arr[coursecode]['Project']

tag_list = []

for i in studentdatarf:
	tag = OrderedDict()
	tag['Empl Id'] = i['Empl Id']
	tag['Campus Id'] = i['Campus Id']
	tag['Name'] = i['Name']
	PROJ_LEFT = 5
	PROJ_LIST = {}
	PROJ_FLAG = 0
	ELEC_FLAG = 0
	POMPOE = 0
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
	for key, value in i['Courses'].items():
		for k in range(len(value)):
			coursecode = str(i['Courses'][key][k]['Subject']) + " " + str(i['Courses'][key][k]['Catalog No'])
			coursetype = getcoursetype(coursecode, branch(i['Campus Id']))
			if coursecode not in tag[coursetype]:
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

	for key,value in PROJ_LIST.items():
		if PROJ_LEFT > 0 and PROJ_FLAG != 1:
			PROJ_LEFT -= value
		
		if (PROJ_LEFT <= 0) or (value >= 3):
			PROJ_FLAG = 1



	tag['CDCs Left'] = CDC_LEFT
	tag['DEL1s Left'] = DEL1_LEFT
	tag['DEL2s Left'] = DEL2_LEFT
	tag['OPENs Left'] = OPEN_LEFT
	tag['HUMs Left'] = HUM_LEFT
	tag['PROJ Flag'] = PROJ_FLAG
	tag['ELEC Flag'] = ELEC_FLAG

	tag_list.append(tag)
# Serialize the list of dicts to JSON
j = json.dumps(tag_list)
 
# Write to file
with open(os.path.join('json','finaldata.json'), 'w') as f:
    f.write(j)

if (arg=='Y') or (arg=='y'):
	print(json.dumps(json.loads(j)[0], indent=4, sort_keys=True))







