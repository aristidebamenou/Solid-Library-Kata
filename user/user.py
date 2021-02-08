from data import book_list


class User:
    def __init__(self, username: str):
        self.__username = username

    def __repr__(self):
        return f"{self.__username}"

    def see_all_books(self):
        return book_list
