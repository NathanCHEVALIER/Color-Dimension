import pygame
from game.Game import *
from pygame.locals import *
running = True


pygame.init()
fenetre = pygame.display.set_mode((500, 500))

game = Game()
running = True
playing = True
alive = True
pause = False
last = time.time()

def event():
    global running
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
           running = False

while running:
    event()
    while playing and running:
        event()
        while alive and running and playing:
            event()
            while not pause and running and playing and alive:
                event()
                now = time.time()
                if now - last < 1/Settings.FPS:
                    time.sleep(1/Settings.FPS - (now - last))
                else:
                    last = time.time()
                    game.update()
                    game.render(fenetre)
                    pygame.display.flip()
pygame.quit()

