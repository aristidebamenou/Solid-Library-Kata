#! /venv/bin python3
# coding: utf-8

from app.user import Guest, Member
from app.book import Book
from app.data import delete_borrowing
from app.borrowing import Borrowing


def main():

    choice = 0

    while choice != 2 and choice != 3:

        print("1. Voir les livres")
        print("2. Devenir membre")
        print("3. Quitter")

        choice = int(input("... "))

        if choice == 1:
            user = Guest("Invité")
            print(user.show_book())
        elif choice == 2:
            username = input("Entrez votre nom svp: ")
            user = Member(username)
            print("1. Voir les livres")
            print("1. Emprunter un livre")
            print("2. Rendre un livre")
        elif choice == 3:
            print("Fermeture...")
        else:
            print("Choix invalide")


if __name__ == "__main__":
    main()