from tornado.options import define, options

define("port", default=5000, help="run on the given port", type=int)
define("debug", default=False, help="debug mode")

options.debug = True