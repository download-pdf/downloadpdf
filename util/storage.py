#!/usr/bin/env python3
import os


def storagePath(url):
    url = url.split("//")[1]
    folderName = url.split("/")[0]
    dirPath = '/tmp/' + folderName

    if not os.path.exists(dirPath):
        os.mkdir(dirPath)

    return dirPath
