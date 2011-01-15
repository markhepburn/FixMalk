#!/usr/bin/env python2.5

from cStringIO import StringIO
import logging
import urllib, urllib2
import web
import web.webapi
import xml.etree.ElementTree as et

routes = (
    '/(.*)', 'Handler'
)

remote_url = 'http://www.drinkmalk.com/books/'
nslink = '{http://www.w3.org/2005/Atom}link'
relaccess = 'http://opds-spec.org/acquisition/open-access'
linktype = 'application/epub'   # ...+zip, sometimes

class Handler(object):
    def GET(self, req):
        logging.debug('got request "%s"' % req)
        # correct if necessary, then pass on request:
        if req in ('', '/'):
            req = req + 'list.xml'
        if req[0] == '/':
            req = req[1:]

        params = urllib.urlencode(web.input())
        if params:
            req = req + '?' + params
        logging.debug('will request "%s"' % req)

        fullrequest = urllib2.Request(remote_url + req)
        opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1))
        remoteresponse = opener.open(fullrequest)
        logging.debug(remoteresponse.info())

        remoteContentType = remoteresponse.info()['Content-Type']
        logging.debug("Remote content-type: %s" % remoteContentType)

        fixedresponse = fixLinks(remoteresponse)
        logging.debug('passing back corrected response:' + fixedresponse)
        web.webapi.header('Content-Type', remoteContentType)
        return fixedresponse

def fixLinks(xml):
    """Fix up download links by adding the right rel-attribute value.
    Note that we currently rely on href values being relative, but
    this could also be corrected for."""

    tree = et.parse(xml)
    for link in tree.getiterator(nslink):
        if link.get('type').startswith(linktype):
            link.set('rel', relaccess)
    outputstr = StringIO()
    tree.write(outputstr)
    return '<?xml version="1.0"?>' + outputstr.getvalue()

def main():
    logging.basicConfig(level=logging.DEBUG)
    app = web.application(routes, globals())
    app.run()


if __name__ == '__main__':
    import sys
    sys.exit(main())
