import os


def get_all_books():

    books = []

    cwd = os.getcwd()

    books_file = open(cwd + "/app/data/dataset/books.txt", "rt")

    while True:
        book = books_file.readline().split(",")
        if book[0] and book[1]:
            books.append(dict(title=book[0].strip(), author=book[1].strip()))
        else:
            break
    books_file.close()

    return books


get_all_books()