import datetime


class Borrowing:
    def __init__(self, member, book):
        self.member = member
        self.book = book
        self.date = datetime.date.today()
        self.deadline = self.date + datetime.timedelta(weeks=4)

    def __repr__(self):
        return f"{self.member.username}, {self.book.title}, {self.date}, {self.deadline}"