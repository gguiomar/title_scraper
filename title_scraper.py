#A simple script to download the titles of a list of scientific papers

from urllib2 import Request, urlopen, URLError
from urllib2 import urlopen
from lxml.html import parse

#some example urls
urls = ['http://www.nature.com/ncomms/2015/151014/ncomms9581/full/ncomms9581.html',
'http://www.nature.com/ncomms/2015/151013/ncomms9537/full/ncomms9537.html']


for i,e in enumerate(urls):
    
    #try's to open the url, if it fails it moves onto the next one
    req = Request(e)
    try:
        response = urlopen(req)
    except URLError as ea:
        if hasattr(ea, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', ea.reason
        elif hasattr(ea, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', ea.code
    else:
        print i
        p = parse(response)
        print e
        print p.find(".//title").text
        print '---'