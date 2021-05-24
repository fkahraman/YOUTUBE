#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""

import random

class Numbers:

    def __init__(self):

        self.numbers = []
        self.number_count = 25
        self.set_numbers()

    def get_numbers(self):
        return self.numbers

    def set_numbers(self):

        for i in range(self.number_count):
            self.numbers.append(random.randint(0,100))

    def show_numbers(self):
        print(self.numbers)

    def get_min_value(self):
        return min(self.numbers)

    def get_max_value(self):
        return max(self.numbers)

    def get_unique_list(self):
        return list(set(self.numbers))

    def my_filter(self, char):

        if char < 50:
            return False

        else:
            return True


if __name__ == '__main__':

    numbers = Numbers()
    numbers.show_numbers()

    print("Listenin minimum değeri: ", numbers.get_min_value())
    print("Listenin maksimum değeri: ", numbers.get_max_value())

    print("Benzersiz liste: ", numbers.get_unique_list())
    print("Benzersiz liste uzunluğu", len(numbers.get_unique_list()))

    filter_list = filter(numbers.my_filter, numbers.get_numbers())
    print("Filtrelenmiş liste: ", list(filter_list))
