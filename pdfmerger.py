# simple script to merge pdf files in directory

import os
from os import listdir
from PyPDF2 import PdfFileMerger, PdfFileReader

target_directory = '/Users/ngurnani/Desktop/cambridge-core_bootstrap-methods-and-their-application_11May2018'
os.chdir(target_directory)

filenames = [f for f in listdir(target_directory)]
merger = PdfFileMerger()
for filename in filenames:
    merger.append(PdfFileReader(open(filename, 'rb')))

merger.write("document-output.pdf")