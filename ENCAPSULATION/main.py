#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""

from Classroom import Classroom

if __name__ == '__main__':

    student_1 = Classroom()
    student_2 = Classroom()

    student_1.set_midterm(50)
    student_1.set_final(30)

    student_2.set_midterm(10)
    student_2.set_final(90)

    print(student_1.get_pass_status())
    print(student_2.get_pass_status())

    student_1.__final = 35
    print(student_1.get_pass_status())