import pygame             ##importation des différents modules
import pygame.locals
import time
from game.map.Map import *


class ChoixMap():

    def __init__(self, fenetre):
        """Constructeur de Menu"""
        ##place et taille de la page, donné par fenetre
        self.fenetre = fenetre

        ##déclaration d'un style de texte, nommé text
        self.text = [pygame.font.Font('../font/impact.ttf', 54)]

        ##chargement des images
        self.image = {"title" : pygame.image.load('../img/menu/title2.png')}
        self.image["closecredit"] = pygame.image.load('../img/menu/closecredit.png')
        self.image["maps_place"] = pygame.image.load('../img/menu/maps_place.png')



        ##création et placements des images
        self.rect = {"title" : self.image["title"].get_rect().move(0, 0)}
        self.rect["closecredit"] = self.image["closecredit"].get_rect().move(1200, 380)
        self.rect["maps_place1"] = self.image["maps_place"].get_rect().move(810, 450)
        self.rect["maps_place2"] = self.image["maps_place"].get_rect().move(810, 545)
        self.rect["maps_place3"] = self.image["maps_place"].get_rect().move(810, 640)
        self.rect["maps_place4"] = self.image["maps_place"].get_rect().move(810, 735)
        self.rect["maps_place5"] = self.image["maps_place"].get_rect().move(810, 830)
        self.rect["maps_place6"] = self.image["maps_place"].get_rect().move(810, 925)



    def run(self):
        """fonction donnant la boucle qui actuallise la page 30 fois par seconde"""
        ##boucle appellant render() 30fois par seconde
        r = 0
        while r == 0:
            r = self.update()
            self.render()
            time.sleep(1/30)
        return r


    def render(self):
        """fonction appellée par run() donnant la place des éléments à actualliser"""
        self.fenetre.fill((255, 0, 255, 1))

        ##placement des images déclarées dans __init__()
        self.fenetre.blit(self.image["title"], (0, 0))
        self.fenetre.blit(self.image["closecredit"], (1200, 380))

        self.cpt = 0
        y_text = 450
        y_place = 450
        self.liste = Map.getMaps(False)
        for element in self.liste:
            self.fenetre.blit(self.image[('maps_place')], (810, y_place))
            text = self.text[0].render((self.liste[self.cpt]), 1, (242,242,242))
            self.fenetre.blit(text, (830, y_text))
            self.cpt += 1
            y_text += 98
            y_place += 95



        ##rafraichissement d'écran
        pygame.display.flip()

    def update(self):
        """fonction regroupant des évènements présents sur la page"""
        mouse = pygame.mouse.get_pos()                              ##on prend la position de la souris avec la variable mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "stop"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.rect["closecredit"].collidepoint(mouse):           ##si clic gauche et souris sur rectangle closecredit,
                        return "startmenu"                                     ##on retourne au menu
                    elif self.cpt == 0 and self.rect["maps_place1"].collidepoint(mouse):
                        game = Game(fenetre, self.liste[0])
                        game.respawn()
                    elif self.cpt == 1 and self.rect["maps_place2"].collidepoint(mouse):
                        game = Game(fenetre, self.liste[1])
                        game.respawn()
                    elif self.cpt == 2 and self.rect["maps_place3"].collidepoint(mouse):
                        game = Game(fenetre, self.liste[2])
                        game.respawn()
                    elif self.cpt == 3 and self.rect["maps_place4"].collidepoint(mouse):
                        game = Game(fenetre, self.liste[3])
                        game.respawn()
                    elif self.cpt == 4 and self.rect["maps_place5"].collidepoint(mouse):
                        game = Game(fenetre, self.liste[4])
                        game.respawn()
                    elif self.cpt == 5 and self.rect["maps_place6"].collidepoint(mouse):
                        game = Game(fenetre, self.liste[5])
                        game.respawn()
        return 0

