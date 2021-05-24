#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""
import random

class ColorPencil:

    def __init__(self):
        self.pencil_color = self.get_pencil_color()
        self.pencil_type = self.get_pencil_type()
        self.pencil_point = self.get_pencil_point()

        self.object_name = "object"
        self.object_counter = 0

    def get_veriable_name(self):
        veriable_name = self.object_name + '_' + str(self.object_counter)
        self.object_counter += 1
        return veriable_name

    def get_pencil_color(self):
        colors = ["red", "blue", "green", "yellow"]
        return random.choice(colors)

    def get_pencil_type(self):
        pencil_type = ["soft", "medium", "strong"]
        return random.choice(pencil_type)

    def get_pencil_point(self):
        soft = ["7B", "6B", "5B", "4B"]
        medium = ["B", "HB", "F", "H"]
        strong = ["4H", "5H", "6H", "7H"]

        if self.pencil_type == "soft":
            return random.choice(soft)

        elif self.pencil_type == "medium":
            return random.choice(medium)

        else:
            return random.choice(strong)

    def __str__(self):
        return "Pencil color {}\nPencil type {}\nPencil point {}".format(self.pencil_color, self.pencil_type, self.pencil_point)

if __name__ == '__main__':

    client_request = random.randint(3,5)
    object_name_list = []

    for i in range(client_request):
        pencil_dummy = ColorPencil()
        object_name_list.append(pencil_dummy.get_veriable_name())

    for content in object_name_list:
        globals()[content] = ColorPencil()
        print(globals()[content])
        print('-----')
