import string
from typing import List

from constants import ManagerType
from dao.db import INoSQLDB
from show import Movie


class MovieManager:
    def __init__(self, db: INoSQLDB):
        self.db = db

    def add_movie(self, movie:Movie):
        self.db.insertAll(ManagerType.MOVIE,movie);


    def get_movies(self):
        self.db.get(ManagerType.MOVIE);



    def  get_movie_by_title(self, list:List[Movie] ,title:string):
        for movie in list:
            if movie.title == title:
                return movie;