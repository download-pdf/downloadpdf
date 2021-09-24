#!/usr/bin/env python3
from urllib import request


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
