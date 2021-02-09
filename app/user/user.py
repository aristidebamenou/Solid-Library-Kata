from app.data import get_all_books
from app.book import Book


class User:
    def __init__(self, username):
        self.username = username.capitalize()

    def __repr__(self):
        return f"{self.username}"

    def get_all_books(self):
        books = get_all_books()
        return [Book(book["title"], book["author"]) for book in books]

    def show_book(self):
        count = 0
        books = self.get_all_books()
        while count < len(books):
            if books[count]:
                print(f"{count+1}. {books[count]}")
                count = count + 1
