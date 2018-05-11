import pygame
from game.Game import *
from pygame.locals import *
from menu.StartMenu import *

class Main():
    pygame.init()
    fenetre = pygame.display.set_mode((1920, 1080))
    game = Game(fenetre, "tower")

    r = "startmenu"
    while r != "stop":
        if r == "start":
            r = game.run()
        elif r == "startmenu":
            startmenu = StartMenu(fenetre)
            r = startmenu.run()
        elif r == "respawn":
            game.respawn()
            r = game.run()
    pygame.quit()