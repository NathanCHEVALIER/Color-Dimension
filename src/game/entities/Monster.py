import pygame
from pygame.locals import *
from game.entities.Entity import *
from physics.AABB import *

class Monster(Entity):
    def __init__(self,fenetre, x, y, z):
        Entity.__init__(self, x, y, z)
        self.fenetre = fenetre
        self.level = pygame.Rect(1000, 9170, 4000, 2000)

        self.onground = False
        self.color = (255, 0, 0)


        #image pour le rendu
        self.image = {"droite": pygame.image.load('../img/monster.png')}
        self.image["gauche"] = pygame.image.load('../img/monster2.png')
        self.image["droite"] = pygame.transform.scale(self.image["droite"], (100, 150))
        self.image["gauche"] = pygame.transform.scale(self.image["gauche"], (100, 150))

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

    def render(self, x, y):
        if self.vx >= 0:
            pygame.draw.polygon(self.fenetre, self.color, [[973, 401], [948, 430], [971, 430]])
            self.fenetre.blit(self.image["droite"], (x, y))
        else:
            pygame.draw.polygon(self.fenetre, self.color, [[946, 401], [948, 430], [971, 430]])
            self.fenetre.blit(self.image["gauche"], (x, y))


    def update(self):
        lastx = self.x
        lasty = self.y
        lastz = self.z



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

    def setMap(self, map):
        self.map = map