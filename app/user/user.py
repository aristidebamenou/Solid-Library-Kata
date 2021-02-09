from app.data import get_all_books


class User:
    def __init__(self, username: str):
        self.username = username

    def __repr__(self):
        return f"{self.username}"

    def see_all_books(self):
        return get_all_books()
