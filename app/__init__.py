import tornado.httpserver
import tornado.ioloop
import tornado.web

from settings import config

from . import routes
from . import models
from . import controllers

app = tornado.web.Application(routes.url_patterns, debug=config.DEBUG)
http_server = tornado.httpserver.HTTPServer(app)
http_server.listen(config.PORT)
tornado.ioloop.IOLoop.instance().start()