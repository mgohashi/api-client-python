from apiclient.api import ClientsHandler, ClientHandler
from os import path
import logging.config
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application

log_file_path = path.join(
    path.dirname(path.abspath(__file__)),
    'logging.ini')
logging.config.fileConfig(
    log_file_path,
    disable_existing_loggers=False)
define('port', default=8888, help='port to listen on')


def main():
    """Construct and serve the tornado application."""
    app = Application(
        [
            (r"/api/v1/client", ClientsHandler),
            (r"/api/v1/client/([0-9]+)", ClientHandler)
        ])
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    print(f'Listening on http://127.0.0.1:{options.port}')
    IOLoop.current().start()
