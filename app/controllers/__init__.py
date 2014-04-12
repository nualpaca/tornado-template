import json
import tornado.web

import logging
logger = logging.getLogger('app.' + __name__)

class BaseController(tornado.web.RequestHandler):
    """A class to collect common handler methods - all other handlers should
    subclass this one.
    """
    pass