from data import book_list


class Book:
    def __init__(self, title: str, author: str):
        self.__title = title
        self.__author = author

    def __repr__(self):
        return f"{self.__title}"
