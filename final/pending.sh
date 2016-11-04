#!/bin/sh
if [[ $4 == '1' ]]
then
	python coursetype.py $1
	echo 'Coursetype Done'
fi
if [[ $5 == '1' ]]
then
	python noofcourse.py $2
	echo 'No Of Course Done'
fi
if [[ $6 == '1' ]]
then
	python studentdata.py $3
	echo 'Student Data Done'
fi
python logic.py
echo 'Logic Done'
python jsontoxls_pre.py
echo 'Excel created'
open result/final_tag.xls