# **downloadpdf**

**Download PDF from the given URL.**

## **Usage**

`pip install downloadpdf`: Install application.

`python -m downloadpdf -h`: Get help.

`DEBUG=1 python -m downloadpdf URL`: Run application in debug mode.

`python -m downloadpdf URL`: Run application

In debug mode (`DEBUG=1`), the application will only fetch **one** PDF.

The downloaded PDFs are stored in `/tmp/DOMAIN`. `DOMAIN` is the domain name from the URL.

Logs are stored in `/tmp/pdfdownload.log`.

Test are stored in `/test`.

## **Development**
`.git/hooks/pre-commit`: Git hook is used for quality assurance.

`.github/workflows`: Github workflow is used for continuous integration and continuous deployment.

Package is continuously deployed at `https://pypi.org/project/downloadpdf/`. 

To deploy, push a `tag`. Tag and `setup.py` version must be higher than the previous deployed versions.


[![Build And Deploy downloadpdf](https://github.com/PythonCheatsheet/downloadpdf/actions/workflows/cicd.yml/badge.svg)](https://github.com/PythonCheatsheet/downloadpdf/actions/workflows/cicd.yml)