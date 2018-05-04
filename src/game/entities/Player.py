import pygame
from pygame.locals import *
from game.entities.Entity import *
from physics.AABB import *

class Player(Entity):
    def __init__(self,fenetre, x, y, z):
        Entity.__init__(self, x, y, z)
        self.fenetre = fenetre

        self.level = pygame.Rect(1000, 9170, 4000, 2000)

        self.alive = True
        self.onground = False

        self.color = (255, 0, 0)

        #image pour le rendu
        self.image = {"droite": pygame.image.load('../img/leila.png')}
        self.image["gauche"] = pygame.image.load('../img/leila2.png')
        self.image["droite"] = pygame.transform.scale(self.image["droite"], (100, 150))
        self.image["gauche"] = pygame.transform.scale(self.image["gauche"], (100, 150))

        #rect pour les couleur de la corne

        #rect pour les collisions
        self.hitbox = []
        self.hitbox.append(pygame.Rect(0, 0, 100, 148))
        self.hitbox.append(pygame.Rect(18, 15, 82, 74))
        self.hitbox.append(pygame.Rect(18, 89, 51, 59))

        #rendu pour les hitbox pour les voir
        tete = pygame.Surface((82, 74))
        tete.fill((255, 0, 0, 0.5))
        corp = pygame.Surface((51, 59))
        corp.fill((0, 255, 0, 0.5))
        ##self.image.blit(tete, self.hitbox[0])
        ##self.image.blit(corp, self.hitbox[1])

    def render(self):
        if self.vx >= 0:
            pygame.draw.polygon(self.fenetre, self.color, [[973, 401], [948, 430], [971, 430]])
            self.fenetre.blit(self.image["droite"], (910, 400))
        else:
            pygame.draw.polygon(self.fenetre, self.color, [[946, 401], [948, 430], [971, 430]])
            self.fenetre.blit(self.image["gauche"], (910, 400))


    def update(self):
        lastx = self.x
        lasty = self.y
        lastz = self.z

        #input
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            self.vx = -20
        if keys[K_d]:
            self.vx = 20
        if not(keys[K_a] or keys[K_d]):
            self.vx = 0

        if keys[K_w]:
            self.z += -60
        if keys[K_s]:
            self.z += 60
        if self.z < 0:
            self.z = 0
        elif self.z > 1530:
            self.z = 1530


        if keys[K_SPACE]:
            if self.onground:
                self.vy -= 90
                self.onground = False

        #calcul de la couleur de la corne
        r = 0
        g = 0
        b = 0
        if self.z < 255:
            r = 255
            g = self.z
            b = 0
        elif self.z < 510:
            r = 510 - self.z
            g = 255
            b = 0
        elif self.z < 765:
            r = 0
            g = 255
            b = self.z - 510
        elif self.z < 1020:
            r = 0
            g = 1020 - self.z
            b = 255
        elif self.z < 1275:
            r = self.z - 1020
            g = 0
            b = 255
        else:
            r = 255
            g = 0
            b = 1530 - self.z
        self.color = (r, g, b);

        #ajout de la gravité et des vitesses
        self.vy += 9.81
        self.x += self.vx
        self.y += self.vy

        if self.y > self.level.h:
            self.vy = 0
            self.y = self.level.h
            self.onground = True

        self.hitbox[0].x = self.x
        self.hitbox[0].y = self.y

        #collision piège
        for rect in self.map.rects["piege"]:
            if(self.hitbox[0].colliderect(rect)):
                self.alive = False

        #collision plateform normal
        for rect in self.map.rects["plateforme"]:
            if self.hitbox[0].colliderect(rect):
                #haut
                if lasty + self.hitbox[0].h <= rect.y:
                    self.y = rect.y - self.hitbox[0].h
                    self.vy = 0
                    self.onground = True
                #bas
                elif lasty >= rect.y + rect.h:
                    self.y = rect.y + rect.h

                #milieu
                else:
                    if lastx >= rect.x + (rect.w / 2):
                        self.x = rect.x + rect.w
                    elif lastx + self.hitbox[0].w <= rect.x + (rect.w / 2):
                        self.x = rect.x - self.hitbox[0].w
                    else:
                        print("La c'est la merde");

                self.hitbox[0].x = self.x
                self.hitbox[0].y = self.y

        #collision plateform de couleur
        for colorPlat in self.map.rects["colorPlateforme"]:
            rect = colorPlat[0]
            z = colorPlat[1]
            if self.z <= z + 200 and self.z >= z - 200:
                if self.hitbox[0].colliderect(rect):
                    #haut
                    if lasty + self.hitbox[0].h <= rect.y:
                        self.y = rect.y - self.hitbox[0].h
                        self.vy = 0
                        self.onground = True
                    #bas
                    elif lasty >= rect.y + rect.h:
                        self.y = rect.y + rect.h

                    #milieu
                    else:
                        if lastx >= rect.x + (rect.w / 2):
                            self.x = rect.x + rect.w
                        elif lastx + self.hitbox[0].w <= rect.x + (rect.w / 2):
                            self.x = rect.x - self.hitbox[0].w
                        else:
                            print("La c'est la merde");

                    self.hitbox[0].x = self.x
                    self.hitbox[0].y = self.y
        ##print("x: ", self.x, " y :", self.y);

    def setMap(self, map):
        self.map = map