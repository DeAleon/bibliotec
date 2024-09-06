"""
План проекта Библиотека:
Создание класса Book

Атрибуты: название, автор, ISBN, доступность, жанр, год издания.
Методы: конструктор, строковое представление, метод для проверки доступности книги.
Создание класса User

Атрибуты: имя, список взятых книг, дата регистрации.
Методы: конструктор, добавление книги, возврат книги, проверка наличия книги у пользователя.
Создание класса Library

Атрибуты: список книг, список пользователей.
Методы: добавление книги, удаление книги, выдача книги пользователю, возврат книги от пользователя, поиск книги по ISBN, поиск книги по автору, поиск книги по жанру, вывод списка всех книг, вывод списка всех пользователей.
Создание основного скрипта

Создание экземпляров классов.
Демонстрация работы библиотеки (добавление книг, выдача книг пользователям, возврат книг, поиск книг, вывод списков).

Ну можно попробовать сделать именно как учет книг. Есть допустим много файлов с жанрами книг

Которые как будто полки

И например при выборе жанра такого то, открывать файл и т.д
"""
import os


class Book:
    def __init__(self, name, author, isbn, genre, year_public):
        self.access = True
        self.name = name
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.year_public = year_public

    def __check_book(self, line):
        count = 0
        name, author, isbn, genre, year_public = line.split(',')
        if self.name == name and author:
            count += 1
            print(f'Данная книга: {self.name} автор: {self.author} уже есть в библиотеке')
            return count

    def __add_book(self, file):
        file.write(f'{self.name}, {self.author}, {self.isbn}, {self.genre}, {self.year_public}\n')

    def add_book(self):
        if self.genre == 'роман':
            with open('novel.txt', 'r+', encoding='utf-8') as file:
                if os.stat("novel.txt").st_size == 0:
                    self.__add_book(file)
                count = 0
                for line in file:
                    if self.__check_book(line) == 1:
                        count += 1
                if count == 0:
                    self.__add_book(file)
        elif self.genre == 'фэнтези':
            with open('fantasy.txt', 'r+', encoding='utf-8') as file:
                if os.stat("fantasy.txt").st_size == 0:
                    self.__add_book(file)
                count = 0
                for line in file:
                    if self.__check_book(line) == 1:
                        count += 1
                if count == 0:
                    self.__add_book(file)
        else:
            with open('all_genre.txt', 'r+', encoding='utf-8') as file:
                if os.stat("all_genre.txt").st_size == 0:
                    self.__add_book(file)
                count = 0
                for line in file:
                    if self.__check_book(line) == 1:
                        count += 1
                if count == 0:
                    self.__add_book(file)


book = Book("Питон для чай", 'Константин В', 1234567890, 'учеба', 2024)
book.add_book()
