import json
import pygame

class Map:
    def __init__(self, fenetre, player, mapId):
        self.fenetre = fenetre
        self.mapId = mapId
        self.player = player
        self.level = 0
        self.zone = []
        self.enemies = []
        self.generateMap(self.mapId)

    def update(self):
        pass

    def render(self, fenetre):
        pass

    def generateMap(self, mapId):
        data = self.loadMap(mapId, False)
        self.level = pygame.image.load('../img/background.jpg')
        self.level = pygame.transform.scale(self.level, (data['limit'][2], data['limit'][3]))
        for i in data:
            if i != "limit":
                self.generateZone(data[i])

    def loadMap(self, mapId, zoneId):
        content = json.load(open('../data/map.json'))
        if zoneId != False:
            return content[mapId][zoneId]
        else:
            return content[mapId]

    def generateZone(self, data):
        zone = pygame.image.load('../img/zone.png')
        zone = pygame.transform.scale(zone, (data['limit'][2], data['limit'][3]))
        pos = zone.get_rect()
        pos = pos.move(data['limit'][0], data['limit'][1])
        self.level.blit(zone, pos)
        self.zone.append(zone)
        self.loadZone(data)

    def loadZone(self, data):
        self.setPlateforme(data["plateforme"])
        self.setCamera(1000,1100)
        self.setCamera(1000,1100)

    def setPlateforme(self, data):
        for i in data:
            zone = pygame.image.load('../img/plateforme.png')
            zone = pygame.transform.scale(zone, (data[i][2], data[i][3]))
            pos = zone.get_rect()
            pos = pos.move(data[i][0], data[i][1])
            self.level.blit(zone, pos)
            pygame.display.flip()

    def setCamera(self, x, y):
        pos = self.level.get_rect()
        pos = pos.move(-x, -y)
        self.fenetre.blit(self.level, pos)
