import pygame
import pygame.locals
import time
from menu.Scores import *
from menu.Options import *
from game.map.Editor import *

class Mur():
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.image = {"leila" : pygame.image.load('../img/leila.png'), "gauche" : {}, "droite" : pygame.image.load('../img/licorne_droite/out0.png')}
        self.image["droite"] = pygame.transform.scale(self.image["droite"], (100, 150))
        self.image["leila"] = pygame.transform.scale(self.image["leila"], (100, 150))


        for i in range(0, 30):
            self.image["gauche"][i] = pygame.image.load('../img/licorne_gauche/out' + str(i) + '.png')
            self.image["gauche"][i] = pygame.transform.scale(self.image["gauche"][i], (100, 150))

        self.t = 0
        self.steep = 0

    def run(self):
        self.t = 0
        while self.t <= 60:
            self.t = self.t + 1
            self.render()
            time.sleep(1/30)

        self.fenetre.fill((255, 255, 0, 1))
        self.fenetre.blit(self.image["droite"], (1220, 500))
        pygame.draw.rect(self.fenetre, (255, 0, 0), pygame.Rect(1300, 500, 100, 1000))
        pygame.display.flip()
        time.sleep(1)

        while self.t > 0:
            self.t = self.t - 1
            self.render2()
            time.sleep(1/30)
        return "startmenu"

    def render(self):
        self.fenetre.fill((255, 255, 0, 1))
        self.fenetre.blit(self.image["leila"], (self.t * 20, 500))
        pygame.draw.rect(self.fenetre, (255, 0, 0), pygame.Rect(1300, 500, 100, 1000))

        pygame.display.flip()

    def render2(self):
        self.fenetre.fill((255, 255, 0, 1))
        self.steep = (self.steep + 1) % 30
        self.fenetre.blit(self.image["gauche"][self.steep], (self.t * 20, 500))
        pygame.draw.rect(self.fenetre, (255, 0, 0), pygame.Rect(1300, 500, 100, 1000))
        pygame.display.flip()

