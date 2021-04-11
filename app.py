import gettext

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(_("Hello, world"))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    zh_TW = gettext.translation('messages', localedir='./translations', languages=['zh_TW'])
    zh_TW.install()
    _ = zh_TW.gettext
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
