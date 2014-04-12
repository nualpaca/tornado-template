import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options

import settings

from routes import url_patterns

def main():
    app = tornado.web.Application(url_patterns, debug=options.debug)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
