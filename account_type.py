from abc import ABC
from xmlrpc.client import Boolean

from booking import Booking
from dao.db import FakeNoSQLDB
from main import db
from show import Movie, Show
from .constants import AccountStatus, ManagerType


# For simplicity, we are not defining getter and setter functions. The reader can
# assume that all class attributes are private and accessed through their respective
# public getter methods and modified only through their public methods function.


class Account:
    def __init__(self, id, password, status=AccountStatus.Active):
        self.__id = id
        self.__password = password
        self.__status = status

    def reset_password(self, password):
        self.__password = password;
        return True


# from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name, address, email, phone, account):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__account = account

    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_email(self):
        return self.__email
    def get_phone(self):
        return self.__phone
class Customer(Person):
    def __init__(self, db:FakeNoSQLDB,person:Person):
        self.__db = db
        self.__person = person
    def make_booking(self, booking):
        self.__db.insertAll(ManagerType.BOOKING, booking)
        return True

    def get_bookings(self):
        return self.__db.get(ManagerType.BOOKING)

    def save_customer(self):
        self.__db.insert_all(ManagerType.CUSTOMER, self.__person)
        return True


class Admin(Person):
    def __init__(self,name,address,email,phone,account, data_base: FakeNoSQLDB):
        super().__init__(name, address, email, phone, account)
        self.data_base = data_base

    def add_movie(self, movie: Movie) -> Boolean:
        self.data_base.insertAll(ManagerType.MOVIE, movie)
        return True
    def add_show(self, show: Show):
        self.data_base.insertAll(ManagerType.SHOW, show)
        return True
    def block_user(self, customer: Customer)->Boolean:
        self.data_base.insertAll("blok", customer)
        return True


class FrontDeskOfficer(Person):
    def create_booking(self, booking:Booking):
        None


class Guest:
    def register_account(self,id,password) -> Account:
        return Account(password, id, AccountStatus.Active);
