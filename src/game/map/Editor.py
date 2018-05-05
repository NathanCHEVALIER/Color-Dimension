import pygame
import time
import pygame.locals

class Editor():
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fond = pygame.Surface((1520, 1080))
        self.fond.fill((240,240,240))
        self.image = {"sprite": 0}
        self.rects = {"menu": 0}

        self.image["menu"] =  pygame.image.load('../img/editeur/menu.png')
        self.last = False
        self.home = True

    def render(self):
        self.fenetre.blit(self.fond, (400,0))
        self.fenetre.blit(self.image["menu"], (0,0))

        pygame.display.flip()

    def update(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                ##if self.rect["option"].collidepoint(mouse):
                    print("GG WP")
                ##elif self.rect["play"].collidepoint(mouse):
                  ##  self.main.game.respawn()
        return True

    def loop(self):
        while self.update():
            self.render()
