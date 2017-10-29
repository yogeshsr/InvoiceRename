
import os 
from os import listdir
from os.path import isfile, join
from shutil import copyfile
import PyPDF2
import re


dir_path = os.path.dirname(os.path.realpath(__file__))

input_dir = join(dir_path, 'data', 'input')
output_dir = join(dir_path, 'data', 'output')

onlyfiles = [join(input_dir, f) for f in listdir(input_dir) if f.endswith('pdf') and isfile(join(input_dir, f))]

count=0
def rename_to_date_and_amount(file_name):
    global count
    pdf = open(file_name, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdf)
    pageObj = pdfReader.getPage(0)

    dated=re.search('Invoice Date: \d+ \w+ \d{4}', pageObj.extractText()).group(0).split(':')[-1].strip()
    amount=re.search('Gross Amount \n*\d+\.\d+ INR', pageObj.extractText()).group(0).split(' ')[-2].strip()
    
    ext = '.pdf'
    out_file = join(output_dir, dated + '-amt-' + str(amount) + ext)
    # incase file exists add a counter.
    while isfile(out_file):
        out_file = join(output_dir, dated + '-amt-' + str(amount) + '-' + str(count) + ext)
        count=count+1

    count=0
    out_file = out_file
    copyfile(file_name, out_file)
    print(dated + ', amt-' + str(amount))
    
if __name__ == '__main__':
    list(map(lambda f: rename_to_date_and_amount(f), onlyfiles))
    print('Copying with new name done!')