from account_type import Account, Person, Customer
from booking import Booking, PaymentType
from constants import ManagerType, BookingStatus
from dao.db import FakeNoSQLDB
from notification import EmailNotification, SMSNotification
from search import Catalog
from show import Movie, Show

db = FakeNoSQLDB()
movie: list[Movie] = [
    Movie("Matrix", "matrix film description", "110", "En", "28.10.2000", "Turkey", "Science-Fiction", "admin"),
    Movie("Matrix2", "matrix film description", "110", "En", "28.10.2000", "Turkey", "Science-Fiction", "admin"),
    Movie("Matrix3", "matrix film description", "110", "En", "28.10.2000", "Turkey", "Science-Fiction", "admin"),
    Movie("Lord of the Rings", "lord of the rings film description", "110", "En", "28.10.2000", "Turkey",
          "Science-Fiction", "admin"),
    Movie("Harry Potter", "harry potter film description", "110", "En", "28.10.2000", "Turkey", "Science-Fiction",
          "admin"),
    Movie("Dark Knight", "dark knight film description", "110", "En", "28.10.2000", "Turkey", "Science-Fiction",
          "admin"),
    Movie("Inception", "inception film description", "110", "En", "28.10.2000", "Turkey", "Science-Fiction", "admin"),
    Movie("Interstellar", "interstellar film description", "110", "En", "28.10.2000", "Turkey", "Science-Fiction",
          "admin"),
    Movie("Prestige", "prestige film description", "110", "En", "28.10.2000", "Turkey", "Science-Fiction", "admin"),
    Movie("Batman Begins", "batman begins film description", "110", "En", "28.10.2000", "Turkey", "Science-Fiction",
          "admin"),
]
show: list[Show] = [
    Show(1, "28.10.2000", movie[1], "12:00", "14:00"),
    Show(2, "28.10.2000", movie[3], "14:00", "16:00"),
    Show(3, "28.10.2000", movie[2], "16:00", "18:00"),
    Show(4, "28.10.2000", movie[4], "18:00", "20:00"),
    Show(5, "28.10.2000", movie[5], "20:00", "22:00"),
    Show(6, "28.10.2000", movie[1], "22:00", "24:00"),
    Show(7, "28.10.2000", movie[3], "24:00", "02:00"),
    Show(8, "28.10.2000", movie[4], "02:00", "04:00"),
    Show(9, "28.10.2000", movie[1], "04:00", "06:00"),
    Show(10, "28.10.2000", movie[0], "06:00", "08:00"),
    Show(11, "28.10.2000", movie[5], "08:00", "10:00"),
    Show(12, "28.10.2000", movie[1], "10:00", "12:00"),
    Show(13, "28.10.2000", movie[3], "12:00", "14:00"),
    Show(14, "28.10.2000", movie[5], "14:00", "16:00"),
    Show(15, "28.10.2000", movie[1], "16:00", "18:00"),
    Show(16, "28.10.2000", movie[5], "18:00", "20:00"),
    Show(17, "28.10.2000", movie[3], "20:00", "22:00"),
    Show(18, "28.10.2000", movie[2], "22:00", "24:00"),
]
booking: list[Booking] = [
    Booking(1, 1, BookingStatus.REQUESTED, show[1], 1, PaymentType.CASH),
    Booking(2, 1, BookingStatus.REQUESTED, show[2], 1, PaymentType.CASH),
    Booking(3, 1, BookingStatus.REQUESTED, show[3], 1, PaymentType.CASH),

]
db.insert_all_base(ManagerType.BOOKING, booking)
db.insert_all_base(ManagerType.SHOW, show)
db.insert_all_base(ManagerType.MOVIE, movie)

title = input("Lütfen izlemek istediğiniz filmin ismini giriniz: ")

catalog = Catalog(db)
newMovie = catalog.search_by_title(title)

while newMovie == None:
    isFound = input("Aradığınız film ve tarih bulunamadı. Tekrar denemek ister misiniz? (E/H)")
    if isFound == "E":
        title = input("Lütfen izlemek istediğiniz filmin ismini giriniz: ")
        newMovie = catalog.search_by_title(title)
    else:
        break;

print("Film bulundu: " + newMovie.get_title())
print("Kayıt olmak için lütfen bilgilerinizi giriniz:")
mail = input("Email: ")
name = input("Password: ")

account = Account(mail, name);
person = Person(mail, "address", mail, "55555555", account)
customer: Customer = Customer(db, person)
print("Kayıt başarılı. Lütfen giriş yapınız.")
print("Giriş başarılı. Lütfen bilet sayısını giriniz.")
ticketCount = input("Bilet sayısı: ")
print("Ödeme tipini seçiniz.")
print("1- Kredi Kartı")
print("2- Nakit")
paymentType_str = input("Ödeme tipi: ")
paymentType = None
try:
    paymentType = PaymentType[paymentType_str.upper()]  # Assuming input is in uppercase
except KeyError:
    print("Geçersiz ödeme tipi.")
if paymentType != None:
    bookTicket: Booking = Booking(4, ticketCount, BookingStatus.REQUESTED, newMovie, 2, paymentType)
    customer.make_booking(bookTicket)
    bookTicket.make_payment(customer)
    print("Ödeme başarılı.")
    print("Biletiniz hazırlanıyor.")
    print("Biletiniz hazır.")
notification_type = input("Biletinizin size ulaşması için lütfen iletişim bilgilerinizi giriniz. (MAIL/SMS)")
if notification_type == "MAIL":
    notificationService = EmailNotification(1, "Mail gönderildi.", customer.get_email())
    notificationService.send_notification()
elif notification_type == "SMS":
    notificationService = SMSNotification(1, "Sms gönderildi.", customer.get_phone())
    notificationService.send_notification()
print("İyi seyirler.")

mail = input("Email: ")
booking_number = input("Booking Number: ")
booking: list[Booking] = db.get(ManagerType.BOOKING)

for element in booking:
    if element.get_booking_number() == int(booking_number):
        print("Biletiniz bulundu.")
        print("İptal etmek istiyor musunuz?")
        isCancel = input("E/H")
        if isCancel == "E":
            element.cancel()
            print("İptal edildi.")
            # iptal edilmiş hali sisteme yüklenir. STATUS = CANCELLED
            db.insert_all(ManagerType.BOOKING, booking)
            element.get_show().set_seats(element.get_show().get_seats() + element.get_number_of_seats())
            db.insert_all(ManagerType.SHOW, element.get_show())
        else:
            print("İptal edilmedi.")

notification_type = input("İptal faturanızı nasıl almak istersiniz? (MAIL/SMS)")
if notification_type == "MAIL":
    notificationService = EmailNotification(1, "Mail gönderildi.", customer.get_email())
    notificationService.send_notification()
elif notification_type == "SMS":
    notificationService = SMSNotification(1, "Sms gönderildi.", customer.get_phone())
    notificationService.send_notification()

