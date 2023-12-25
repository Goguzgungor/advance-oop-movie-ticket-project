# Define an interface for the NoSQL database
class INoSQLDB:
    def insert(self, table, key, value): pass

    def get(self, key): pass

    def delete(self, key): pass

    def insert_all(self, key, map): pass

    def update(self, key, value): pass


class FakeNoSQLDB(INoSQLDB):
    def __init__(self):
        self.data = {}

    def insert(self, table, key, value):
        self.data[table] = {key: value}

    def get(self, key):
        return self.data.get(key)

    def delete(self, key):
        if key in self.data:
            del self.data[key]

    def insert_all_base(self, key, map):
        self.data[key] = map

    def insert_all(self, key, map):
        list = self.data.get(key);
        if list is None:
            list = []
        list.append(map);
        self.data[key] = list;
