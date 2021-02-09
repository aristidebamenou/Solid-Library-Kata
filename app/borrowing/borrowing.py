import datetime


class Borrowing:
    def __init__(self, member: Member, book: Book):
        self.__member = member
        self.__book = book
        self.__borrowing_date = date.today()
        self.__deadline = self.__borrowing_date + datetime.timedelta(weeks=4)
