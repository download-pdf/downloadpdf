#!/usr/bin/env python3
import unittest
from util import validateURL


class TestURL(unittest.TestCase):
    obj = ""

    def test_shouldPassWithValidURL(self):
        validURL = 'http://google.com'
        self.assertIsNone(validateURL(validURL))

    def test_shouldRaiseExceptionWithInvalidURL(self):
        invalidURL = 'google.com'
        with self.assertRaises(Exception) as cm:
            validateURL(invalidURL)
        self.assertIsInstance(cm.exception, Exception)
