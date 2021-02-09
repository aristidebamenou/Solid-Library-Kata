from app.borrowing import Borrowing
from app.data import add_borrowing, borrowing_exits, borrowings_number, delete_borrowing

from .user import User


class Member(User):
    def __init__(self, username):
        super().__init__(username)

    def borrow_book(self, book):
        if borrowings_number(self) == 3:
            raise Exception("The user has already borrowed three books.")

        if borrowings_exits(self, book):
            raise Exception("The user has already borrowed this book")

        borrowing = Borrowing(self, book)
        add_borrowing(borrowing)

        return borrowing

    def return_book(self, book):
        if not borrowing_exits(self, book):
            raise Exception("This book is not borrowed.")

        delete_borrowing(self, book)
