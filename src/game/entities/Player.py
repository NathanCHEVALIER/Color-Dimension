import pygame
from pygame.locals import *
from game.entities.Entity import *
from physics.AABB import *
class Player(Entity):
    def __init__(self, x, y, z):
        Entity.__init__(self, x, y, z)
        self.tete = AABB(x + 10, y, z, 10, 10, 10)
        self.corp = AABB(x, y + 10, z, 10, 40, 20)

    def render(self, fenetre):
        pass

    def update(self):
        pass