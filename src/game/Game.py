from game.entities.Player import *
from game.map.Map import *
from game.settings import *
import time

class Game:
    def __init__(self, fenetre, mapId):
        self.fenetre = fenetre
        self.player = Player(self.fenetre, 0, 0, 0)
        self.mapId = mapId
        self.map = Map(self.fenetre, self.player, self.mapId)

    def render(self):
        ##self.map.render()
        self.map.setCamera(self.player.x - 910, self.player.y - 400)
        self.player.render()

    def update(self):
        self.player.update()
        self.map.update()
