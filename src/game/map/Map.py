import json
import pygame
from game.entities.Monster import *
from game.tools import *

class Map:
    def __init__(self, fenetre, player, mapId):
        self.fenetre = fenetre
        self.mapId = mapId
        self.player = player
        self.level = 0
        self.zone = 0
        self.posZone = 0
        self.image = {"sprite": 0, "plateforme": 0, "piege": 0, "colorPlateforme": 0}
        self.rects = {"plateforme": [], "piege": [], "colorPlateforme": []}

        self.generateMap(self.mapId)

    def update(self):
        pass

    def render(self):
        pass

    def generateMap(self, mapId):
        data = self.loadMap(mapId, False)
        self.level = pygame.Surface((data['limit'][2], data['limit'][3]))
        self.level.fill((174,226,254))
        for i in data:
            if i != "limit":
                self.generateZone(data[i])

    def loadMap(self, mapId, zoneId):
        file = open('../data/map.json')
        content = json.load(file)
        self.image["sprite"] = pygame.image.load('../img/sprite' + mapId + '.png')
        plateforme = self.image["sprite"].subsurface(300, 300, 100, 50)
        self.image["plateforme"] = [plateforme, plateforme.get_rect()]
        piege = self.image["sprite"].subsurface(300, 120, 100, 30)
        self.image["piege"] = [piege, piege.get_rect()]
        colorPlateforme = self.image["sprite"].subsurface(300, 200, 100, 50)
        self.image["colorPlateforme"] = [colorPlateforme, colorPlateforme.get_rect()]
        if zoneId != False:
            return content[mapId][zoneId]
        else:
            return content[mapId]
        file.close()


    def generateZone(self, data):
        self.zone = pygame.Surface((data['limit'][2], data['limit'][3]))
        self.zone.fill((200,200,200))
        self.posZone = self.zone.get_rect()
        self.posZone = self.posZone.move(data['limit'][0], data['limit'][1])
        self.setPlateforme(data["plateforme"])
        self.setPiege(data["piege"])
        self.setColorPlateforme(data["colorPlateforme"])
        self.setCamera(1000,1100)

    def setPlateforme(self, data):
        for c in data:
            for i in range(0, int(data[c][2] / 100)):
                pos = self.image["plateforme"][1].move(data[c][0] + (i *100), data[c][1])
                self.rects["plateforme"].append(pos)
                self.zone.blit(self.image["plateforme"][0], pos)

    def setPiege(self, data):
        for c in data:
            for i in range(0, int(data[c][2] / 100)):
                pos = self.image["piege"][1].move(data[c][0] + (i *100), data[c][1])
                self.rects["piege"].append(pos)
                self.zone.blit(self.image["piege"][0], pos)

    def setColorPlateforme(self, data):
        for c in data:
            for i in range(0, int(data[c][2] / 100)):
                pos = self.image["colorPlateforme"][1].move(data[c][0] + (i *100), data[c][1])
                self.rects["colorPlateforme"].append([pos, data[c][4]])
                pygame.draw.rect(self.zone, getColor(data[c][4]), pos)
                self.zone.blit(self.image["colorPlateforme"][0], pos)

    def setCamera(self, x, y):
        pos = self.level.get_rect()
        pos = pos.move(-x, -y)
        self.level.blit(self.zone, self.posZone)
        self.fenetre.blit(self.level, pos)
        pygame.display.flip()
