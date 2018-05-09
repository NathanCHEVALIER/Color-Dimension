import pygame
import pygame.locals
import time
from menu.Scores import *
from menu.Options import *
from game.map.Editor import *

class StartMenu():
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.image = {"title" : pygame.image.load('../img/menu/title2.png')}
        self.image["play"] = pygame.image.load('../img/menu/play.png')
        self.image["score"] = pygame.image.load('../img/menu/score.png')
        self.image["option"] = pygame.image.load('../img/menu/option.png')
        self.image["edit"] = pygame.image.load('../img/menu/edit.png')

        self.rect = {"title" : self.image["title"].get_rect().move(0, 0)}
        self.rect["play"] = self.image["play"].get_rect().move(805, 445)
        self.rect["score"] = self.image["score"].get_rect().move(805, 587)
        self.rect["option"] = self.image["option"].get_rect().move(805, 729)
        self.rect["edit"] = self.image["edit"].get_rect().move(805, 871)

        #self.rect = {"option" : pygame.Rect(500, 400)}
        self.last = False

    def run(self):
        r = 0
        while r == 0:
            r = self.update()
            self.render()
            time.sleep(1/30)
        return r


    def render(self):
        self.fenetre.fill((255, 0, 255, 1))
        self.fenetre.blit(self.image["title"], (0, 0))
        self.fenetre.blit(self.image["play"], (805, 445))
        self.fenetre.blit(self.image["score"], (805, 587))
        self.fenetre.blit(self.image["option"], (805, 729))
        self.fenetre.blit(self.image["edit"], (805, 871))

        pygame.display.flip()

    def update(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "stop"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect["play"].collidepoint(mouse):
                    return "respawn"
                elif self.rect["score"].collidepoint(mouse):
                    score = Scores(self.fenetre)
                    r = score.run()
                    if r == "close":
                        return 0
                    else:
                        return r
                elif self.rect["option"].collidepoint(mouse):
                    option = Options(self.fenetre)
                    r = option.run()
                    if r == "close":
                        return 0
                    else:
                        return r
                elif self.rect["edit"].collidepoint(mouse):
                    editeur = Editor(self.fenetre)
                    editeur.loop()
        return 0

