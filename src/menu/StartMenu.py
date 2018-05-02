import pygame
import pygame.locals

class StartMenu():
    def __init__(self, fenetre, main):
        self.fenetre = fenetre
        self.main = main
        self.image = {"option" : pygame.image.load('../img/menu/option.png')}
        self.image["play"] = pygame.image.load('../img/menu/play.png')
        self.rect = {"option" : self.image["option"].get_rect().move(500, 400)}
        self.rect["play"] = self.image["play"].get_rect().move(500, 300)


        #self.rect = {"option" : pygame.Rect(500, 400)}
        self.last = False

    def render(self):
        self.fenetre.fill((255, 0, 255, 1))
        self.fenetre.blit(self.image["play"], (500, 300))
        self.fenetre.blit(self.image["option"], (500, 400))



        pygame.display.flip()

    def update(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect["option"].collidepoint(mouse):
                    print("GG WP")
                elif self.rect["play"].collidepoint(mouse):
                    self.main.game.respawn()
        return True