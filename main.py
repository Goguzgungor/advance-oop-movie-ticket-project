# This is a sample Python script.
from cinema import Cinema, CinemaHall
from constants import ManagerType
from dao.db import FakeNoSQLDB
from managers.movie_manager import MovieManager
from show import Show

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    db = FakeNoSQLDB()
    hall = CinemaHall("esenlerhall",123,12,"")
    cinema = Cinema("starwars","12","istanbul/esenler",)
    db.insertAll(ManagerType.CINEMA,{
    "name":"siperman"
    })
    print(db.get(ManagerType.CINEMA))
