#!/usr/bin/env python

import logging
import unittest
import os, sys
import shutil
import downloadpdf
import tracemalloc

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
    os.environ["DEBUG"] = "TRUE"
    
    url = ''
    folder = ''
    pdfFileExists = False

    def setUp(self):
        super(TestDownloadPDF, self).setUp()
        self.initilaizeLog()
    
    def initilaizeLog(self):
        logfile =  '/tmp/pdfdownload.log'
        log_format = (
            '[%(asctime)s] %(levelname)-8s %(name)-12s ' 
            '%(message)s')
        
        logging.basicConfig(
            level=logging.INFO,
            format=log_format,
            filename=logfile
        )

    def test_shouldDownloadFromAthena(self):
        self.folder = 'athena.ecs.csus.edu'
        self.url = 'http://athena.ecs.csus.edu/~buckley/CSc191/'
        self.assertIsNone(downloadpdf.downloadPDF(self.url))
        self.fileAndFolderExists(self.folder)

    def test_shouldDownloadFromWTF(self):
        self.folder = 'wtf.tw'
        self.url = 'https://wtf.tw/ref/'
        self.assertIsNone(downloadpdf.downloadPDF(self.url))
        self.fileAndFolderExists(self.folder)
    
    def test_shouldProcessGracefully(self):
        self.folder = 'codeanit.com'
        self.url = 'https://codeanit.com'
        self.assertIsNone(downloadpdf.downloadPDF(self.url))
    
    def fileAndFolderExists(self, folder):
        self.assertTrue(os.path.exists('/tmp/' + folder))

        for fname in os.listdir('/tmp/' + folder):
            
            if fname.endswith('.pdf'):
                self.pdfFileExists = True
                break
        
        self.assertTrue(self.pdfFileExists)

    def tearDown(self):
        super(TestDownloadPDF, self).tearDown()
       
        urlPart = self.url.split("//")[1]
        folderName = urlPart.split("/")[0]
        dirPath =  '/tmp/' + folderName

        if os.path.exists(dirPath):
            shutil.rmtree(dirPath)
        
        logging.FileHandler(self.folder).close()
        logging.shutdown()

        self.url = ''
        self.pdfFileExists = False
        self.folder=''

'''
Pass PYTHONTRACEMALLOC=1 in CLI to enable tracing.
'''
tracemalloc.start()

if __name__ == '__main__':
    unittest.main()

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')
for stat in top_stats[:10]:
    print(stat)

# https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python#24065533
# https://stackoverflow.com/questions/303200/how-do-i-remove-delete-a-folder-that-is-not-empty#303225
# https://docs.python.org/3/library/exceptions.html
# https://docs.python.org/3/library/tracemalloc.html