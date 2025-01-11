from const import *
from square import Sqr
from piece import *

class Board:

    def __init__(self):
        self.squares = [[0,0,0,0,0,0,0,0] for cols in range (COLS)] # list for no of places

        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def _create(self):

        for rows in range(ROWS): # initializing the loop
            for cols in range(COLS):
                self.squares[rows][cols] = Sqr(rows, cols)

    def _add_pieces(self,color):
        if color == 'white':
            row_pawn, row_other = (6,7)
        else:
            row_pawn,row_other = (1,0)
        
        for col in range(COLS):
            self.squares[row_pawn][col] = Sqr(row_pawn, col, Pawn(color))

        self.squares[row_other][1] = Sqr(row_other, 1, Knight(color))
        self.squares[row_other][6] = Sqr(row_other, 6, Knight(color))

        self.squares[row_other][2] = Sqr(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Sqr(row_other, 5, Bishop(color))

        self.squares[row_other][0] = Sqr(row_other, 0, Rook(color))
        self.squares[row_other][7] = Sqr(row_other, 7, Rook(color))
        
        self.squares[row_other][3] = Sqr(row_other, 3, Queen(color))

        self.squares[row_other][4] = Sqr(row_other, 4, King(color))
Board()._create()