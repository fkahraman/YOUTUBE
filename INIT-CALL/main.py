#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""

class Book:

    def __init__(self, page_count, author, book_type):
        self.page_count = page_count
        self.author = author
        self.book_type = book_type
        self.book_shape = "Dikdörtgen"

    def print_book_info(self):
        print("Sayfa sayısı: ",self.page_count)
        print("Yazar: ", self.author)
        print("Kitap tipi: ", self.book_type)
        print("Kitap şekli: ", self.book_shape)

    def __str__(self):
        return "Kitabın adı: {}".format(self.book_name)

    def __call__(self, *args, **kwargs):
        self.book_name = args[0]

if __name__ == '__main__':

    book = Book(200, "Selim Tuna", "Roman")
    book.print_book_info()

    book("Python Günlükleri")

    print(book)




