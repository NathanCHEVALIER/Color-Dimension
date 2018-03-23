import json
import pygame

class Map:
    def __init__(self, fenetre, player, mapId):
        self.fenetre = fenetre
        self.mapId = mapId
        self.player = player
        self.level = 0
        self.zone = 0
        self.posZone = 0
        ##self.zones = []
        self.enemies = []
        self.generateMap(self.mapId)

    def update(self):
        pass

    def render(self):
        pass

    def generateMap(self, mapId):
        data = self.loadMap(mapId, False)
        self.level = pygame.image.load('../img/background.png')
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
        self.zone = pygame.image.load('../img/zone.png')
        self.zone = pygame.transform.scale(self.zone, (data['limit'][2], data['limit'][3]))
        self.posZone = self.zone.get_rect()
        self.posZone = self.posZone.move(data['limit'][0], data['limit'][1])
        self.loadZone(data)
        self.setCamera(1000,1100)

    def loadZone(self, data):
        self.setPlateforme(data["plateforme"])
        data = data["plateforme"]
        plateforme = pygame.image.load('../img/plateforme.png')
        plateforme = pygame.transform.scale(plateforme, (data["2"][2], data["2"][3]))
        pos = plateforme.get_rect()
        pos = pos.move(data["2"][0], data["2"][1])
        self.zone.blit(plateforme, pos)

    def setPlateforme(self, data):
        for i in data:
            plateforme = pygame.image.load('../img/plateforme.png')
            plateforme = pygame.transform.scale(plateforme, (data[i][2], data[i][3]))
            pos = plateforme.get_rect()
            pos = pos.move(data[i][0], data[i][1])
            self.zone.blit(plateforme, pos)

    def setCamera(self, x, y):
        pos = self.level.get_rect()
        pos = pos.move(-x, -y)
        self.level.blit(self.zone, self.posZone)
        self.fenetre.blit(self.level, pos)
        pygame.display.flip()
