import pygame
import pygame.locals
import time

class GameOver():
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.image = {"GOpage" : pygame.image.load('../img/menu/GOpage.png')}
        self.image["GOmenu"] = pygame.image.load('../img/menu/GOmenu.png')
        self.image["GOrejouer"] = pygame.image.load('../img/menu/GOrejouer.png')


        self.rect = {"GOpage" : self.image["GOpage"].get_rect().move(685, 250)}
        self.rect["GOmenu"] = self.image["GOmenu"].get_rect().move(705, 740)
        self.rect["GOrejouer"] = self.image["GOrejouer"].get_rect().move(965, 740)
        self.last = False

    def run(self):
        r = 0
        while r == 0:
            r = self.update()
            self.render()
            time.sleep(1/30)
        return r

    def render(self):
        self.fenetre.blit(self.image["GOpage"], (685, 250))
        self.fenetre.blit(self.image["GOmenu"], (705, 740))
        self.fenetre.blit(self.image["GOrejouer"], (965,740))
        pygame.display.flip()

    def update(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "stop"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect["GOrejouer"].collidepoint(mouse):
                    return "respawn"
                elif self.rect["GOmenu"].collidepoint(mouse):
                    return "startmenu"

        return 0
