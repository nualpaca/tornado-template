from . import BaseHandler

import logging
logger = logging.getLogger('app.' + __name__)

class IndexHandler(BaseHandler):
    def get(self):
        self.write("Hello, world - this is the index page.")