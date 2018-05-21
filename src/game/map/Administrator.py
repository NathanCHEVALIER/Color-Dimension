import json
import pygame
import game
from game.map.Editor import *
import pygame.locals
from game.tools import *

class Administrator():
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.ecriture = [pygame.font.Font('../font/impact.ttf', 40), pygame.font.Font('../font/impact.ttf', 30), pygame.font.Font('../font/impact.ttf', 20)]
        self.image = {"sprite":  pygame.image.load('../img/editeur.png')}
        self.image["edit"] = self.image["sprite"].subsurface(200, 0, 120, 40)
        self.image["create"] = self.image["sprite"].subsurface(200, 50, 120, 40)
        self.image["remove"] = self.image["sprite"].subsurface(350, 0, 120, 40)

        self.cadres = [pygame.Surface((1920, 1080)), pygame.Surface((420, 580)), pygame.Surface((400, 470)), pygame.Surface((10, 3)),
                        pygame.Surface((400, 50)), pygame.Surface((195, 50))]
        self.cadres[0].fill((50, 50, 50))
        self.cadres[1].fill((80, 80, 80))
        self.cadres[2].fill((60, 60, 60))
        self.cadres[3].fill((255, 255, 255))

        self.rects = {"edit": self.image["edit"].get_rect().move((900, 750)), "create": self.image["create"].get_rect().move((770, 750)),
                        "remove": self.image["remove"].get_rect().move((1030, 750))}

        self.datas = []
        self.current = {"run": True, "type": 0, "list": 0}

        self.loadWorlds()

    def loop(self):
        ##boucle récursive appelée par le menu
        while self.updateMenu():
            if self.current["type"] == "levelEditing":
                editor = Editor(self.fenetre, self.datas[self.current["list"]][2], self.datas[self.current["list"]][0])
                while editor.update():
                    editor.render()
                self.current["type"] = False
            elif self.current["type"] == "levelCreating":
                pass
            elif self.current["type"] == "worldEditing":
                pass
            elif self.current["type"] == "worldCreating":
                self.renderWorldCreating()
            else:
                self.renderMenu()

    def updateMenu(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    Settings.changeFullScreen(self.fenetre)
                if event.key == pygame.K_UP and self.current["list"] > 0:
                    self.current["list"] -= 1
                if event.key == pygame.K_DOWN and self.current["list"] < len(self.datas) -1:
                    self.current["list"] += 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.rects["edit"].collidepoint(mouse) and self.datas[self.current["list"]][1] == "level":
                        self.current["type"] = "levelEditing"
                    if self.rects["create"].collidepoint(mouse) and self.datas[self.current["list"]][1] == "level":
                        self.current["type"] = "levelCreating"
                    if self.rects["create"].collidepoint(mouse) and self.datas[self.current["list"]][1] == "world":
                        self.current["type"] = "worldCreating"
                    if self.rects["edit"].collidepoint(mouse) and self.datas[self.current["list"]][1] == "world":
                        self.current["type"] = "worldEditing"

        return True

    def renderMenu(self):
        self.fenetre.blit(self.cadres[0], (0, 0))
        self.fenetre.blit(self.cadres[1], (750, 240))
        self.fenetre.blit(self.cadres[2], (760, 250))
        self.fenetre.blit(self.cadres[3], (765, 290 + (35 * self.current["list"])))

        self.fenetre.blit(self.image["create"], (770, 750))
        self.fenetre.blit(self.image["edit"], (900, 750))
        self.fenetre.blit(self.image["remove"], (1030, 750))

        i = 0
        c = 0
        for i in self.datas:
            if i[1] == "world":
                self.fenetre.blit(self.ecriture[1].render(i[0], 1, (255,255,255)), (780, (35 * c) + 270 ))
            elif i[1] == "level":
                self.fenetre.blit(self.ecriture[2].render(i[0], 1, (200,200,200)), (790, (35 * c) + 280 ))
            c += 1

        pygame.display.flip()

    def renderWorldCreating(self):
        self.fenetre.blit(self.cadres[0], (0, 0))
        self.fenetre.blit(self.cadres[1], (750, 240))
        self.fenetre.blit(self.cadres[4], (760, 250))

        pygame.display.flip()

    def loadWorlds(self):
        file = open('../data/map.json', 'r')
        content = json.load(file)
        for key in content:
            self.datas.append([key, "world"])
            for cle in content[key]:
                if cle != "limit":
                    self.datas.append([cle, "level", key])
        file.close()

    def createLevel(self, world):
        file = open('../data/map.json', 'r')
        content = json.load(file)
        content[world]["temp"] = []
        file.close()
