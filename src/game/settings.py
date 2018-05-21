import pygame
class Settings:
    FPS = 30
    fullscreen = False

    def changeFullScreen(fenetre):
        if Settings.fullscreen == False:
            fenetre = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN | pygame.DOUBLEBUF)
            Settings.fullscreen = True
        else:
            fenetre = pygame.display.set_mode((1920, 1080))
            Settings.fullscreen = False