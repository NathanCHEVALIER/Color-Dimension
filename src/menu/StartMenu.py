import pygame             ##importation des différents modules
import pygame.locals
import time
from menu.Scores import *
from menu.Options import *
from menu.Mur import *
from game.map.Editor import *

class StartMenu():

    def __init__(self, fenetre):
        """Constructeur de Menu"""
        ##place et taille de la page, donné par fenetre
        self.fenetre = fenetre

        ##déclaration d'un style de texte, nommé text
        self.text = [pygame.font.Font('../font/impact.ttf', 32)]

        ##chargement des fichiers sonores
        self.music = pygame.mixer.Sound("../music/musique.wav")

        ##chargement des images
        self.image = {"title" : pygame.image.load('../img/menu/title3.png')}
        self.image["play"] = pygame.image.load('../img/menu/play.png')
        self.image["score"] = pygame.image.load('../img/menu/score.png')
        self.image["option"] = pygame.image.load('../img/menu/option.png')
        self.image["edit"] = pygame.image.load('../img/menu/edit.png')
        self.image["cerdit"] = pygame.image.load('../img/menu/credit.png')

        ##création et placements des images
        self.rect = {"title" : self.image["title"].get_rect().move(0, 0)}
        self.rect["play"] = self.image["play"].get_rect().move(805, 445)
        self.rect["score"] = self.image["score"].get_rect().move(805, 587)
        self.rect["option"] = self.image["option"].get_rect().move(805, 729)
        self.rect["edit"] = self.image["edit"].get_rect().move(805, 871)
        self.rect["credit"] = self.image["edit"].get_rect().move(1019, 1750)
        self.rect["mur"] = pygame.Rect(1900, 0, 20, 20)

    def run(self):
        """fonction donnant la boucle qui actuallise la page 30 fois par seconde"""
        ##on lance le fichier son (musique.wav)
        self.music.play()

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
        self.fenetre.blit(self.image["play"], (805, 445))
        self.fenetre.blit(self.image["score"], (805, 587))
        self.fenetre.blit(self.image["option"], (805, 729))
        self.fenetre.blit(self.image["edit"], (805, 871))

        ##placement et contenu des textes
        text_nom1 = self.text[0].render('Armand PICARD', 1, (242,242,242))
        self.fenetre.blit(text_nom1, (40, 125))
        text_nom2 = self.text[0].render('Nathan CHEVALIER', 1, (242,242,242))
        self.fenetre.blit(text_nom2, (40, 180))
        text_nom3 = self.text[0].render('Jules ECARD', 1, (242,242,242))
        self.fenetre.blit(text_nom3, (40, 235))

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
                    if self.rect["play"].collidepoint(mouse):           ##si clic gauche et souris sur rectangle play,
                        self.music.stop()                               ##on coupe la musique
                        return "respawn"                                ##on lance le jeu
                    elif self.rect["score"].collidepoint(mouse):        ##si clic gauche et souris sur rectangle score,
                        score = Scores(self.fenetre)
                        r = score.run()                                 ##on ouvre la page des scores
                        if r == "close":
                            return 0
                        else:
                            return r
                    elif self.rect["option"].collidepoint(mouse):       ##si clic gauche et souris sur rectangle option,
                        option = Options(self.fenetre)
                        r = option.run()                                ##on ouvre la page des options
                        if r == "close":
                            return 0
                        else:
                            return r
                    elif self.rect["edit"].collidepoint(mouse):         ##si clic gauche et souris sur rectangle edit,
                        editeur = Editor(self.fenetre)                  ##on ouvre la page éditeur
                        editeur.loop()
                    elif self.rect["mur"].collidepoint(mouse):          ##Easter egg ;-)
                        mur = Mur(self.fenetre)
                        mur.run()
        return 0

