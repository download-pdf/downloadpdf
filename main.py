#!/usr/bin/env python3

import argparse
from downloadpdf import downloadPDF

parser = argparse.ArgumentParser(
    description='Download PDFs from URL.')
parser.add_argument('url', metavar='url', 
    type=str, help='URL')
args = parser.parse_args()
downloadPDF(args.url)
