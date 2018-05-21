import pygame
from pygame.locals import *
from game.entities.Entity import *
import math

class Monster(Entity):
    def __init__(self,fenetre, x, y, z, player):
        Entity.__init__(self, x, y, z)
        self.fenetre = fenetre
        self.level = pygame.Rect(1000, 9170, 4000, 2000)

        self.onground = False
        self.color = (255, 0, 0)
        self.target = player
        #image pour le rendu
        self.image = {"droite": pygame.image.load('../img/monster.png')}
        self.image["gauche"] = pygame.image.load('../img/monster2.png')
        self.image["droite"] = pygame.transform.scale(self.image["droite"], (65, 100))
        self.image["gauche"] = pygame.transform.scale(self.image["gauche"], (65, 100))

        #rect pour les collisions
        self.hitbox = pygame.Rect(0, 0, 65, 100)

    def render(self, x, y):
        """affiche l'ennemi"""
        #affiche la hitbox
        ##pygame.draw.rect(self.fenetre, (255, 0, 0, 1), pygame.Rect(x, y, self.hitbox.w, self.hitbox.h))
        #on a deux cas pour le rendu suivant l'orientation de l'enemny
        if self.vx >= 0:
            self.fenetre.blit(self.image["droite"], (x, y))
        else:
            self.fenetre.blit(self.image["gauche"], (x, y))

    def update(self):
        """Actualise le jouer: IA, collisions"""
        self.lastx = self.x
        self.lasty = self.y
        self.lastz = self.z

        #IA
        dx = self.target.x - self.x
        dy = self.target.y - self.y
        dd = math.sqrt((dx)**2 + (dy)**2)
        if dd == 0:
            self.vx = 0
        elif dd < 500:
            self.vx = (dx / dd) * 10
            if self.onground and dy < -15:
                self.vy = -50
                self.onground = False
        else:
            self.vx = 0
            self.vy = 0

        #ajout de la gravité et des vitesses
        self.vy += 9.81
        self.x += self.vx
        self.y += self.vy

        if self.y > self.level.h:
            self.vy = 0
            self.y = self.level.h
            self.onground = True

        self.hitbox.x = self.x
        self.hitbox.y = self.y

        self.collisionPiege()
        self.collisionPlatform()
        self.collisionPlatformColor()

    def setMap(self, map):
        self.map = map