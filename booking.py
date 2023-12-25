from abc import ABC
from datetime import datetime
from enum import Enum

from cinema import CinemaHallSeat
from constants import PaymentStatus, BookingStatus
from show import Show




class PaymentType(Enum):
    CASH = 1
    CARD = 2


class ShowSeat(CinemaHallSeat):
    def __init__(self, id, is_reserved, price):
        self.__show_seat_id = id
        self.__is_reserved = is_reserved
        self.__price = price


class Payment(ABC):
    def __init__(self, amount, transaction_id, payment_status:PaymentStatus):
        self.__amount = amount
        self.__created_on = datetime.today()
        self.__transaction_id = transaction_id
        self.__status = payment_status

    def make_payment(self, amount):pass

    def set_payment_status(self, status:PaymentStatus):
        self.__status = status;
        return True

class CreditCardTransaction(Payment):
    def __init__(self, amount, transaction_id, payment_status, name_on_card):
        super().__init__(amount, transaction_id, payment_status)
        self.__name_on_card = name_on_card

    def make_payment(self, amount):
        self.set_payment_status(PaymentStatus.COMPLETED)
        return True

class CashTransaction(Payment):
    def __init__(self, amount, transaction_id, payment_status, cash_tendered):
        super().__init__(amount, transaction_id, payment_status)
        self.__cash_tendered = cash_tendered

    def make_payment(self, amount):
        self.set_payment_status(PaymentStatus.COMPLETED)
        return True

class Booking:
    def __init__(self, booking_number, number_of_seats, status:BookingStatus, show:Show, show_seats,payment_tpye:PaymentType):
        self.__booking_number = booking_number
        self.__number_of_seats = number_of_seats
        self.__created_on = datetime.today()
        self.__status = status
        self.__show = show
        self.__seats = show_seats
        self.__payment_type = payment_tpye

    def get_booking_number(self):
        return self.__booking_number

    def get_number_of_seats(self):
        return self.__number_of_seats

    def get_created_on(self):
        return self.__created_on

    def get_status(self):
        return self.__status

    def get_show(self):
        return self.__show

    def get_seats(self):
        return self.__seats

    def get_payment_type(self):
        return self.__payment_type

    def set_status(self, status:BookingStatus):
        self.__status = status
        return True

    def make_payment(self,user):
        if(self.__payment_type == PaymentType.CASH):
            self.__payment = CashTransaction(self.__show.get_price(), "123", PaymentStatus.PENDING, 100)
        elif(self.__payment_type == PaymentType.CARD):
            self.__payment = CreditCardTransaction(self.__show.get_price(), "123", PaymentStatus.PENDING, user)
        self.__status = PaymentStatus.COMPLETED
        return True

    def cancel(self):
        self.__status = PaymentStatus.CANCELLED
        return True

    def assign_seats(self, seats):
        None
