from apiclient.model import Client
from datetime import date
from tornado.testing import AsyncTestCase, gen_test


class TestClient(AsyncTestCase):
    @gen_test
    def test_save(self):
        client1 = Client("1", "Pai", "pai@test.com", date.today())
        client2 = Client("2", "Mae", "mae@test.com", date.today())
        saved_client1 = yield client1.save()
        saved_client2 = yield client2.save()
        self.assertEqual(client1, saved_client1, "It should be equal!")
        self.assertEqual(client2, saved_client2, "It should be equal!")

        clients = yield Client.find(lambda c: True)
        clients = list(clients)
        self.assertEqual(2, len(clients), "It should have 2 values!")
        self.assertEqual(clients[0], client1, "It should be equal!")
        self.assertEqual(clients[1], client2, "It should be equal!")

    @gen_test
    def test_remove(self):
        client1 = Client("1", "Pai", "pai@test.com", date.today())
        client2 = Client("2", "Mae", "mae@test.com", date.today())
        yield client1.save()
        yield client2.save()

        clients = yield Client.find(lambda c: True)
        clients = list(clients)
        self.assertEqual(2, len(clients), "It should have 2 values!")

        deleted_client1 = yield client1.remove()
        self.assertEqual(client1, deleted_client1[0], "It show be equal!")
        clients = yield Client.find(lambda c: True)
        clients = list(clients)
        self.assertEqual(1, len(clients), "It should have one values!")
        self.assertEqual(clients[0], client2, "It should be equal!")

        deleted_client2 = yield client2.remove()
        self.assertEqual(client2, deleted_client2[0], "It show be equal!")
        clients = yield Client.find(lambda c: True)
        clients = list(clients)
        self.assertEqual(0, len(clients), "It should have zero values!")

    @gen_test
    def test_find(self):
        client1 = Client("1", "Pai", "pai@test.com", date.today())
        client2 = Client("2", "Mae", "mae@test.com", date.today())
        yield client1.save()
        yield client2.save()

        clients = yield Client.find(lambda c: c.name == "Pai")
        clients = list(clients)
        self.assertEqual(1, len(clients), "It should have one values!")
        self.assertEqual(clients[0], client1, "It should be equal!")

        clients = yield Client.find(lambda c: c.name == "Mae")
        clients = list(clients)
        self.assertEqual(1, len(clients), "It should have one values!")
        self.assertEqual(clients[0], client2, "It should be equal!")
