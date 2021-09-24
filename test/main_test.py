#!/usr/bin/env python3
import logging
import unittest
import os
import shutil
import tracemalloc
from util.log import initilaizeLog
from util.storage import storagePath
from util.header import setHeaders
from main.scrap import scrapHREF
from main.download import downloadPDF


class TestDownloadPDF(unittest.TestCase):
    os.environ["DEBUG"] = "TRUE"
    url = ''
    folder = ''
    pdfFileExists = False

    def setUp(self):
        super(TestDownloadPDF, self).setUp()
        initilaizeLog()

    def test_shouldDownloadFromAthena(self):
        self.folder = 'athena.ecs.csus.edu'
        self.url = 'http://athena.ecs.csus.edu/~buckley/CSc191/'
        location = storagePath(self.url)
        setHeaders(self.url)
        pdfs = scrapHREF(self.url)

        self.assertIsNone(downloadPDF(self.url, location, pdfs))
        self.fileAndFolderExists(self.folder)

    def test_shouldDownloadFromWTF(self):
        self.folder = 'wtf.tw'
        self.url = 'https://wtf.tw/ref/'
        location = storagePath(self.url)
        setHeaders(self.url)
        pdfs = scrapHREF(self.url)

        self.assertIsNone(downloadPDF(self.url, location, pdfs))
        self.fileAndFolderExists(self.folder)

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
        location = '/tmp/' + folderName

        if os.path.exists(location):
            shutil.rmtree(location)

        logging.shutdown()

        self.url = ''
        self.pdfFileExists = False
        self.folder = ''


'''
Pass PYTHONTRACEMALLOC=1 in CLI to enable memory tracing.
'''
tracemalloc.start()

if __name__ == '__main__':
    unittest.main()

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')
for stat in top_stats[:10]:
    print(stat)
