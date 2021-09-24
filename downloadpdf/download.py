#!/usr/bin/env python3
import logging
import os
from urllib import request
from urllib.parse import unquote


def downloadPDF(url, storage, pdfs):
    logger = logging.getLogger(storage)

    for link in pdfs:
        decodedFileName = link.get('href')
        unquoteFileName = unquote(decodedFileName)

        request.urlretrieve(url + '/' + decodedFileName,
                            storage + '/' + unquoteFileName)

        logger.info(unquoteFileName)

        if (os.environ.get('DEBUG')):
            break
