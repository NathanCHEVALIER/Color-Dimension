import pygame             ##importation des différents modules
import pygame.locals
import time
from menu.Scores import *
from menu.Options import *
from menu.Mur import *
from menu.Credits import *
from game.map.Editor import *
from game.settings import *

class StartMenu():

    def __init__(self, fenetre):
        """Constructeur de Menu"""
        ##place et taille de la page, donné par fenetre
        self.fenetre = fenetre

        ##chargement des fichiers sonores
        self.music = pygame.mixer.Sound("../music/musique.wav")

        ##chargement des images
        self.image = {"title" : pygame.image.load('../img/menu/title3.png')}
        self.image["play"] = pygame.image.load('../img/menu/play.png')
        self.image["score"] = pygame.image.load('../img/menu/score.png')
        self.image["option"] = pygame.image.load('../img/menu/option.png')
        self.image["edit"] = pygame.image.load('../img/menu/edit.png')
        self.image["credit"] = pygame.image.load('../img/menu/credit.png')

        ##création et placements des images
        self.rect = {"title" : self.image["title"].get_rect().move(0, 0)}
        self.rect["play"] = self.image["play"].get_rect().move(805, 445)
        self.rect["score"] = self.image["score"].get_rect().move(805, 587)
        self.rect["option"] = self.image["option"].get_rect().move(805, 729)
        self.rect["edit"] = self.image["edit"].get_rect().move(805, 871)
        self.rect["mur"] = pygame.Rect(1900, 0, 20, 20)
        self.rect["credit"] = self.image["edit"].get_rect().move(1740, 960)

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
        self.fenetre.blit(self.image["credit"], (1740, 960))

        ##rafraichissement d'écran
        pygame.display.flip()



    def update(self):
        """fonction regroupant des évènements présents sur la page"""
        mouse = pygame.mouse.get_pos()                              ##on prend la position de la souris avec la variable mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "stop"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    Settings.changeFullScreen(self.fenetre)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.rect["play"].collidepoint(mouse):           ##si clic gauche et souris sur rectangle play,
                        self.music.stop()                               ##on coupe la musique
                        return "start"                                ##on lance le jeu
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
                    elif self.rect["credit"].collidepoint(mouse):       ##si clic gauche et souris sur rectangle option,
                        credit = Credits(self.fenetre)
                        r = credit.run()                                ##on ouvre la page des options
                        if r == "close":
                            return 0
                        else:
                            return r
        return 0

