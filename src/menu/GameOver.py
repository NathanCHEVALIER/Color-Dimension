import pygame             ##importation des différents modules
import pygame.locals
import time

class GameOver():

    def __init__(self, fenetre):
        """Constructeur de Menu"""
        ##place et taille de la page, donné par fenetre
        self.fenetre = fenetre

        ##chargement des images
        self.image = {"GOpage" : pygame.image.load('../img/menu/GOpage.png')}
        self.image["GOmenu"] = pygame.image.load('../img/menu/GOmenu.png')
        self.image["GOrejouer"] = pygame.image.load('../img/menu/GOrejouer.png')

        ##création et placements des images
        self.rect = {"GOpage" : self.image["GOpage"].get_rect().move(685, 250)}
        self.rect["GOmenu"] = self.image["GOmenu"].get_rect().move(705, 740)
        self.rect["GOrejouer"] = self.image["GOrejouer"].get_rect().move(965, 740)

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
        self.fenetre.blit(self.image["GOpage"], (685, 250))
        self.fenetre.blit(self.image["GOmenu"], (705, 740))
        self.fenetre.blit(self.image["GOrejouer"], (965,740))

        ##rafraichissement d'écran
        pygame.display.flip()

    def update(self):
        """Gestion des évènements"""
        mouse = pygame.mouse.get_pos()                              ##on prend la position de la souris avec la variable mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "stop"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.rect["GOrejouer"].collidepoint(mouse):  ##si clic gauche et souris sur rectangle GOrejouer,
                        return "respawn"                            ##on lance le jeu
                    elif self.rect["GOmenu"].collidepoint(mouse):   ##si clic gauche et sourus sur rectangle GOmenu,
                        return "startmenu"                          ##on retourne au menu principal
        return 0
