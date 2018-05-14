import pygame             ##importation des différents modules
import pygame.locals
import time

class Credits():

    def __init__(self, fenetre):
        """Constructeur de Menu"""
        ##place et taille de la page, donné par fenetre
        self.fenetre = fenetre

        ##chargement des images
        self.image = {"title" : pygame.image.load('../img/menu/titlecredit.png')}
        self.image["closecredit"] = pygame.image.load('../img/menu/closecredit.png')

        ##création et placements des images
        self.rect = {"title" : self.image["title"].get_rect().move(0, 0)}
        self.rect["closecredit"] = self.image["closecredit"].get_rect().move(1200, 380)

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
                        return "startmenu"                                     ##on retourne au menu principal
        return 0
