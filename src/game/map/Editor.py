##Import des librairies et fichiers de classes
import json
import pygame
import pygame.locals
from game.tools import *
from game.settings import *

##déclaration de la classe éditor
class Editor():
    def __init__(self, fenetre, world, level):##Constructeur de classe appelé lors de l'instanciation d'un objet
        ##Chargement de police
        file = open('../data/map.json', 'r+')
        self.dataMap = json.load(file)
        file.close()
        self.ecriture = [pygame.font.Font('../font/impact.ttf', 40), pygame.font.Font('../font/impact.ttf', 30), pygame.font.Font('../font/impact.ttf', 20)]
        ##récupération de l'objet fenêtre
        self.fenetre = fenetre
        self.map = {"title": "", "width": "", "height": "", "selected": ""}
        self.list = []
        self.camPos = {"x": 5, "y": 9}
        self.current = {"element": ["empty", False], "world": [world, level]}
        self.cases = []

        self.loadMap()

        ##création de surfaces
        self.cadre = [pygame.Surface((1920, 1080)), pygame.Surface((200, 1080)), pygame.Surface((100, 50))]
        self.cadre[0].fill((50,50,50))
        self.cadre[1].fill((50,50,50))

        ##chargement et découpage du sprite
        self.image = {"sprite": pygame.image.load('../img/editeur.png'), "decor": pygame.image.load('../img/' + self.dataMap[self.current["world"][0]]["limit"][4] + '.png')}
        self.image["save"] = self.image["sprite"].subsurface(100, 0, 100, 40)
        self.image["plateforme"] = self.image["decor"].subsurface(0, 0, 100, 50)
        self.image["piege"] = self.image["decor"].subsurface(0, 100, 100, 50)
        self.image["colorPlateforme"] = self.image["decor"].subsurface(0, 50, 100, 50)
        self.image["ennemies"] = self.image["decor"].subsurface(0, 150, 100, 50)
        self.image["debut"] = self.image["decor"].subsurface(0, 200, 100, 50)
        self.image["fin"] = self.image["decor"].subsurface(0, 250, 100, 50)
        self.image["empty"] = self.image["sprite"].subsurface(100, 50, 100, 50)
        self.image["paletteColor"] = self.image["sprite"].subsurface(200, 100, 175, 50)
        self.image["cursor"] = self.image["sprite"].subsurface(200, 150, 10, 50)

        self.image["background"] = pygame.Surface((self.dataMap[self.current["world"][0]][self.current["world"][1]]["limit"][2] + 2000, self.dataMap[self.current["world"][0]][self.current["world"][1]]["limit"][3] + 2000))
        self.image["background"].fill((174,226,254))
        self.image["zone"] = pygame.Surface((self.dataMap[self.current["world"][0]][self.current["world"][1]]["limit"][2], self.dataMap[self.current["world"][0]][self.current["world"][1]]["limit"][3]))
        self.image["zone"].fill((210,210,210))

        ##création des surfaces correspondantes aux images (utilisées pour les event)
        self.rects = {"save": self.image["save"].get_rect().move((50, 950)), "paletteColor": self.image["paletteColor"].get_rect().move((200, 1000)),
                        "piege": self.image["piege"].get_rect().move((50, 290)), "colorPlateforme": self.image["colorPlateforme"].get_rect().move((50, 230)),
                        "empty": self.image["empty"].get_rect().move((50, 70)), "plateforme": self.image["plateforme"].get_rect().move((50, 150)),
                        "ennemies": self.image["ennemies"].get_rect().move((50, 350)), "debut": self.image["debut"].get_rect().move((50, 420)),
                        "fin": self.image["fin"].get_rect().move((50, 500))}

    def render(self):
        ## on décale le fond pour centrer le champ de vision comme voulu
        self.fenetre.blit(self.cadre[0], (0,0))
        self.fenetre.blit(self.image["background"], (self.camPos["x"] * -100, self.camPos["y"] * -100))
        self.image["background"].blit(self.image["zone"], (1000, 1000))
        self.image["zone"].fill((210, 210,210))

        ##on affiche le contenu du tableau, soit les obstacles
        for i in range(0, len(self.cases)):
            for c in range(0, len(self.cases[i])):
                if self.cases[i][c][0] == "colorPlateforme":
                    pygame.draw.rect(self.image["zone"], getColor(self.cases[i][c][1]), (c * 100, i*50, 100, 50))
                self.image["zone"].blit(self.image[self.cases[i][c][0]], (c * 100, i*50))

        ##on affiche tout les éléments d'interfaces de l'éditeur
        self.fenetre.blit(self.cadre[1], (0,0))
        self.cadre[2].fill(getColor(self.current["element"][1]))
        self.fenetre.blit(self.cadre[2], (50,230))
        self.fenetre.blit(self.image["empty"], (50, 70))
        self.fenetre.blit(self.image["plateforme"], (50, 150))
        self.fenetre.blit(self.image["colorPlateforme"], (50, 230))
        self.fenetre.blit(self.image["piege"], (50, 290))
        self.fenetre.blit(self.image["ennemies"], (50, 350))
        self.fenetre.blit(self.image["debut"], (50, 420))
        self.fenetre.blit(self.image["fin"], (50, 500))
        self.fenetre.blit(self.image["paletteColor"], (200, 1000))
        self.fenetre.blit(self.image["cursor"], (205 + (int(self.current["element"][1]) / 10), 1000 ))
        self.fenetre.blit(self.image["save"], (50, 950))

        ##on rafraichit l'écran
        pygame.display.flip()

    def update(self):
        ##on récupère les events
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:##quitter l'édition en cours
                self.editing = False
                return False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_F11:
                    Settings.changeFullScreen(self.fenetre)
                if event.key == pygame.K_UP and self.camPos["y"] >= 0:
                    self.camPos["y"] -= 1
                if event.key == pygame.K_DOWN:
                    self.camPos["y"] += 1
                if event.key == pygame.K_RIGHT and self.camPos["y"]  <= self.dataMap[self.current["world"][0]]["limit"][3]:
                    self.camPos["x"] += 1
                if event.key == pygame.K_LEFT and self.camPos["x"] >= 0:
                    self.camPos["x"] -= 1
            if event.type == pygame.MOUSEBUTTONDOWN:##détection des pointde clics de la souris
                ##Choix d'un type d'obstacle sur le panel d'édition
                if self.rects["plateforme"].collidepoint(mouse):
                    self.current["element"][0] = "plateforme"##on garde en mémoire l'outil d'édition actuel
                elif self.rects["colorPlateforme"].collidepoint(mouse):
                    self.current["element"][0] = "colorPlateforme"
                elif self.rects["piege"].collidepoint(mouse):
                    self.current["element"][0] = "piege"
                elif self.rects["empty"].collidepoint(mouse):
                    self.current["element"][0] = "empty"
                elif self.rects["ennemies"].collidepoint(mouse):
                    self.current["element"][0] = "ennemies"
                elif self.rects["debut"].collidepoint(mouse):
                    self.current["element"][0] = "debut"
                elif self.rects["fin"].collidepoint(mouse):
                    self.current["element"][0] = "fin"
                ##choix de la couleur sur la palette
                elif self.rects["paletteColor"].collidepoint(mouse):
                    mousePos = pygame.mouse.get_pos()
                    if mousePos[0] <= 363:
                        color = (mousePos[0] - 210)*10
                    else:
                        color = 1530
                    ##la couleur est une valeur analogique interprétée lors e l'affichage
                    self.current["element"][1] = color
                ##appui sur le bouton d'enregistrement
                elif self.rects["save"].collidepoint(mouse):
                    ##on enregistre puis sort de l'éditeur
                    self.saveMap()
                    self.editing = False
                    return False
                else:
                    ##si il y a clic detecté mais sur aucun des éléments d'éditions, on détermine s'il se situe sur une case de la map
                    mousePos = pygame.mouse.get_pos()
                    y = int(((self.camPos["y"] * 100) + mousePos[1] - 1000) / 50)
                    x = int(((self.camPos["x"] * 100) + mousePos[0] - 1000) / 100)
                    if x >= 0 and x < len(self.cases[0]) and y >= 0 and y < len(self.cases):##si c'est le cas on attribue la valeur de l'obstacle à la cellule du tableau
                        self.cases[y][x] = [self.current["element"][0], self.current["element"][1]]

        return True

    def saveMap(self):
        ##on parcours le tableau de l'éditeur pour reconnaitre les cases pleines
        for i in range (0, len(self.cases)):
            for c in range (0, len(self.cases[i])):
                if self.cases[i][c][0] == "plateforme":
                    if c == 0:
                        self.newMap["plateforme"][len(self.newMap["plateforme"])] = [c*100, i*50, 100, 50]
                    else:
                        if self.cases[i][c-1][0] == "plateforme":##si la case précédente est du même type on agrandit la largeur plutôt que de doubler le nombre de plateformes
                            self.newMap["plateforme"][len(self.newMap["plateforme"]) - 1][2] += 100
                        else:
                            self.newMap["plateforme"][len(self.newMap["plateforme"])] = [c*100, i*50, 100, 50]

                elif self.cases[i][c][0] == "colorPlateforme":##de même pour les autres types d'obstacles
                    if c == 0:
                        self.newMap["colorPlateforme"][len(self.newMap["colorPlateforme"])] = [c*100, i*50, 100, 50, self.cases[i][c][1]]
                    else:
                        if self.cases[i][c-1][0] == "colorPlateforme":
                            self.newMap["colorPlateforme"][len(self.newMap["colorPlateforme"]) - 1][2] += 100
                        else:
                            self.newMap["colorPlateforme"][len(self.newMap["colorPlateforme"])] = [c*100, i*50, 100, 50, self.cases[i][c][1]]

                elif self.cases[i][c][0] == "piege":
                    if c == 0:
                        self.newMap["piege"][len(self.newMap["piege"])] = [c*100, i*50 + 20, 100, 30]
                    else:
                        if self.cases[i][c-1][0] == "piege":
                            self.newMap["piege"][len(self.newMap["piege"]) - 1][2] += 100
                        else:
                            self.newMap["piege"][len(self.newMap["piege"])] = [c*100, i*50 + 20, 100, 30]

                elif self.cases[i][c][0] == "ennemies":
                    self.newMap["ennemies"][len(self.newMap["ennemies"])] = [c*100, i*50 + 20, 100, 30]
                elif self.cases[i][c][0] == "debut":
                    self.newMap["debut"][len(self.newMap["debut"])] = [c*100, i*50 + 20, 100, 30]
                elif self.cases[i][c][0] == "fin":
                    self.newMap["fin"][len(self.newMap["fin"])] = [c*100, i*50 + 20, 100, 30]

        ##on lit les données, les modifie puis les réécrits
        file = open('../data/map.json', 'r+')
        content = json.load(file)
        content[self.current["world"][0]][self.current["world"][1]] = self.newMap
        file.seek(0)
        json.dump(content, file)
        file.truncate()
        file.close()

    def setCamera(self, x, y):
        ##permet de éplacer le champ de vision dans l'éditeur
        pos = self.fond.get_rect()
        pos = pos.move(-x, -y)
        self.level.blit(self.zone, self.posZone)
        self.fenetre.blit(self.level, pos)
        pygame.display.flip()

    def loadMap(self):
        ##création d'un tableau double dimension initialisé à "empty"
        self.cases = [[["empty", False]] * int(self.dataMap[self.current["world"][0]][self.current["world"][1]]["limit"][2] / 100) for i in range(int(self.dataMap[self.current["world"][0]][self.current["world"][1]]["limit"][3] / 50))]

        ##Chargement de la map courantes: on place les obstacles à leurs places
        for j in self.dataMap[self.current["world"][0]][self.current["world"][1]]:
            if j in ["plateforme", "piege", "debut", "fin", "colorPlateforme", "ennemies"]:
                for i in self.dataMap[self.current["world"][0]][self.current["world"][1]][j]:
                    for c in range(0, int(self.dataMap[self.current["world"][0]][self.current["world"][1]][j][i][2] / 100)):
                        x = int(self.dataMap[self.current["world"][0]][self.current["world"][1]][j][i][0]/100) + c
                        y = int(self.dataMap[self.current["world"][0]][self.current["world"][1]][j][i][1]/ 50)
                        if j in ["colorPlateforme",]:
                            argu = self.dataMap[self.current["world"][0]][self.current["world"][1]][j][i][4]
                        else:
                            argu = 0
                        self.cases[y][x] = [j, argu]


        self.newMap = {"limit": self.dataMap[self.current["world"][0]][self.current["world"][1]]["limit"], "plateforme": {}, "piege": {}, "colorPlateforme": {}, "debut": {}, "fin": {}, "ennemies": {}}
