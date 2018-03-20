from game.entities.Player import *
from game.map.Map import *
from game.settings import *
import time

class Game:
    def __init__(self, fenetre, mapId):
        self.player = Player(0, 0, 0)
        self.fenetre = fenetre
        self.mapId = mapId
        self.map = Map(self.fenetre, self.player, self.mapId)

    def render(self, fenetre):
        self.map.render(fenetre)
        self.player.render(fenetre)

    def update(self):
        self.input()
        self.map.update()

    def input(self):
        pass