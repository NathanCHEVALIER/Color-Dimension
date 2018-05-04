import pygame
import time
import pygame.locals

class Editor():
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fond = pygame.Surface((1520, 1080))
        self.fond.fill((240,240,240))
        self.menu = pygame.Surface((400, 1080))
        self.menu.fill((50,50,50))

        self.last = False

    def render(self):
        self.fenetre.blit(self.fond, (400,0))
        self.fenetre.blit(self.menu, (0,0))

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
