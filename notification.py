from abc import ABC
from datetime import datetime

from account_type import  Customer


class Notification(ABC):
    def __init__(self, id, content):
        self.__notification_id = id
        self.__created_on = datetime.today()
        self.__content = content

    def send_notification(self): pass


    def get_content(self):
        return self.__content


class EmailNotification(Notification):
    def __init__(self, id, content, email_id):
        super().__init__(id, content)
        self.__email_id = email_id

    def send_notification(self):
        print("sending email to " + self.__email_id)


class SMSNotification(Notification):
    def __init__(self, id, content, phone_number):
        super().__init__(id, content)
        self.__phone_number = phone_number

    def send_notification(self,):
        print(self.get_content() + " to " + self.__phone_number)
