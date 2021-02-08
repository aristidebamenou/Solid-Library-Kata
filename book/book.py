from data import book_list


class Book:
    def __init__(self, title: str, author: str):
        self.__title = title
        self.__author = author
        self.available = True
        book_list.append(self)

    def __repr__(self):
        return f"{self.__title}"

    def is_available(self) -> bool:
        return self.available