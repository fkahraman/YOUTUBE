#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""

from abc import ABC, abstractmethod

class ChessPieces(ABC):

    @abstractmethod
    def show_move(self):
        pass

    @abstractmethod
    def show_count_in_board(self):
        pass

class Knight(ChessPieces):
    def show_move(self):
        print("L şeklinde gider.")

    def show_count_in_board(self):
        print("4 tane bulunur.")

class Bishop(ChessPieces):
    def show_move(self):
        print("Çapraz gider.")

    def show_count_in_board(self):
        print("4 tane bulunur.")

class Rook(ChessPieces):
    def show_move(self):
        print("Dikey ve yatay gider.")

    def show_count_in_board(self):
        print("4 tane bulunur.")

class Pawn(ChessPieces):
    def show_move(self):
        print("Düz gider.")

    def show_count_in_board(self):
        print("16 tane bulunur.")

    def show_special_skill(self):
        print("Vezire dönüşür.")

if __name__ == '__main__':

    knigh = Knight()
    bishop = Bishop()
    rook = Rook()
    pawn = Pawn()

    knigh.show_move()
    bishop.show_move()
    rook.show_count_in_board()
    pawn.show_count_in_board()

    pawn.show_special_skill()