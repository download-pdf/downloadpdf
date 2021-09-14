import urllib, re, os, sys, logging
from urllib import request
from urllib.parse import unquote
from bs4 import BeautifulSoup

def initilaizeLog(dir):
    global logger     
    logfile = dir + '/.log'
    log_format = (
        '[%(asctime)s] %(levelname)-8s %(name)-12s ' 
        '%(message)s')

    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[
            logging.FileHandler(logfile),
            logging.StreamHandler(sys.stdout),
        ],
    )

    logger = logging.getLogger(dir.split("/")[2])

def downloadPDF(url):
    """Download And Save PDF

    This script allows the user to downloads
    all PDF documents from the given URL.
    """
    try:
        isURLValid(url)

        if ( url.split("//")[0] == "https:"):
            opener = request.build_opener()
            opener.addheaders = [('User-agent', 
                'Mozilla/5.0 (Macintosh; '
                'Intel Mac OS X 10_9_3) '
                'AppleWebKit/537.36(KHTML, like Gecko) '
                'Chrome/35.0.1916.47 '
                'Safari/537.36')]
            request.install_opener(opener)

        html = request.urlopen(url).read()

        soup = BeautifulSoup(html, features="html.parser")
        pdfs = soup.findAll("a", href=re.compile("pdf"))
        
        if len(pdfs) == 0:
            raise Exception('No PDFs found!')

        dirPath = createFolder(url)
        initilaizeLog(dirPath)
        
        logger.info('Started  wtf.tw PDFs from ' + url)
        
        for link in pdfs:
            decodedFileName = link.get('href')
            unquoteFileName = unquote(decodedFileName)  
            request.urlretrieve( url + decodedFileName, 
                dirPath + '/' + unquoteFileName)
            
            logger.info('Downloaded ' + unquoteFileName)

    except Exception as e:
        exit(e)

def isURLValid(url):
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if ( regex.search(url) is None  or url is None):
        raise Exception('Invalid URL!')
 
def createFolder(url):
        url = url.split("//")[1]
        folderName = url.split("/")[0]
        dirPath =  '/tmp/' + folderName

        if os.path.exists(dirPath):
            raise Exception('Folder exists!')
        else:
            os.mkdir(dirPath)
            return dirPath
