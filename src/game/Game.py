from game.entities.Player import *
from game.map.Map import *
from game.settings import *
import time

class Game:
    def __init__(self, fenetre):
        self.player = Player(0, 0, 0)
        self.fenetre = fenetre
        self.map = Map(fenetre)

    def render(self, fenetre):
        self.map.render(fenetre)
        self.player.render(fenetre)

    def update(self):
        self.input()
        self.map.update()

    def input(self):
        pass