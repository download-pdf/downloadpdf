#!/usr/bin/env python3
import logging


def initilaizeLog():
    logfile = '/tmp/downloadpdf.log'
    log_format = (
        '[%(asctime)s] %(levelname)-8s %(name)-12s '
        '%(message)s')

    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        filename=logfile
    )
