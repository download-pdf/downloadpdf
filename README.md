# downloadpdf

Download PDF from the given URL.

### Usage
`pip install downloadpdf`: Install
`python -m downloadpdf -h`: Get help
`DEBUG=true python -m downloadpdf URL`: Run application in debug mode
`python -m downloadpdf URL `: Run application

In debug mode, the application will only fetch one PDF.

The downloaded PDFs are stored in /tmp/DOMAIN. DOMAIN is the domain name from the URL.

Logs are stored in /tmp/pdfdownload.log.

Test are stored in /test.

### Development
`.git/hooks/pre-commit`: Git hook is used for quality assurance.
`.github/workflows/cicd.yml`: Github workflow is used for continuous integration and continuous deployment.
Package is continuously deployed at https://pypi.org/project/downloadpdf/.