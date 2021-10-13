#!/usr/bin/env python3
import logging
from util.cli import setUpCLI
from util.storage import storagePath
from util.log import initialiseLog
from util.url import validateURL
from util.header import setHeaders
from main.download import downloadPDF
from main.scrape import scrapeHREF

try:
    args = setUpCLI()
    initialiseLog()
    validateURL(args.url)
    location = storagePath(args.url)
    setHeaders(args.url)
    pdfs = scrapeHREF(args.url)

    downloadPDF(args.url, location, pdfs)

except Exception as e:
    logging.error(e)

