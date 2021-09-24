# downloadpdf

Download PDFs from the given URL.

### Usage
`python -m downloadpdf -h` : Get help
`DEBUG=true python -m downloadpdf URL` : Run application in debug mode
`python -m downloadpdf URL ` : Run application

In debug mode, the application will only fetch one PDF.

The downloaded PDFs are stored in /tmp/DOMAIN.
DOMAIN is the domain name from the URL.

Logs are stored in /tmp/pdfdownload.log.
