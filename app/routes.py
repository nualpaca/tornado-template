from controllers.users import UserController
from handlers.index import IndexHandler

url_patterns = [
	(r"/", IndexHandler),
    (r"/users", UserController),
]
