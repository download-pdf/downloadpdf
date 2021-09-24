#!/usr/bin/env python3
import unittest
import os
import shutil
from util.storage import storagePath


class TestFolder(unittest.TestCase):
    def test_shouldCreateFolder(self):
        url = 'https://test.com'
        dirPath = '/tmp/test.com'

        if os.path.exists(dirPath):
            shutil.rmtree('/tmp/test.com')

        self.assertEqual(storagePath(url), dirPath)

    def test_shouldReturnFolderPathIfExists(self):
        url = 'http://test.com'
        dirPath = '/tmp/test.com'

        if not os.path.exists(dirPath):
            os.mkdir(dirPath)

        self.assertEqual(storagePath(url), dirPath)

    def tearDown(self):
        super(TestFolder, self).tearDown()

        if os.path.exists('/tmp/test.com'):
            shutil.rmtree('/tmp/test.com')
