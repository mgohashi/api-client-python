import json
from tornado.web import RequestHandler
from apiclient.model import Client


class BaseClientHandler(RequestHandler):
    def initialize(self):
        self.json_args = None

    def set_default_headers(self):
        """Set the default response header to be JSON."""
        self.set_header("Content-Type", 'application/json; charset="utf-8"')

    def send_response(self, data, status=200, to_json=True):
        """Construct and send a JSON response with appropriate status code."""
        self.set_status(status)
        if to_json:
            self.write(json.dumps(data, default=Client.client_serializer))
        else:
            self.write(data)

    def prepare(self):
        if self.request.body:
            self.json_args = json.loads(self.request.body, object_hook=Client.client_deserializer)


class ClientsHandler(BaseClientHandler):
    SUPPORTED_METHODS = ["GET", "POST"]

    async def get(self):
        clients = list(Client.find(lambda c: True))
        self.send_response(clients, 200)

    async def post(self):
        client = Client(**self.json_args)
        saved_client = Client.get(client.oid)
        if not saved_client:
            client.save()
            self.send_response(client, 201)
        else:
            self.send_response(saved_client, 409)


class ClientHandler(BaseClientHandler):
    SUPPORTED_METHODS = ["GET", "PUT", "DELETE"]

    async def put(self, id):
        client = Client(**self.json_args)
        saved_client = Client.get(id)
        if saved_client:
            saved_client.__merge__(client)
            saved_client.save()
            self.send_response(client, 200)
        else:
            self.send_response("{\"message\": \"Client not found!\"}", 404, False)

    async def get(self, id):
        saved_client = Client.get(id)
        if saved_client:
            self.send_response(saved_client, 200)
        else:
            self.send_response("{\"message\": \"Client not found!\"}", 404, False)

    async def delete(self, id):
        saved_client = Client.get(id)
        if saved_client:
            saved_client.remove()
            self.send_response(saved_client, 200)
        else:
            self.send_response("{\"message\": \"Client not found!\"}", 404, False)
