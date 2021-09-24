#!/usr/bin/env python3
import logging
from main.cli import setUpCLI
from util.storage import storagePath
from util.log import initilaizeLog
from util.url import validateURL
from util.header import setHeaders
from downloadpdf.download import downloadPDF
from downloadpdf.scrap import scrapHREF

try:
    args = setUpCLI()
    initilaizeLog()
    validateURL(args.url)
    location = storagePath(args.url)
    setHeaders(args.url)
    pdfs = scrapHREF(args.url)

    downloadPDF(args.url, location, pdfs)

except Exception as e:
    logging.error(e)
