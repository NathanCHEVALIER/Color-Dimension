import json
import pygame
import pygame.locals

datascore = json.load(open('../data/scorelist.json'))
print(datascore['scores']['1'])
print(datascore['scores']['2'])
print(datascore['scores']['3'])

class Scores():
    def __init__(self, fenetre, main):
        self.fenetre = fenetre
        self.main = main
        self.image = {"title" : pygame.image.load('../img/menu/title2.png')}
        self.image["close"] = pygame.image.load('../img/menu/close.png')
        self.image["page"] = pygame.image.load('../img/menu/page.png')


        self.rect = {"title" : self.image["title"].get_rect().move(0, 0)}
        self.rect["close"] = self.image["close"].get_rect().move(1120, 340)
        self.rect["page"] = self.image["page"].get_rect().move(685, 400)

        self.last = False

    def render(self):
        self.fenetre.fill((255, 0, 255, 1))
        self.fenetre.fill((255, 0, 255, 1))
        self.fenetre.blit(self.image["title"], (0, 0))
        self.fenetre.blit(self.image["close"], (1120, 340))
        self.fenetre.blit(self.image["page"], (685, 400))

        pygame.display.flip()

    def update(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect["close"].collidepoint(mouse):
                    self.menu.StartMenu()


        return True

