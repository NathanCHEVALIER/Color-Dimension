import pygame
from pygame.locals import *
from game.entities.Entity import *
from physics.AABB import *

class Player(Entity):
    def __init__(self,fenetre, x, y, z):
        Entity.__init__(self, x, y, z)
        self.fenetre = fenetre

        self.level = pygame.Rect(1000, 9170, 4000, 2000)

        self.onground = False

        self.image = pygame.image.load('../img/leila.png')
        self.image = pygame.transform.scale(self.image, (100, 150))

        self.hitbox = []
        self.hitbox.append(pygame.Rect(0, 0, 100, 147))
        self.hitbox.append(pygame.Rect(18, 15, 82, 74))
        self.hitbox.append(pygame.Rect(18, 89, 51, 59))

        tete = pygame.Surface((82, 74))
        tete.fill((255, 0, 0, 0.5))
        corp = pygame.Surface((51, 59))
        corp.fill((0, 255, 0, 0.5))
        ##self.image.blit(tete, self.hitbox[0])
        ##self.image.blit(corp, self.hitbox[1])

    def render(self):
        self.fenetre.blit(self.image, (910, 400))
        ##print("x: ", self.x, "| y: ", self.y)


    def update(self):
        lastx = self.x
        lasty = self.y
        lastz = self.z

        keys = pygame.key.get_pressed()
        if keys[K_a]:
            self.vx = -20
        if keys[K_d]:
            self.vx = 20
        if not(keys[K_a] or keys[K_d]):
            self.vx = 0

        if keys[K_SPACE]:
            if self.onground:
                self.vy -= 80
                self.onground = False

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
                    #haut gauche
                    if lastx + self.hitbox[0].w <= rect.x:
                        print("Haut gauche")
                        pass
                    #haut droit
                    elif lastx >= rect.x + rect.w:
##                        print("Haut droit")
##                        a = (lastx - self.hitbox[0].x)/(lasty - self.hitbox[0].y)
##                        c = (lastx - rect.x)/(lasty - rect.y)
##                        if a < c:
##                            pass
##                        elif a > c:
##                            ny = a * (rect.x + rect.w - self.hitbox.x) + rect.y
##                        else:
##                            pass
                        pass
                    #haut millieu
                    else:
                        print("Haut milieu")
                        self.y = rect.y - self.hitbox[0].h
                        self.vy = 0
                        self.onground = True
                #bas
                elif lasty >= rect.y + rect.h:
                    print("bas")
                    if lastx + self.hitbox[0].w < rect.x:
                        pass
                    elif lastx > rect.x + rect.w:
                        pass
                    else:
                        self.y = rect.y + rect.h
                else:
                    if lastx >= rect.x + rect.w:
                        self.x = rect.x + rect.w
                    elif lastx + self.hitbox[0].w <= rect.x:
                        self.x = rect.x - self.hitbox[0].w






    def setMap(self, map):
        self.map = map