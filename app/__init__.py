import tornado.httpserver
import tornado.ioloop
import tornado.web

from settings import config

from routes import url_patterns

def main():
    app = tornado.web.Application(url_patterns, debug=config.DEBUG)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(config.PORT)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
