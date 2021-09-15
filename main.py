#!/usr/bin/env python3

import argparse
import logging
from downloadpdf import downloadPDF

parser = argparse.ArgumentParser(
    description='Download PDFs from URL.')
parser.add_argument('url', metavar='url', 
    type=str, help='URL, i.e. http://google.com')
args = parser.parse_args()

logfile =  '/tmp/pdfdownload.log'
log_format = (
    '[%(asctime)s] %(levelname)-8s %(name)-12s ' 
    '%(message)s')

logging.basicConfig(
    level=logging.INFO,
    format=log_format,
    filename=logfile)

downloadPDF(args.url)
