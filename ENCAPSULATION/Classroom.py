#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""

class Classroom:

    def __init__(self):
        self.__midterm = 0
        self.__final = 0
        self.__pass_status = ""

    def set_midterm(self, midterm):
        self.__midterm = midterm

    def set_final(self, final):
        self.__final = final

    def get_midterm(self):
        return self.__midterm

    def get_final(self):
        return self.__final

    def get_pass_status(self):
        self.__pass_status = self.pass_process()
        return self.__pass_status

    def pass_process(self):

        if self.__final < 35:
            return False

        else:
            if (self.__midterm + self.__final)/2 < 35:
                return False

            else:
                return True
