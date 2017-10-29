# Rename Uber invioce
While reimbusing Uber trip one has to open the file to find the date and amount. This python script will create copy of each invoice file to data/output folder and renames the file to <Date><amount>.pdf. It also produces output with (date, amount) for easy reference.

Download Uber pdf receipts from your Uber trip web page to data/input folder. 

## Installing dependencies
	virtualenv virt_env
	pip install -r requirenements.pip


## Activate virtual env
	Ensure the virtual env is activated before executing below commands
	source virt_env/bin/activate

## run
	python rename_uber_receipts.py


