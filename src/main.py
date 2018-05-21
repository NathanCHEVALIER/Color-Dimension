import pygame
import game
from game.Game import *
from pygame.locals import *
from menu.StartMenu import *

class Main():
    """boucle principale du programme"""
    pygame.init()
    fenetre = pygame.display.set_mode((1920, 1080)) ##, pygame.FULLSCREEN)
    game = 0
    r = "startmenu"
    while r != "stop":
        if r == "start":
            game = Game(fenetre, "tower")
            game.respawn()
            r = game.run()
        elif r == "startmenu":
            startmenu = StartMenu(fenetre)
            r = startmenu.run()
        elif r == "respawn":
            game.respawn()
            r = game.run()
    pygame.quit()