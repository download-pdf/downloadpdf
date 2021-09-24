#!/usr/bin/env python3
import argparse


def setUpCLI():
    parser = argparse.ArgumentParser(
        description='Download PDFs from URL.')
    parser.add_argument('url', metavar='url',
                        type=str, help='URL, i.e. http://google.com')
    return parser.parse_args()
