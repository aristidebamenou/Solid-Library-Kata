from .user import User


class Member(User):
    def __init__(self, username):
        super().__init__(username)

        self.book_borrowed = []

    def borrow_book(self, book: Book):
        if len(self.book_borrowed) == 3:
            raise Exception("The user has already borrowed three books.")

        if not book.available:
            raise Exception("This book is not available.")

        book.available = False
        self.book_borrowed.append(book)

    def return_book(self, book: Book):
        if book not in self.book_borrowed:
            raise Exception("This book is not borrowed.")

        self.book_borrowed.pop(self.book_borrowed.index(book))
        book.available = True
