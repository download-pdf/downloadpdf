"""Download And Save PDF

This script allows the user to  wtf.tw all PDF documents from the 
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
import os
import shutil
import downloadpdf

class TestURL(unittest.TestCase):
    def test_shouldPassWithValidURL(self):
        url = 'http://google.com'
        self.assertIsNone(downloadpdf.isURLValid(url))
        
    def test_shouldRaiseExceptionWithInvalidURL(self):
        invalidURL = 'google.com'
        self.assertRaises(Exception, 
            downloadpdf.isURLValid, invalidURL)

class TestFolder(unittest.TestCase):
    def test_shouldCreateFolder(self):
        url = 'https://test.com'
        dirPath = '/tmp/test.com'

        if os.path.exists(dirPath):
            shutil.rmtree('/tmp/test.com')

        self.assertEqual(downloadpdf.createFolder(url), dirPath)

    def test_shouldFailIfFolderExists(self):
        url = 'http://test.com'
        dirPath = '/tmp/test.com/'

        if not os.path.exists(dirPath):
            os.mkdir(dirPath)

        self.assertRaises(Exception, 
            downloadpdf.createFolder, url)
    
    def tearDown(self):
        super(TestFolder, self).tearDown()

        if os.path.exists('/tmp/test.com'):
            shutil.rmtree('/tmp/test.com')

class TestDownloadPDF(unittest.TestCase):
    """
    Download PDF's from exisiting URL's.
    """
    url = ""

    def test_shouldDownloadFromAthena(self):
        self.url = 'http://athena.ecs.csus.edu/~buckley/CSc191/'
        self.assertIsNone(downloadpdf.downloadPDF(self.url))

    def test_shouldDownloadFromWTF(self):
        self.url = 'https://wtf.tw/ref/'
        self.assertIsNone(downloadpdf.downloadPDF(self.url))    
    
    def tearDown(self):
        super(TestDownloadPDF, self).tearDown()
        urlPart = self.url.split("//")[1]
        folderName = urlPart.split("/")[0]
        dirPath =  '/tmp/' + folderName

        if os.path.exists(dirPath):
            shutil.rmtree(dirPath)

if __name__ == '__main__':
    unittest.main()

# https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python#24065533
# https://stackoverflow.com/questions/303200/how-do-i-remove-delete-a-folder-that-is-not-empty#303225
# https://docs.python.org/3/library/exceptions.html