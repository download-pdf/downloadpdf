"""Download And Save PDF

This script allows the user to download all PDF documents from the 
URL.

At the moment it does not accept URL as a parameter as a static
URL is provided.

This script requires that `BeautifulSoup` be installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following
functions:

    * downloadPDF - Downloads and stores PDF

TODO: 
    - Write Unit tests
    - Pass URL as a parameter in downloadPDF()
    - Make the system installable and standalone 
"""

import unittest
import requests
from bs4 import BeautifulSoup
import urllib
import re
from urllib.parse import unquote
import os

def downloadPDF():
    """
    Downloads PDF's from the URL.
    """

    URL = 'http://athena.ecs.csus.edu/~buckley/CSc191/'
    response = urllib.request.urlopen(URL)
    html = response.read()
    soup = BeautifulSoup(html)

    for link in soup.find_all("a", href=re.compile("pdf")):
        decodedFileName = unquote(link.get('href'))
        r = requests.get(URL+decodedFileName)
        with open(os.path.join('/home/anit/work/athena.ecs.csus.edu', decodedFileName), 'wb') as f:
            f.write(r.content) 

if __name__ == '__main__':
    downloadPDF()

class TestSolution(unittest.TestCase):
    def test_downloadPDF(self):            
        print('TODO')
