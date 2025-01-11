import sys
import pygame
from const import *
from gui import GUI

class Main:

    def __init__(self): #initializing the display
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = GUI()

    def mainloop(self):

        screen = self.screen
        game = self.game

        while True:

            game.show_bg(screen)
            game.show_pieces(screen)
            for event in pygame.event.get():    # initializing the quit function
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
            

            pygame.display.update()

main = Main()

main.mainloop()