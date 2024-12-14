import sys
import pygame
from const import *

class GUI:

    def __init__(self):
        pass

    def show_bg(self,surface):

        for rows in range(ROWS):
            for cols in range(COLS):
                if (rows + cols) % 2 == 0:
                    color = (234,235,200) #switch to white later
                else:
                    color = (119,154,88) #switch to black later

                rectang = (cols * SQUARES, rows * SQUARES, SQUARES , SQUARES)

                pygame.draw.rect(surface,color,rectang)