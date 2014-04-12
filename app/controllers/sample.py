from . import BaseController

import logging
logger = logging.getLogger('app.' + __name__)

class SampleController(BaseController):
    def get(self):
        self.write("Hello, world")