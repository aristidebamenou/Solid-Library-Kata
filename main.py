#! /venv/bin python3
# coding: utf-8

from app.user import Guest, Member
from app.book import Book


def main():

    book = Book("Candide", "Jean Jacques Rousseau")

    member = Member("Sido")

    books = member.see_all_books()

    member.borrow_book(book)


if __name__ == "__main__":
    main()