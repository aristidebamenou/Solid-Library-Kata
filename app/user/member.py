from .user import User
from app.data import add_borrowing, borrowings_number
from app.borrowing import Borrowing


class Member(User):
    def __init__(self, username):
        super().__init__(username)

    def borrow_book(self, book):
        if borrowings_number(self) == 3:
            raise Exception("The user has already borrowed three books.")

        borrowing = Borrowing(self, book)
        add_borrowing(borrowing)

        return borrowing

    """

    def return_book(self, book: Book):
        if book not in self.book_borrowed:
            raise Exception("This book is not borrowed.")

        self.book_borrowed.pop(self.book_borrowed.index(book))
        book.available = True
    """