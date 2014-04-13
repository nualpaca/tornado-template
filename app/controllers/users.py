from . import BaseController

import logging
logger = logging.getLogger('app.' + __name__)

class UserController(BaseController):
    def get(self):
        self.write("Hello, world - this is the user controller")