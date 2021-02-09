class Member(User):
    def __init__(self, username):
        super().__init__(username)

    def borrow_book(self, book: Book):
        if len(self.book_borrowed) == 3:
            raise Exception("The user has already borrowed three books.")

        self.book_borrowed.append(book)

    def return_book(self, book: Book):
        if book not in self.book_borrowed:
            raise Exception("This book is not borrowed.")

        self.book_borrowed.pop(self.book_borrowed.index(book))
        book.available = True
