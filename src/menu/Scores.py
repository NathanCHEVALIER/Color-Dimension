import json             ##importation des différents modules
import pygame
import pygame.locals
import time

class Scores():

    def __init__(self, fenetre):
        """Constructeur de Menu"""
        ##place et taille de la page, donné par fenetre
        self.fenetre = fenetre

        ##déclaration d'un style de texte, nommé text
        self.text = [pygame.font.Font('../font/impact.ttf', 54)]

        ##chargement des images
        self.image = {"title" : pygame.image.load('../img/menu/title1.png')}
        self.image["close"] = pygame.image.load('../img/menu/close.png')
        self.image["page"] = pygame.image.load('../img/menu/tabscore.png')
        self.image["scoretag"] = pygame.image.load('../img/menu/scoretag.png')

        ##création et placements des images
        self.rect = {"title" : self.image["title"].get_rect().move(0, 0)}
        self.rect["close"] = self.image["close"].get_rect().move(1090, 390)
        self.rect["page"] = self.image["page"].get_rect().move(685, 440)
        self.rect["scoretag"] = self.image["scoretag"].get_rect().move(750, 375)

    def run(self):
        """fonction donnant la boucle qui actuallise la page 30 fois par seconde"""
        ##on appel la fichier scorelist.json pour que l'affichage des scores dans la page s'actuallise à chaques ouverture de la page
        file = open('../data/scorelist.json', 'r+')
        self.datascore = json.load(file)

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
        self.fenetre.blit(self.image["close"], (1090, 390))
        self.fenetre.blit(self.image["page"], (685, 440))
        self.fenetre.blit(self.image["scoretag"], (750, 375))

        ##placement et contenu des textes
        text_score1 = self.text[0].render(str(self.datascore[0]['scores']['1']), 1, (242,242,242))
        self.fenetre.blit(text_score1, (900, 525))
        text_score2 = self.text[0].render(str(self.datascore[0]['scores']['2']), 1, (242,242,242))
        self.fenetre.blit(text_score2, (900, 635))
        text_score3 = self.text[0].render(str(self.datascore[0]['scores']['3']), 1, (242,242,242))
        self.fenetre.blit(text_score3, (900, 745))

        ##rafraichissement d'écran
        pygame.display.flip()

    def update(self):
        """fonction regroupant des évènements présents sur la page"""
        mouse = pygame.mouse.get_pos()                                  ##on prend la position de la souris avec la variable mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "stop"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.rect["close"].collidepoint(mouse):          ##si clic gauche et souris sur sur rectangle close,
                        return "close"                                  ##on retourne sur le menu principal
        return 0


def score_udapte(score):
    """fonction qui, à la fin d'une partie, modifie la liste des meilleurs scores dans scorelist.json"""
    file = open('../data/scorelist.json', 'r+')
    datascore = json.load(file)
    if datascore[0]['scores']['3'] < score <=  datascore[0]['scores']['2']:
        datascore[0]['scores']['3'] = score
    if datascore[0]['scores']['2'] < score <=  datascore[0]['scores']['1']:
        datascore[0]['scores']['3'] = datascore[0]['scores']['2']
        datascore[0]['scores']['2'] = score
    if datascore[0]['scores']['1'] < score:
        datascore[0]['scores']['3'] = datascore[0]['scores']['2']
        datascore[0]['scores']['2'] = datascore[0]['scores']['1']
        datascore[0]['scores']['1'] = score

    ##Sauvegarde des nouvelles valeurs dans scorelist.json
    file.seek(0)
    file.truncate()
    file.close()

