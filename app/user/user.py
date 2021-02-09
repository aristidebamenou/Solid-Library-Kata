from app.data import get_all_books
from app.book import Book


class User:
    def __init__(self, username: str):
        self.username = username

    def __repr__(self):
        return f"{self.username}"

    def get_all_books(self):
        books = get_all_books()
        return [Book(book["title"], book["author"]) for book in books]
