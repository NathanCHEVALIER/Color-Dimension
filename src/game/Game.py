from game.entities.Player import *
from game.map.Map import *
from game.map.Editor import *
from game.settings import *
import time

class Game:
    def __init__(self, fenetre, mapId):
        self.fenetre = fenetre
        self.player = Player(self.fenetre, 2000, 1700, 0)
        self.mapId = mapId
        self.map = Map(self.fenetre, self.player, self.mapId)
        self.editor = Editor(self.fenetre)
        self.player.setMap(self.map)




    def render(self):
        """rendu de la map et du joueur"""
        self.map.setCamera(self.player.x - 910 + self.player.level.x , self.player.y - 400 + self.player.level.y)
        self.map.render()
        self.player.render()

    def update(self):
        """update de la map et du joueur"""
        self.map.update()
        self.player.update()

    def respawn(self):
        """remet le joeur à sa position de depart"""
        self.player.x = 2000
        self.player.y = 1700
        self.player.z = 0
        self.player.alive = True
