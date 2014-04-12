# import json
# # from bson import json_util
# from datetime import datetime

# import tornado.web
# import tornado.ioloop
# import tornado.escape
# import tornado.gen as gen
# # from pymongo.errors import ConnectionFailure
# # from motor import MotorClient


# class UserResource(tornado.web.RequestHandler):

#     def set_default_headers(self):
#         self.set_header("Content-Type", "application/json")

#     def write_error(self, status_code, **kwargs):
#         self.write({"status": status_code, "msg": tornado.web.httputil.responses.get(status_code, "Unknown")})

#     @property
#     def db(self):
#         return self.application.database

#     @gen.coroutine
#     def get(self, n=None):
#         doc, err = (yield gen.Task(self.db.users.find_one, dict(_id=int(n)))).args if n else (yield gen.Task(self.db.users.find().limit(self.get_argument("limit", 10)).to_list)).args
#         if err:
#             raise tornado.web.HTTPError(500)
#         if n and not doc:
#             raise tornado.web.HTTPError(404)
#         self.write(json.dumps({"status": 200, "msg": "OK", "response": doc}, default=json_util))

#     @gen.coroutine
#     def post(self):
#         body = tornado.escape.json_decode(self.request.body)
#         body["created"] = body["updated"] = datetime.utcnow().isoformat()
#         res, err = (yield gen.Task(self.db.counters.find_and_modify, {"_id": "users"}, {"$inc": {"seq": 1}})).args
#         if err:
#             raise tornado.web.HTTPError(500)
#         body["_id"] = int(res["seq"])
#         doc, err = (yield gen.Task(self.db.users.insert, body)).args
#         if err:
#             raise tornado.web.HTTPError(500)
#         self.send_error(201)

#     @gen.coroutine
#     def put(self, n):
#         body = tornado.escape.json_decode(self.request.body)
#         body["updated"] = datetime.utcnow().isoformat()
#         res, err = (yield gen.Task(self.db.users.update, dict(_id=int(n)), {"$set": body})).args
#         if err:
#             raise tornado.web.HTTPError(500)
#         self.send_error(202)

#     @gen.coroutine
#     def delete(self, n):
#         res, err = (yield gen.Task(self.db.users.remove, dict(_id=int(n)))).args
#         if err:
#             raise tornado.web.HTTPError(500)
#         if res['n']:
#             raise tornado.web.HTTPError(204)
#         self.send_error(410)


# def main():
#     app = tornado.web.Application(
#         [
#             (r"/users/([0-9]+)", UserResource),
#             (r"/users/", UserResource)
#         ],
#         autoreload=True
#     )

#     try:
#         setattr(app, "database", MotorClient("localhost", 27017).open_sync()["test"])
#     except ConnectionFailure as e:
#         print(e)

#     print("starting server on port %i" % 3030)
#     app.listen(3030)
#     tornado.ioloop.IOLoop.instance().start()


# if __name__ == "__main__": main()