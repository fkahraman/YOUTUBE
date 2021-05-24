#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""

globals()["value"] = int(input("Bir sayı giriniz: "))

def take_square():
    globals()["value"] **= 2
    print("Value: {}".format(globals()["value"]))

def turn_abs():
    globals()["value"] = abs(globals()["value"])
    print("Value: {}".format(globals()["value"]))

def take_root():
    globals()["value"] **= 0.5
    print("Value: {}".format(globals()["value"]))

def turn_negative():
    if globals()["value"] > 0:
        globals()["value"] *= -1

    else:
        pass

    print("Value: {}".format(globals()["value"]))

if __name__ == '__main__':

    take_square()
    turn_abs()
    take_root()
    turn_negative()