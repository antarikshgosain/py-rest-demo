import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("This is a python command")
class animalsListRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/animals", animalsListRequestHandler)
    ])
    port = 8882
    app.listen(port)
    print(f"App is up on port {port}")
    tornado.ioloop.IOLoop.current().start()