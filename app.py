import gettext

import tornado.ioloop
import tornado.web

en_US = gettext.translation('messages', localedir='./translations', languages=['en_US'])
zh_TW = gettext.translation('messages', localedir='./translations', languages=['zh_TW'])

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        en_US.install()
        self.write(_("Hello, world"))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    zh_TW.install()
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
