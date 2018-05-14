﻿from . import entities
from .entities.Player import *
from .map.Map import *
from .map.Editor import *
from ..menu.Options import *
from . import map
from .settings import *
import time


class Game:
    def __init__(self, fenetre, mapId):
        self.fenetre = fenetre
        self.player = Player(self.fenetre, 2000, 1700, 0)
        self.mapId = mapId
        self.map = Map(self.fenetre, self.player, self.mapId)
        self.editor = Editor(self.fenetre)
        self.player.setMap(self.map)

        #enemies
        self.enemies = []
        self.enemies.append(Monster(self.fenetre, 3000, 1000, 0, self.player))
        self.enemies[0].setMap(self.map)

        #son
        self.music = pygame.mixer.Sound("../music/musique.wav")

        self.event = []
        #etat
        self.pause = False
        self.running = True

    def run(self):
        self.options = menu.Options.load()

        self.music.play()
        last = 0
        while self.running:
            while not self.pause and self.player.alive:
                now = time.time()
                if now - last < 1/Settings.FPS:
                    time.sleep(1/Settings.FPS - (now - last))
                else:
                    last = time.time()
                    r = self.getEvent()
                    if r == "stop":
                        return "stop"
                    self.update()
                    self.fenetre.fill((255, 0, 255, 0.1))
                    self.render()
                    pygame.display.flip()
            if self.pause:
                pause = Pause(self.fenetre)
                r = pause.run()
                if r == "reprendre":
                    self.setOffPause()
                elif r == "startmenu":
                    self.exit()
                    self.setOffPause()
                    return "startmenu"
                elif r == "stop":
                    self.exit()
                    return "stop"
            elif not self.player.alive:
                gameover = GameOver(self.fenetre)
                r = gameover.run()
                if r == "respawn":
                    self.respawn()
                elif r == "startmenu":
                    self.exit()
                    return "startmenu"
                elif r == "stop":
                    self.exit()
                    return "stop"
        self.exit()
        return "startmenu"

    def exit(self):
        self.music.stop()

    def setOnPause(self):
        self.pause = True

    def setOffPause(self):
        self.pause = False

    def getEvent(self):
        self.event = pygame.event.get()
        for e in self.event:
            if e.type == pygame.QUIT:
                return "stop"
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            self.setOnPause()

    def render(self):
        """rendu de la map et du joueur"""
        self.map.setCamera(self.player.x - 910 + self.player.level.x , self.player.y - 400 + self.player.level.y)
        self.map.render()
        for e in self.enemies:
            e.render(e.x - self.player.x + 910, e.y - self.player.y + 400)
        self.player.render()

    def update(self):
        """update de la map et du joueur"""
        self.map.update()
        for e in self.enemies:
            e.update()
        self.player.update(self.event, self.options)

    def respawn(self):
        """remet le joeur à sa position de depart"""
        self.player.x = 2000
        self.player.y = 1700
        self.player.z = 0
        self.player.alive = True