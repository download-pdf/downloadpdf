#!/usr/bin/env python3
import logging
from main.cli import setUpCLI
from downloadpdf.download import downloadPDF
from downloadpdf.scrap import scrapHREF
from util.storage import storagePath
from util.log import initilaizeLog
from util.url import validateURL
from util.url import setHeaders


try:
    args = setUpCLI

    initilaizeLog()
    logger = logging.getLogger(args.url.split("//")[1])

    validateURL(args.url)
    location = storagePath(args.url)
    setHeaders(args.url)
    pdfs = scrapHREF(args.url)

    downloadPDF(args.url, location, pdfs)

except Exception as e:
    logger.error(e)
