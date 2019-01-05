from apiclient.database import InMemoryStorage
import datetime
import re


class Client(InMemoryStorage):
    DB_NAME = "CLIENT"
    VALID_STATUS = {"active": 'ACTIVE', "inactive": 'Inactive', "deleted": 'Deleted'}

    def __init__(self, oid, name, email, birth_date):
        super().__init__()
        self.oid = oid
        self.name = name
        self.email = email
        self.birth_date = birth_date
        self.__status__ = Client.VALID_STATUS['active']

    @property
    def status(self):
        return self.__status__

    @status.setter
    def status(self, status):
        if status in Client.VALID_STATUS:
            self.__status__ = Client.VALID_STATUS[status]
        else:
            raise ValueError(f'Invalid Status {status} valid {Client.VALID_STATUS.keys()}')

    @classmethod
    def find(cls, criteria):
        return super().__find_obj__(cls.DB_NAME, criteria)

    @classmethod
    def get(cls, id):
        try:
            return next(iter(super().__find_obj__(cls.DB_NAME, lambda x: x.oid == id)))
        except StopIteration:
            return None

    def set_active(self):
        self.__status__ = Client.VALID_STATUS['active']

    def set_inactive(self):
        self.__status__ = Client.VALID_STATUS['inactive']

    def set_deleted(self):
        self.__status__ = Client.VALID_STATUS['deleted']

    def save(self):
        return super().__save_obj__(Client.DB_NAME, self,
                                    lambda x: x.oid == self.oid)

    def remove(self):
        return super().__remove_obj__(Client.DB_NAME, lambda x: x.oid == self.oid)

    def __repr__(self):
        return f"Client [{self.oid}, {self.name}, {self.email}, {self.birth_date}, {self.status}]"

    def __merge__(self, other):
        self.oid = other.oid
        self.name = other.name
        self.email = other.email
        self.__status__ = other.__status__
        self.birth_date = other.birth_date

    @classmethod
    def client_serializer(cls, data):
        if type(data) == datetime.datetime:
            return data.strftime('%Y-%m-%d')
        elif type(data) == Client:
            return {
                "oid": data.oid,
                "name": data.name,
                "email": data.email,
                "birth_date": data.birth_date,
                "status": data.status
            }
        else:
            raise ValueError(f"Invalid type {type(data)}!")

    @classmethod
    def client_deserializer(cls, client_dict):
        for (key, value) in client_dict.items():
            try:
                if re.match(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', value):
                    client_dict[key] = datetime.datetime.strptime(value, "%Y-%m-%d")
            except BaseException as e:
                print(e)
        return client_dict


InMemoryStorage.__db__[Client.DB_NAME] = []

