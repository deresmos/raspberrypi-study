import json

import tornado.ioloop
import tornado.web
import tornado.websocket

IS_PIR_RUNNING = False


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    count = 0
    clients = set()

    def open(self):
        print(f"Websocket open ({self.request.remote_ip})")
        WebSocketHandler.clients.add(self)
        self.write_message(self.make_payload(WebSocketHandler.count))

    def on_message(self, message):
        _dict = json.loads(message)
        count = int(_dict.get("count", 0))
        WebSocketHandler.count = count

        payload = self.make_payload(count)
        for client in WebSocketHandler.clients:
            client.write_message(payload)

    def on_close(self):
        print(f"Websocket close ({self.request.remote_ip})")
        WebSocketHandler.clients.remove(self)

    def make_payload(self, count):
        return json.dumps({"count": count})


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


if __name__ == "__main__":
    application = tornado.web.Application(
        [(r"/", MainHandler), (r"/websocket", WebSocketHandler)]
    )
    application.listen(8008)
    tornado.ioloop.IOLoop.current().start()
