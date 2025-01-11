import sys
import pygame
from const import *
from board import *
from piece import *

class GUI:

    def __init__(self):
        self.board = Board()

    def show_bg(self,surface):

        for rows in range(ROWS): # loops initalized for setting black or white colors
            for cols in range(COLS):
                if (rows + cols) % 2 == 0:
                    color = (234,235,200) #switch to white later
                else:
                    color = (119,154,88) #switch to black later

                rectang = (cols * SQUARES, rows * SQUARES, SQUARES , SQUARES)

                pygame.draw.rect(surface,color,rectang)

    def show_pieces(self, surface):
        for rows in range(ROWS): # loops initalized for setting black or white colors
            for cols in range(COLS):
                if self.board.squares[rows][cols].has_piece():
                    piece = self.board.squares[rows][cols]

                    img = pygame.image.load(piece.texture)
                    img_center = cols*Sqr+Sqr//2, rows * Sqr + Sqr//2
                    piece.texture_rect = img.get_rect(center = img_center)
                    surface.blit(img, piece.texture_rect)