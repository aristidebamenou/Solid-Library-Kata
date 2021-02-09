import os

path = os.getcwd() + "/app/data/dataset/"


def get_all_books():

    books = []

    books_file = open(path + "books.txt", "rt")

    while True:
        book = books_file.readline().split(",")
        if book[0] and book[1]:
            books.append(dict(title=book[0].strip(), author=book[1].strip()))
        else:
            break

    books_file.close()

    return books


def add_borrowing(borrowing):

    borrowings_file = open(path + "borrowings.txt", "at")

    borrowings_file.write(
        f"{borrowing.member.username}, {borrowing.book.title}, {borrowing.date}, {borrowing.deadline}\n"
    )

    borrowings_file.close()


def borrowings_number(member):

    count = 0

    borrowings_file = open(path + "borrowings.txt", "rt")

    while True:
        borrowing = borrowings_file.readline().split(",")
        if len(borrowing) == 4:
            if borrowing[0] == member.username:
                count = count + 1
        else:
            break

    borrowings_file.close()

    return count
