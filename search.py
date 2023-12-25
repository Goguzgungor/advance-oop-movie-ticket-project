from abc import ABC

from constants import ManagerType
from dao.db import INoSQLDB, FakeNoSQLDB
from show import Movie, Show


class Search(ABC):
    def search_by_title(self, title):
        None
    def search_by_language(self, language):
        None

    def search_by_genre(self, genre):
        None

    def search_by_release_date(self, rel_date):
        None

    def search_by_city(self, city_name):
        None


class Catalog(Search):
    def __init__(self, db: FakeNoSQLDB):
        self.db = db
        self.__movie_titles = {}
        self.__movie_languages = {}
        self.__movie_genres = {}
        self.__movie_release_dates = {}
        self.__movie_cities = {}

    def search_by_title(self, title):
        print("searching by title")
        movie_list : list[Show] = self.db.get(ManagerType.SHOW)
        for movie in movie_list:
            if movie.get_movie().get_title() == title:
                return movie

    def search_by_language(self, language):
        movie_list: list[Show] = self.db.get(ManagerType.SHOW)
        for movie in movie_list:
            if movie.get_movie().get_lang() == language:
                return movie

    def search_by_genre(self, genre):
        movie_list = self.db.get(ManagerType.MOVIE)
        for element in movie_list:
            movie: Movie = element
            if movie.get_genre() == genre:
                return movie

    def search_by_release_date(self, rel_date):
        movie_list = self.db.get(ManagerType.MOVIE)
        for element in movie_list:
            movie: Movie = element
            if movie.get_release_date() == rel_date:
                return movie

    def search_by_city(self, city_name):
        movie_list = self.db.get(ManagerType.MOVIE)
        for element in movie_list:
            movie: Movie = element
            if movie.get_country() == city_name:
                return movie

