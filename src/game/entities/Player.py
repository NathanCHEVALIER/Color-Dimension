import pygame
from pygame.locals import *
from game.entities.Entity import *
from physics.AABB import *
class Player(Entity):
    def __init__(self,fenetre, x, y, z):
        Entity.__init__(self, x, y, z)
        self.fenetre = fenetre
        self.image = pygame.image.load('../img/leila.png')
        self.image = pygame.transform.scale(self.image, (100, 150))
        self.hitbox = []
        self.hitbox.append(pygame.Rect(18, 15, 82, 74))
        self.hitbox.append(pygame.Rect(18, 89, 51, 59))

        tete = pygame.Surface((82, 74))
        tete.fill((255, 0, 0, 0.5))
        corp = pygame.Surface((51, 59))
        corp.fill((0, 255, 0, 0.5))
        self.image.blit(tete, self.hitbox[0])
        self.image.blit(corp, self.hitbox[1])

    def render(self):
        self.fenetre.blit(self.image, (910, 400))
        print("x: ", self.x, "| y: ", self.y)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            self.vx = -15
        if keys[K_d]:
            self.vx = 15
        if not(keys[K_a] or keys[K_d]):
            self.vx = 0


        if keys[K_w]:
            self.y -= 60
        if keys[K_s]:
            self.y += 60

        self.x += self.vx

        if self.y < 1850:
            self.vy += 9.81 / 2
            self.y += self.vy
            if self.y > 1850:
                self.y = 1850
                self.vy = 0
