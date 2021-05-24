#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""

import googletrans
from googletrans import Translator


def translate(text, german=False, french=False, turkish=False):

    translation_dict = {}

    tranlator = Translator()

    if german==True:
        result = tranlator.translate(text, dest='de')
        translation_dict["Almanca"] = result.text

    if french==True:
        result = tranlator.translate(text, dest='fr')
        translation_dict["Fransızca"] = result.text

    if turkish==True:
        result = tranlator.translate(text, dest='tr')
        translation_dict["Türkçe"] = result.text


    return translation_dict

if __name__ == '__main__':

    text = 'Hello, My name is Fatih.'
    result = translate(text, french=True, german=True)

    for language in result.items():
        print(language)