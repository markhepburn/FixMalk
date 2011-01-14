#!/usr/bin/env python2.5

import cStringIO as StringIO
import logging
import web
import xml.etree.ElementTree as et

routes = (
    '/(.*)', 'Handler'
)

remote_url = 'http://www.drinkmalk.com/books/'
nslink = '{http://www.w3.org/2005/Atom}link'
relaccess = 'http://opds-spec.org/acquisition/open-access'
linktype = 'application/epub' # +zip, sometimes

class Handler(object):
    def GET(self, req):
        logging.debug('got request "%s"' % req)
        return 'ping -> pong'

def fixLinks(xml):
    tree = et.parse(xml)
    for link in tree.getiterator(nslink):
        if link.get('type').startswith(linktype):
            link.set('rel', relaccess)
    outputstr = StringIO()
    tree.write(outputstr)
    return outputstr.getvalue()

def main():
    logging.basicConfig(level=logging.DEBUG)
    app = web.application(routes, globals())
    app.run()


if __name__ == '__main__':
    import sys
    sys.exit(main())
