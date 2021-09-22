# downloadpdf

Download PDF from the given URL.
i.e. It is like downloading only PDF files in a directory.

### Usage
`python main.py -h` : Get help
`DEBUG=true python main.py URL` : Run application in debug mode
`python main.py URL ` : Run application

URL must the directory of the PDF.

While in debug mode, the application will only fetch one PDF.

The downloaded PDFs are stored in /tmp/DOMAIN.
DOMAIN is the domain name from the URL.

Logs are stored in /tmp/pdfdownload.log.

## Quality Assurance

### Run Tests
`python -m unittest downloadpdf_test`: Run all the test cases/Classes
`python -m unittest downloadpdf_test.TestURL`: Run specific test Class
`python -m unittest downloadpdf_test.TestDownloadPDF.test_shouldDownloadFromAthena`: Run specific test case
`pytest downloadpdf_test.py --html=testcov-html/downloadpdf_testdata.html --cov=$(pwd) --cov-report=html`

