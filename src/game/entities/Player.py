import pygame
from pygame.locals import *
from game.entities.Entity import *
from game.tools import *
import json

class Player(Entity):
    def __init__(self,fenetre, x, y, z):
        """constructeur pour player"""
        Entity.__init__(self, x, y, z)
        self.fenetre = fenetre
        self.level = 0

        self.alive = True
        self.onground = False

        self.color = (255, 0, 0)

        self.side = "droite"
        self.steep = 0

        #met en memoir le son pour le saut
        self.son = {"saut" : pygame.mixer.Sound("../music/saut.wav")}

        #image pour le rendu
        self.image = {"droite": {}, "gauche" : {}}
        for i in range(0, 30):
            self.image["droite"][i] = pygame.image.load('../img/licorne_droite/out' + str(i) + '.png')
            self.image["droite"][i] = pygame.transform.scale(self.image["droite"][i], (100, 150))
            self.image["gauche"][i] = pygame.image.load('../img/licorne_gauche/out' + str(i) + '.png')
            self.image["gauche"][i] = pygame.transform.scale(self.image["gauche"][i], (100, 150))

        #rect pour les collisions
        self.hitbox = pygame.Rect(0, 0, 80, 150)
        self.inputs = {"droite" : False, "gauche" : False, "sauter" : False}

    def render(self):
        """rendu du joueur"""
        #affiche le hitbox
        ##pygame.draw.rect(self.fenetre, (255, 0, 0, 0.5), pygame.Rect(910, 400, self.hitbox.w, self.hitbox.h))

        if self.vx != 0:
            if self.side == "droite":
                pygame.draw.polygon(self.fenetre, self.color, [[968, 400], [938, 435], [965, 435]])
                self.steep = (self.steep + 1) % 30
                self.fenetre.blit(self.image["droite"][self.steep], (900, 400))
            elif self.side == "gauche":
                pygame.draw.polygon(self.fenetre, self.color, [[928, 400], [930, 435], [957, 435]])
                self.steep = (self.steep + 1) % 30
                self.fenetre.blit(self.image["gauche"][self.steep], (900, 400))
        else:
            if self.side == "droite":
                pygame.draw.polygon(self.fenetre, self.color, [[968, 400], [938, 435], [965, 435]])
                self.fenetre.blit(self.image["droite"][0], (900, 400))
            elif self.side == "gauche":
                pygame.draw.polygon(self.fenetre, self.color, [[928, 400], [930, 435], [957, 435]])
                self.fenetre.blit(self.image["gauche"][0], (900, 400))

    def getInput(self, event, options):
        for e in event:
            key = None
            if e.type == pygame.KEYDOWN or e.type == pygame.MOUSEBUTTONDOWN:
                if e.type == pygame.KEYDOWN:
                    key = e.key
                elif e.type == pygame.MOUSEBUTTONDOWN:
                    key = e.button
                if key == options["input"]["droite"][1]:
                    self.inputs["droite"] = True
                    self.vx = 20
                    self.side = "droite"
                elif key == options["input"]["gauche"][1]:
                    self.inputs["gauche"] = True
                    self.vx = -20
                    self.side = "gauche"
                if key == options["input"]["z+"][1]:
                    self.z += 60
                elif key == options["input"]["z-"][1]:
                    self.z -= 60
                if key == options["input"]["sauter"][1]:
                    self.inputs["sauter"] = True
            if e.type == pygame.KEYUP or e.type == pygame.MOUSEBUTTONUP:
                if e.type == pygame.KEYUP:
                    key = e.key
                elif e.type == pygame.MOUSEBUTTONUP:
                    key = e.button
                if key == options["input"]["droite"][1]:
                    self.inputs["droite"] = False
                    if self.inputs["gauche"]:
                        self.vx = -20
                        self.side = "gauche"
                    else:
                        self.vx = 0
                elif key == options["input"]["gauche"][1]:
                    self.inputs["gauche"] = False
                    if self.inputs["droite"]:
                        self.vx = 20
                        self.side = "droite"
                    else:
                        self.vx = 0

                if key == options["input"]["sauter"][1]:
                    self.inputs["sauter"] = False



    def update(self, event, options):
        """update du joueur"""
        self.getInput(event, options)
        self.lastx = self.x
        self.lasty = self.y
        self.lastz = self.z
        if self.inputs["sauter"]:
            if self.onground:
                self.son["saut"].play()
                self.vy -= 90
                self.onground = False

##        if self.inputs["droite"] and not self.inputs["gauche"]:
##            self.vx = 20
##            self.side = "droite"
##        elif self.inputs["gauche"] and not self.inputs["droite"]:
##            self.vx = -20
##            self.side = "gauche"
##        if not self.inputs["droite"] and not self.inputs["gauche"]:
##            self.vx = 0
##
##        if self.inputs["sauter"]:
##            if self.onground:
##                self.son["saut"].play()
##                self.vy -= 90
##                self.onground = False
##        if self.inputs["z+"] and not self.inputs["z-"]:
##            self.vz = 60
##        elif self.inputs["z-"] and not self.inputs["z+"]:
##            self.vz = -60
##        else:
##            vz = 0


        self.z += self.vz
        self.z = self.z % 1530

        #calcul de la couleur de la corne
        self.color = getColor(self.z)

        #ajout de la gravité et des vitesses
        self.vy += 9.81
        self.x += self.vx
        self.y += self.vy


        if self.y > self.level.h:
            self.vy = 0
            self.y = self.level.h
            self.onground = True

        self.updateHitbox()

        #collision

        self.collisionPlatform()
        self.collisionPlatformColor()
        self.collisionPiege()
