from apiclient.model import Client
from datetime import date
import unittest


class TestClient(unittest.TestCase):
    def test_save(self):
        client1 = Client("1", "Pai", "pai@test.com", date.today())
        client2 = Client("2", "Mae", "mae@test.com", date.today())
        saved_client1 = client1.save()
        saved_client2 = client2.save()
        self.assertEqual(client1, saved_client1, "It should be equal!")
        self.assertEqual(client2, saved_client2, "It should be equal!")

        clients = list(Client.find(lambda c: True))
        self.assertEquals(2, len(clients), "It should have 2 values!")
        self.assertEqual(clients[0], client1, "It should be equal!")
        self.assertEqual(clients[1], client2, "It should be equal!")

    def test_delete(self):
        client1 = Client("1", "Pai", "pai@test.com", date.today())
        client2 = Client("2", "Mae", "mae@test.com", date.today())
        client1.save()
        client2.save()

        clients = list(Client.find(lambda c: True))
        self.assertEquals(2, len(clients), "It should have 2 values!")

        client1.remove()
        clients = list(Client.find(lambda c: True))
        self.assertEquals(1, len(clients), "It should have one values!")
        self.assertEqual(clients[0], client2, "It should be equal!")

        client2.remove()
        clients = list(Client.find(lambda c: True))
        self.assertEquals(0, len(clients), "It should have zero values!")

    def test_find(self):
        client1 = Client("1", "Pai", "pai@test.com", date.today())
        client2 = Client("2", "Mae", "mae@test.com", date.today())
        client1.save()
        client2.save()

        clients = list(Client.find(lambda c: c.name == "Pai"))
        self.assertEquals(1, len(clients), "It should have one values!")
        self.assertEqual(clients[0], client1, "It should be equal!")

        clients = list(Client.find(lambda c: c.name == "Mae"))
        self.assertEquals(1, len(clients), "It should have one values!")
        self.assertEqual(clients[0], client2, "It should be equal!")

