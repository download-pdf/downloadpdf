#!/usr/bin/env python3

import re
import os
import logging
from urllib import request
from urllib.parse import unquote
from bs4 import BeautifulSoup


def downloadPDF(url):
    """Download And Save PDF

    This script allows the user to downloads
    all PDF documents from the given URL.
    """
    try:
        isURLValid(url)
        dirPath = createFolder(url)
        logger = logging.getLogger('test')

        if (url.split("//")[0] == "https:"):
            opener = request.build_opener()
            opener.addheaders = [('User-agent',
                                  'Mozilla/5.0 (Macintosh; '
                                  'Intel Mac OS X 10_9_3) '
                                  'AppleWebKit/537.36(KHTML, like Gecko) '
                                  'Chrome/35.0.1916.47 '
                                  'Safari/537.36')]
            request.install_opener(opener)

        html = request.urlopen(url).read()

        soup = BeautifulSoup(html, features="html.parser")
        pdfs = soup.findAll("a", href=re.compile("pdf"))

        if len(pdfs) == 0:
            raise Exception('No PDFs found at ' + url)

        logger.info('Started  downloading PDFs from ' + url)

        for link in pdfs:
            decodedFileName = link.get('href')
            unquoteFileName = unquote(decodedFileName)

            request.urlretrieve(url + '/' + decodedFileName,
                                dirPath + '/' + unquoteFileName)

            logger.info('Downloaded ' + unquoteFileName)

            if (os.environ.get('DEBUG')):
                break

    except Exception as e:
        logger.error(e)


def isURLValid(url):
    regex = re.compile(
        r'^https?://'  # http:// or https://
        # domain...
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if (regex.search(url) is None or url is None):
        raise Exception('Invalid URL!')


def createFolder(url):
    url = url.split("//")[1]
    folderName = url.split("/")[0]
    dirPath = '/tmp/' + folderName

    if not os.path.exists(dirPath):
        os.mkdir(dirPath)

    return dirPath
