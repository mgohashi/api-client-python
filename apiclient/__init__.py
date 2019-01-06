from apiclient.api import ClientsHandler, ClientHandler
from pkg_resources import resource_filename
import logging.config
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application


def main():
    """Construct and serve the tornado application."""

    logging_cfg_file = 'logging.ini'
    try:
        logging.config.fileConfig(logging_cfg_file,
                                  disable_existing_loggers=False)
    except KeyError:
        log_config_location = resource_filename(__name__, logging_cfg_file)
        logging.config.fileConfig(log_config_location, disable_existing_loggers=False)

    define('port', default=8888, help='port to listen on')

    app = Application(
        [
            (r"/api/v1/client", ClientsHandler),
            (r"/api/v1/client/([0-9]+)", ClientHandler)
        ],
        autoreload=True,
        debug=True)
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    print(f'Listening on http://127.0.0.1:{options.port}')
    IOLoop.current().start()
