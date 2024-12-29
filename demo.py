import tornado.web
import tornado.ioloop


class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("This is a python command")


class animalsListRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class queryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("num")
        if num.isdigit():
            num = int(num)  # important conversion
            result = "Even" if num % 2 == 0 else "Odd"
            self.write(f"Number {num} is {result}")
        else:
            self.write("num is not a valid int")

class resourceParamReqHandler(tornado.web.RequestHandler):
    def get(self, studentName, courseId):
        self.write(f"Welcome {studentName} to {courseId} course")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler),                                # http://localhost:8882/
        (r"/animals", animalsListRequestHandler),                   # http://localhost:8882/animals
        (r"/isEven", queryParamRequestHandler),                     # http://localhost:8882/isEven?num=7
        (r"/students/([a-z]+)/([0-9]+)", resourceParamReqHandler)   # http://localhost:8882/students/anta/676
    ])
    port = 8882
    app.listen(port)
    print(f"App is up on port {port}")
    tornado.ioloop.IOLoop.current().start()
