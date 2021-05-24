#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""

class Capsule:

    def __init__(self):
        self.set_Minerals()
        self.set_Vitamins()

    def set_Minerals(self):
        self.mineral_K = True
        self.mineral_Fe = True
        self.mineral_Mg = True

    def set_Vitamins(self):
        self.vitamin_A = True
        self.vitamin_D = True
        self.vitamin_E = True
        self.vitamin_K = True

    def show_content(self):

        self.safe_execute('print("Mineral K: ", self.mineral_K)')
        self.safe_execute('print("Mineral Fe: ", self.mineral_Fe)')
        self.safe_execute('print("Mineral Mg: ", self.mineral_Mg)')
        self.safe_execute('print("Vitamin A: ", self.vitamin_A)')
        self.safe_execute('print("Vitamin D: ", self.vitamin_D)')
        self.safe_execute('print("Vitamin E: ", self.vitamin_E)')
        self.safe_execute('print("Vitamin K: ", self.vitamin_K)')

    def safe_execute(self, char):

        try:
            exec(char)
        except:
            pass

class Special_Capsule(Capsule):

    def set_Minerals(self):
        
        super(Special_Capsule, self).set_Minerals()
        
        self.mineral_Zn = True
        self.mineral_I = True

    def show_content(self):
        
        super(Special_Capsule, self).show_content()
        
        print("Mineral Zn", self.mineral_Zn)
        print("Mineral I", self.mineral_I)

    

if __name__ == '__main__':

    tablet = Special_Capsule()
    tablet.show_content()

