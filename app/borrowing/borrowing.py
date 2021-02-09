import datetime


class Borrowing:
    def __init__(
        self,
        member,
        book,
        date=datetime.date.today(),
        deadline=datetime.date.today() + datetime.timedelta(weeks=4),
    ):
        self.member = member
        self.book = book
        self.date = date
        self.deadline = deadline

    def __repr__(self):
        return f"{self.member.username}, {self.book.title}, {self.date}, {self.deadline}"