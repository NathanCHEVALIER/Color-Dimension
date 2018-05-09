import pygame
import pygame.locals
import time

class Pause():
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.image = {"pausepage" : pygame.image.load('../img/menu/pausepage.png')}
        self.image["pausereprendre"] = pygame.image.load('../img/menu/pausereprendre.png')
        self.image["pausemenu"] = pygame.image.load('../img/menu/pausemenu.png')

        self.rect = {"pausepage" : self.image["pausepage"].get_rect().move(685, 200)}
        self.rect["pausereprendre"] = self.image["pausereprendre"].get_rect().move(785, 580)
        self.rect["pausemenu"] = self.image["pausemenu"].get_rect().move(785, 700)

        self.last = False

    def run(self):
        r = 0
        while r == 0:
            r = self.update()
            self.render()
            time.sleep(1/30)
        return r

    def render(self):
        self.fenetre.blit(self.image["pausepage"], (685, 300))
        self.fenetre.blit(self.image["pausereprendre"], (785, 580))
        self.fenetre.blit(self.image["pausemenu"], (785,700))
        pygame.display.flip()

    def update(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "stop"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect["pausereprendre"].collidepoint(mouse):
                    return "reprendre"
                elif self.rect["pausemenu"].collidepoint(mouse):
                    return "startmenu"

        return 0
