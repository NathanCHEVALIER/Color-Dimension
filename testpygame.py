from pygame import *
from pygame.locals import *

init()

fenetre = display.set_mode((1920, 1080))
fond = image.load("img/fond.jpg").convert()
unicorn = image.load("img/unicorn.png").convert_alpha()
plateforme = image.load("img/plateforme.png").convert_alpha()
pos_unicorn = unicorn.get_rect()
pos_unicorn = pos_unicorn.move(0,500)

alive = 1

key.set_repeat(30, 10)

def refresh_screen():
    fenetre.blit(fond, (0,0))
    fenetre.blit(plateforme, (100, 600))
    fenetre.blit(unicorn, pos_unicorn)
    display.flip()

while alive == 1:
    for events in event.get():
        if events.type == QUIT:
            alive = 0
        if events.type == KEYDOWN:
            if events.key == K_RIGHT:
                pos_unicorn = pos_unicorn.move(2,0)
            if events.key == K_LEFT:
                pos_unicorn = pos_unicorn.move(-2,0)
    refresh_screen()