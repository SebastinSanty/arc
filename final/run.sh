#!/bin/sh
echo 'Welcome to ARC Elective Module (BITS Pilani K.K. Birla Goa Campus)'
echo 'Further steps will require you to input the filename of the excel file, to be parsed into JSON, recognizable by this software.'
echo 'Do you wish to continue?(Y/N)'
read option
if [ $option = 'Y' ]
then
	echo 'Excel file containing the course description will be processed[ENTER]'
	read coursetype
	python coursetype.py data/coursetype.xlsx
	echo 'Excel file containing the no of courses to be completed in a particular discipline will be processed[ENTER]'
	read noofcourse
	python noofcourse.py data/noofcourse.xls
	echo 'Excel file containing the student description will be processed'
	read studentdata
	python studentdata.py data/studentdata.xls
	echo 'Do you want the final output to be displayed?(Y/N)'
	read display
	python logic.py $display
	echo 'Do you want to the final output as excel file?(Y/N)'
	read ask
	if [ $ask = 'Y' ]
	then
		python jsontoxls_final.py
	fi
fi