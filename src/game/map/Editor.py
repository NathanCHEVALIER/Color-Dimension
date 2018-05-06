import pygame
import time
import pygame.locals

class Editor():
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fond = pygame.Surface((1920, 1080))
        self.fond.fill((50,50,50))
        self.image = {"sprite": 0}

        self.image["editeur"] =  pygame.image.load('../img/editeur/menu.png')
        self.image["zoneChoice"] = self.image["editeur"].subsurface(450, 0, 400, 500)
        self.image["mapChoice"] = self.image["editeur"].subsurface(850, 0, 400, 500)
        self.image["menu"] = self.image["editeur"].subsurface(0, 0, 400, 1080)
        self.rects = {"mapChoice": self.image["mapChoice"].get_rect().move((960, 220)), "zoneChoice": self.image["zoneChoice"].get_rect().move((460,220))}
        self.last = False
        self.home = True
        self.editing = False

    def loop(self):
        while self.updateSelect():
            self.renderSelect()
            while self.editing:
                while self.update():
                    self.render()

    def render(self):
        self.fenetre.blit(self.fond, (0,0))
        self.fenetre.blit(self.image["menu"], (0,0))

        pygame.display.flip()

    def update(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.editing = False
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                    print("GG WP")
        return True

    def renderSelect(self):
        self.fenetre.blit(self.fond, (0,0))
        self.fenetre.blit(self.image["zoneChoice"], (960,220))
        self.fenetre.blit(self.image["mapChoice"], (460,220))

        pygame.display.flip()

    def updateSelect(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rects["zoneChoice"].collidepoint(mouse):
                    self.editing = True
                if self.rects["mapChoice"].collidepoint(mouse):
                    self.editing = True
        return True
