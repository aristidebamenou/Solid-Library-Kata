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

    borrowings_file.write(f"{str(borrowing)}\n")

    borrowings_file.close()


def delete_borrowing(member, book):

    borrowings_file = open(path + "borrowings.txt", "rt")

    borrowing_lines = borrowings_file.readlines()

    borrowings_file.close()

    borrowings_file = open(path + "borrowings.txt", "wt")

    for line in borrowing_lines:
        borrowing = line.split(",")
        if borrowing[0].strip() != member.username and book.title != borrowing[1].strip():
            borrowings_file.write(line)

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


def borrowing_exits(member, book):

    borrowings_file = open(path + "borrowings.txt", "rt")

    while True:
        borrowing = borrowings_file.readline().split(",")
        if len(borrowing) == 4:
            if borrowing[0] == member.username and borrowing[1] == book.title:
                return True
        else:
            break

    return False
