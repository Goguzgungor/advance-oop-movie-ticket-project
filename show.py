from datetime import datetime


class Movie:
    def __init__(self, title, description, duration_in_mins, language, release_date, country, genre, added_by):
        self.__title = title
        self.__description = description
        self.__duration_in_mins = duration_in_mins
        self.__language = language
        self.__release_date = release_date
        self.__country = country
        self.__genre = genre
        self.__movie_added_by = added_by

        self.__shows = []

    def get_shows(self):
        return self.__shows

    def add_show(self, show):
        self.__shows.append(show)

    def get_title(self):
        return self.__title

    def get_lang(self):
        return self.__language

    def get_genre(self):
        return self.__genre

    def get_release_date(self):
        return self.__release_date

    def get_country(self):
        return self.__country


class Show:
    def __init__(self, id, played_at, movie: Movie, start_time, end_time):
        self.__show_id = id
        self.__created_on = datetime.date
        self.__start_time = start_time
        self.__end_time = end_time
        self.__played_at = played_at
        self.__movie = movie

    def get_movie(self):
        return self.__movie

    def get_show_id(self):
        return self.__show_id

    def get_start_time(self):
        return self.__start_time

    def get_end_time(self):
        return self.__end_time

    def get_played_at(self):
        return self.__played_at

    def get_created_on(self):
        return self.__created_on
