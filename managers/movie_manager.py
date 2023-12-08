from dao.db import INoSQLDB


class MovieManager:
    def __init__(self, db: INoSQLDB):
        self.db = db

    def add_movie(self, key, value):
        self.db.insert("movie",key, value)
        data = self.db.get(key)
        print(data)

    def get_movies(self, key):
        return self.db.get(key);

