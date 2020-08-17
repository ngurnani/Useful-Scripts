"""
get_files.py

Simply function to return all files of a certain type within a filepath
"""
import os
import glob
from decorators import timer


@timer
def get_files(filepath, fileprefix="", filetype="json"):
    """
    return all files of  filetype in filepath
    :param filepath: str
    :param fileprefix: str
    :param filetype: str (json, pdf, xlsx)
    :return: list of files
    """
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, "{0}*.{1}".format(fileprefix, filetype)))
        for f in files:
            all_files.append(os.path.abspath(f))
    return all_files
