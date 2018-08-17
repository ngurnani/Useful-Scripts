"""
pdfmerger.py is a simple script to merge pdf files in a directory

input - target_directory
ouput - document-output.pdf file containing merged pdfs
"""

import sys
import os
from os import listdir
from PyPDF2 import PdfFileMerger, PdfFileReader


def mergefiles(target_directory):
    filenames = [f for f in listdir(target_directory)]
    filenames.sort()  # pdfs sorted in correct order
    merger = PdfFileMerger()
    for filename in filenames:
        print(filename)
        merger.append(PdfFileReader(open(filename, 'rb')))
    merger.write("document-output.pdf")
    print("All files successfully merged!")


def main():
    target_directory = sys.argv[1]
    os.chdir(target_directory)
    mergefiles(target_directory)


if __name__ == '__main__':
    main()
