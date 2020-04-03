"""
filedownloader.py is a simple script to download all files of a certain type
(e.g. pdf) from a web directory

input - target_directory, ftype, archive_url
ouput - all the files in that directory
"""

import sys
import os
import requests
from bs4 import BeautifulSoup


def get_file_links(ftype, archive_url):

    # create response object
    r = requests.get(archive_url)

    # create beautiful-soup object
    soup = BeautifulSoup(r.content, "html5lib")

    # find all links on web-page
    links = soup.findAll("a")

    # filter the link sending with file type
    # specified by ftype (i.e. .pdf, .mp4 etc.)
    file_links = [
        archive_url + link["href"] for link in links if link["href"].endswith(ftype)
    ]

    return file_links


def download_files(file_links):

    for link in file_links:

        """iterate through all links in file_links
        and download them one by one"""

        # obtain filename by splitting url and getting
        # last string
        file_name = link.split("/")[-1]

        print("Downloading file:%s" % file_name)

        # create response object
        r = requests.get(link, stream=True)

        # download started
        with open(file_name, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)

        print("%s downloaded!\n" % file_name)

    print("All files downloaded!")
    return


def main():
    target_directory = sys.argv[1]
    os.chdir(target_directory)
    ftype = sys.argv[2]
    archive_url = sys.argv[3]
    file_links = get_file_links(ftype, archive_url)
    os.chdir(target_directory)
    download_files(file_links)


if __name__ == "__main__":
    main()
