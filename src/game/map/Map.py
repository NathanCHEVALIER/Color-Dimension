import json
import pygame

class Map:
    def __init__(self, fenetre):
        self.blocks = []
        self.enemies = []
        self.fenetre = fenetre
        self.generateMap()

    def update(self):
        for e in self.enemies:
            e.update()

    def render(self, fenetre):
        for e in self.enemies:
            e.render(fenetre)

        return fenetre

    def loadMap(self, source):
        content = json.load(open('../data/map.json'))
        data = content[source]

        return data

    def generateMap(self):
        data = self.loadMap("tower")
        self.setPlateforme(data["plateforme"])

    def setPlateforme(self, data):
        for i in data:
            pygame.draw.rect(self.fenetre, (255,0,0), tuple(data[i]), 0)
