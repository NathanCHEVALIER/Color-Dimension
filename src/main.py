import pygame
from game.Game import *
from pygame.locals import *
from menu.StartMenu import *


class Main():
    def __init__(self):
        pygame.init()
        self.fenetre = pygame.display.set_mode((1920, 1080))

        self.game = Game(self.fenetre, "tower")
        self.running = True

        self.playing = True
        self.pause = False
        self.last = time.time()

        while self.running:
        	self.event()
        	startmenu = StartMenu(self.fenetre, self)
        	while self.playing and self.running:
        		if not startmenu.update():
        			self.running = False
        		startmenu.render()
        		while self.game.player.alive and self.running and self.playing:
        			self.event()
        			while not self.pause and self.running and self.playing and self.game.player.alive:
        				self.event()
        				now = time.time()
        				if now - self.last < 1/Settings.FPS:
        					time.sleep(1/Settings.FPS - (now - self.last))
        				else:
        					self.last = time.time()
        					self.game.update()
        					self.fenetre.fill((255, 0, 255, 0.1))
        					self.game.render()
        					pygame.display.flip()

        pygame.quit()


    def event(self):
        global running
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False


main = Main()

