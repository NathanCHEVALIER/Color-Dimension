import pygame
from pygame.locals import *
from game.entities.Entity import *
from game.tools import *

class Player(Entity):
    def __init__(self,fenetre, x, y, z):
        Entity.__init__(self, x, y, z)
        self.fenetre = fenetre

        self.level = 0

        self.alive = True
        self.onground = False


        self.color = (255, 0, 0)

        self.side = "droite"
        self.steep = 0

        #son
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


    def render(self):
        """rendu du joueur"""
        pygame.draw.rect(self.fenetre, (255, 0, 0, 0.5), pygame.Rect(910 + 10, 400, self.hitbox.w, self.hitbox.h))
        if self.vx != 0:
            if self.side == "droite":
                pygame.draw.polygon(self.fenetre, self.color, [[978, 400], [948, 435], [975, 435]])
                self.steep = (self.steep + 1) % 30
                self.fenetre.blit(self.image["droite"][self.steep], (910, 400))
            elif self.side == "gauche":
                pygame.draw.polygon(self.fenetre, self.color, [[938, 400], [940, 435], [967, 435]])
                self.steep = (self.steep + 1) % 30
                self.fenetre.blit(self.image["gauche"][self.steep], (910, 400))
        else:
            if self.side == "droite":
                pygame.draw.polygon(self.fenetre, self.color, [[978, 400], [948, 435], [975, 435]])
                self.fenetre.blit(self.image["droite"][0], (910, 400))
            elif self.side == "gauche":
                pygame.draw.polygon(self.fenetre, self.color, [[938, 400], [940, 435], [967, 435]])
                self.fenetre.blit(self.image["gauche"][0], (910, 400))

    def update(self, event):
        """update du joueur"""
        self.lastx = self.x
        self.lasty = self.y
        self.lastz = self.z

        #input
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            self.vx = -20
            self.side = "gauche"
        if keys[K_d]:
            self.vx = 20
            self.side = "droite"
        if not(keys[K_a] or keys[K_d]):
            self.vx = 0

##        if keys[K_w]:
##            self.z += -60
##        if keys[K_s]:
##            self.z += 60
##        if self.z < 0:
##            self.z = 0
##        elif self.z > 1530:
##            self.z = 1530
        for e in event:
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 4:
                    self.z -= 102
                if e.button == 5:
                    self.z += 102
                if self.z < 0:
                    self.z = 0
                elif self.z > 1530:
                    self.z = 1530

        if keys[K_SPACE]:
            if self.onground:
                self.son["saut"].play()
                self.vy -= 90
                self.onground = False

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

        self.collisionPiege()
        self.collisionPlatform()
        self.collisionPlatformColor()

