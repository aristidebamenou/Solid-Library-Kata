#! /venv/bin python3
# coding: utf-8

from app.user import Guest, Member
from app.book import Book
from app.data import delete_borrowing
from app.borrowing import Borrowing


def main():

    book = Book("Candide", "Jean Jacques Rousseau")

    member = Member("Sido")

    print(member.see_all_books())


if __name__ == "__main__":
    main()