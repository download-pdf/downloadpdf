#!/usr/bin/env python3
import re
from urllib import request


def validateURL(url):
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


def setHeaders(url):
    if (url.split("//")[0] == "https:"):
        opener = request.build_opener()
        opener.addheaders = [('User-agent',
                              'Mozilla/5.0 (Macintosh; '
                              'Intel Mac OS X 10_9_3) '
                              'AppleWebKit/537.36(KHTML, like Gecko) '
                              'Chrome/35.0.1916.47 '
                              'Safari/537.36')]
        request.install_opener(opener)
