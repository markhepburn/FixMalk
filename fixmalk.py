#!/usr/bin/env python2.5

import web
import logging

routes = (
    '/(.*)', 'Handler'
)

remote_url = 'http://www.drinkmalk.com/books/'

class Handler(object):
    def GET(self, req):
        logging.debug('got request "%s"' % req)
        return 'ping -> pong'

def main():
    logging.basicConfig(level=logging.DEBUG)
    app = web.application(routes, globals())
    app.run()


if __name__ == '__main__':
    import sys
    sys.exit(main())
