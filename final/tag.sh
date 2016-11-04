#!/bin/sh
if [[ $4 = '1' ]]
then
	python coursetype.py $1
fi
if [[ $5 = '1' ]]
then
	python noofcourse.py $2
fi
if [[ $6 = '1' ]]
then
	python studentdata.py $3
fi
python logic.py
python jsontoxls_final.py
open result/final.xls