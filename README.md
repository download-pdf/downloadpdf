# downloadpdf

Download PDFs from the given URL.

### Usage
`python main.py -h` : Get help
`DEBUG=true python main.py URL` : Run application in debug mode
`python main.py URL ` : Run application

URL must the directory of the PDF.

While in debug mode, the application will only fetch one PDF.

The downloaded PDFs are stored in /tmp/DOMAIN.
DOMAIN is the domain name from the URL.

Logs are stored in /tmp/pdfdownload.log.
