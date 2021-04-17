import tornado.ioloop
import tornado.web

from tools import switch_locale


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        switch_locale('zh')
        self.write(_("Hello, world"))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    switch_locale('en')
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
