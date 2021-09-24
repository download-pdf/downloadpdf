#!/usr/bin/env python3
import re
from urllib import request
from bs4 import BeautifulSoup


def scrapHREF(url):
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")
    pdfs = soup.findAll("a", href=re.compile("pdf"))

    if len(pdfs) == 0:
        raise Exception('No PDFs found at ' + url)

    return pdfs
