##Import des librairies et fichiers de classes
import json
import pygame
from game.entities.Monster import *
from game.tools import *

##déclaration de la classe map
class Map:
    def __init__(self, fenetre, player, mapId):##Constructeur de classe appelé lors de l'instanciation d'un objet
    ##Récupération de paramètres comme attributs de classe
        self.fenetre = fenetre
        self.mapId = mapId
        self.player = player
        ##Initialisation des variables
        self.level = 0
        self.zone = 0
        self.posZone = 0
        self.image = {"sprite": 0, "plateforme": 0, "piege": 0, "colorPlateforme": 0}
        self.rects = {"plateforme": [], "piege": [], "colorPlateforme": [], "start": [], "finish": []}
        self.music = ''
        ##appel de fonction
        self.generateMap(self.mapId)

    def update(self):
        pass

    def render(self):
        pass

    def generateMap(self, mapId):
        ##chargement des données
        data = self.loadMap(mapId, False)
        self.level = pygame.Surface((data['limit'][2], data['limit'][3]))
        self.level.fill((174,226,254))
        ##on parcours les zones de la map
        for i in data:
            if i != "limit":
                ##création de la zone de jeu
                self.zone = pygame.Surface((data[i]['limit'][2], data[i]['limit'][3]))
                self.zone.fill((200,200,200))
                self.posZone = self.zone.get_rect()
                self.posZone = self.posZone.move(data[i]['limit'][0], data[i]['limit'][1])
                ##appel des fonctions d'affichage des plateformes
                self.setPlateforme(data[i]["plateforme"])
                self.setPiege(data[i]["piege"])
                self.setColorPlateforme(data[i]["colorPlateforme"])
                self.rects["debut"] = self.image["debut"][1].move((data[i]["debut"][2], data[i]["debut"][3]))
                self.rects["fin"] = self.image["fin"][1].move((data[i]["fin"][2], data[i]["fin"][3]))
                ##choix de la vue de la zone de jeu
                self.setCamera(1000,1100)
        print(self.rects)

    def loadMap(self, mapId, zoneId):
        ##chargement des données du fichier JSON, du sprite et de la musique correspondants
        file = open('../data/map.json')
        content = json.load(file)
        self.image["sprite"] = pygame.image.load('../img/' + content[mapId]["limit"][4] + '.png')
        self.music = '../music/' + content[mapId]["limit"][4] + '.wav'
        ##Création des images d'obstacles à partir du sprite
        plateforme = self.image["sprite"].subsurface(0, 0, 100, 50)
        self.image["plateforme"] = [plateforme, plateforme.get_rect()]
        piege = self.image["sprite"].subsurface(0, 120, 100, 30)
        self.image["piege"] = [piege, piege.get_rect()]
        colorPlateforme = self.image["sprite"].subsurface(0, 50, 100, 50)
        self.image["colorPlateforme"] = [colorPlateforme, colorPlateforme.get_rect()]

        debut = self.image["sprite"].subsurface(0, 200, 100, 50)
        self.image["debut"] = [debut, debut.get_rect()]
        fin = self.image["sprite"].subsurface(0, 250, 100, 50)
        self.image["fin"] = [fin, fin.get_rect()]
        ##on retourne les données chargées
        if zoneId != False:
            return content[mapId][zoneId]
        else:
            return content[mapId]
        file.close()

    def setPlateforme(self, data):
        ##affichage et considération comme obstacle des plateformes contenues dans le tableau de données
        for c in data:
            for i in range(0, int(data[c][2] / 100)):
                pos = self.image["plateforme"][1].move(data[c][0] + (i *100), data[c][1])
                self.rects["plateforme"].append(pos)
                self.zone.blit(self.image["plateforme"][0], pos)

    def setPiege(self, data):
        ##affichage et considération comme obstacle des pièges contenues dans le tableau de données
        for c in data:
            for i in range(0, int(data[c][2] / 100)):
                pos = self.image["piege"][1].move(data[c][0] + (i *100), data[c][1])
                self.rects["piege"].append(pos)
                self.zone.blit(self.image["piege"][0], pos)

    def setColorPlateforme(self, data):
        ##affichage et considération comme obstacle des plateformes de couleur contenues dans le tableau de données
        for c in data:
            for i in range(0, int(data[c][2] / 100)):
                pos = self.image["colorPlateforme"][1].move(data[c][0] + (i *100), data[c][1])
                self.rects["colorPlateforme"].append([pos, data[c][4]])
                pygame.draw.rect(self.zone, getColor(data[c][4]), pos)
                self.zone.blit(self.image["colorPlateforme"][0], pos)

    def setCamera(self, x, y):
        ##déplacement du champ de vision de la zone de jeu en fonction de la position du personnage
        pos = self.level.get_rect()
        pos = pos.move(-x, -y)
        ##le principe consistant à décaler le fond
        self.level.blit(self.zone, self.posZone)
        self.fenetre.blit(self.level, pos)
        ##on rafraichit l'écran
        pygame.display.flip()

    def getMusic(self):
        ## retourne la musique en fonction du décor
        music = pygame.mixer.Sound(self.music)
        music.set_volume(0.2)
        return music

    def getMaps(self):
        ## retourne la liste des maps existantes
        file = open('../data/map.json')
        content = json.load(file)
        liste = []
        for i in content:
            liste.append(i)
        return liste
