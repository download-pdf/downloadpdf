#!/usr/bin/env python3
import logging
import unittest
import os
import shutil
import tracemalloc
from util.log import initializeLog
from util.storage import storagePath
from util.header import setHeaders
from main.scrape import scrapeHREF
from main.download import downloadPDF


class TestDownloadPDF(unittest.TestCase):
    os.environ["DEBUG"] = "TRUE"
    url = ''
    folder = ''
    location = ''
    pdfFileExists = False

    def setUp(self):
        super(TestDownloadPDF, self).setUp()
        initializeLog()

    def test_shouldDownloadFromAthena(self):
        self.folder = 'athena.ecs.csus.edu'
        self.url = 'http://athena.ecs.csus.edu/~buckley/CSc191/'
        pdfList = self.getPDF()

        self.assertIsNone(downloadPDF(self.url, self.location, pdfList))
        self.fileAndFolderExists()

    def test_shouldDownloadFromWTF(self):
        self.folder = 'wtf.tw'
        self.url = 'https://wtf.tw/ref/'
        pdfList = self.getPDF()

        self.assertIsNone(downloadPDF(self.url, self.location, pdfList))
        self.fileAndFolderExists()

    def getPDF(self):
        self.location = storagePath(self.url)
        setHeaders(self.url)

        return scrapeHREF(self.url)

    def fileAndFolderExists(self):
        self.assertTrue(os.path.exists('/tmp/' + self.folder))

        for fname in os.listdir('/tmp/' + self.folder):

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
