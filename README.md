# ARC

##Setup Instructions

* Setup Python Virtual Environment using `virtualenv arc`. If virtualenv is not there present, then `pip install virtualenv`.
* Activate Virtual Environment `cd arc`, `source bin/activate`
* Clone the repository `git clone https://github.com/SebastinSanty/arc`
* Run the files using `python <file>`. The functions of each file is mentioned below.

##General Instructions
* tagging contains all the files.
* data.xls: Excel data provided.
* xlstojson.py takes data from xls and saves it into data.json
* jsontoxls_filtered.py converts json from data.json to xls filtering out data and outputs into filterd.xls
* ignore jsonmultilevel_sorted.py