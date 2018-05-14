import pygame             ##importation des différents modules
import pygame.locals
import time

class Pause():

    def __init__(self, fenetre):
        """Constructeur de Menu"""
        ##place et taille de la page, donné par fenetre
        self.fenetre = fenetre

        ##chargement des images
        self.image = {"pausepage" : pygame.image.load('../img/menu/pausepage.png')}
        self.image["pausereprendre"] = pygame.image.load('../img/menu/pausereprendre.png')
        self.image["pausemenu"] = pygame.image.load('../img/menu/pausemenu.png')

        ##création et placements des images
        self.rect = {"pausepage" : self.image["pausepage"].get_rect().move(685, 200)}
        self.rect["pausereprendre"] = self.image["pausereprendre"].get_rect().move(785, 580)
        self.rect["pausemenu"] = self.image["pausemenu"].get_rect().move(785, 700)

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
        ##placement des images déclarées dans __init__()
        self.fenetre.blit(self.image["pausepage"], (685, 300))
        self.fenetre.blit(self.image["pausereprendre"], (785, 580))
        self.fenetre.blit(self.image["pausemenu"], (785,700))

        ##rafraichissement d'écran
        pygame.display.flip()

    def update(self):
        """Gestion des évènements"""
        mouse = pygame.mouse.get_pos()                               ##on prend la position de la souris avec la variable mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "stop"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.rect["pausereprendre"].collidepoint(mouse):     ##si clic gauche et souris sur rectangle pausereprendre,
                        return "reprendre"                                  ##on reprend le jeu
                    elif self.rect["pausemenu"].collidepoint(mouse):        ##si clic gauche et souris sur rectangle pausemenu,
                        return "startmenu"                                  ##on retourne au menu principal
        return 0