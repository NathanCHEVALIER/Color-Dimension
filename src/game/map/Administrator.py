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
        self.image["countryside"] = self.image["sprite"].subsurface(0, 100, 100, 100)
        self.image["desert"] = self.image["sprite"].subsurface(100, 100, 100, 100)
        self.image["snow"] = self.image["sprite"].subsurface(0, 200, 100, 100)
        self.image["castle"] = self.image["sprite"].subsurface(100, 200, 100, 100)
        self.image["forest"] = self.image["sprite"].subsurface(0, 300,  100, 100)
        self.image["sugar"] = self.image["sprite"].subsurface(100, 300, 100, 100)
        self.image["border"] = self.image["sprite"].subsurface(0, 0, 100, 100)
        self.image["save"] = self.image["sprite"].subsurface(100, 0, 100, 40)

        self.cadres = [pygame.Surface((1920, 1080)), pygame.Surface((420, 580)), pygame.Surface((400, 470)), pygame.Surface((10, 3)),
                        pygame.Surface((400, 50)), pygame.Surface((195, 50)), pygame.Surface((195, 50))]
        self.cadres[0].fill((50, 50, 50))
        self.cadres[1].fill((80, 80, 80))
        self.cadres[2].fill((60, 60, 60))
        self.cadres[3].fill((255, 255, 255))

        self.rects = {"edit": self.image["edit"].get_rect().move((900, 750)), "create": self.image["create"].get_rect().move((770, 750)),
                        "remove": self.image["remove"].get_rect().move((1030, 750)), "countryside": self.image["countryside"].get_rect().move((780,320)),
                        "desert": self.image["desert"].get_rect().move((910,320)), "snow": self.image["snow"].get_rect().move((1040,320)),
                        "castle": self.image["castle"].get_rect().move((780,450)), "forest": self.image["forest"].get_rect().move((910,450)),
                        "sugar": self.image["sugar"].get_rect().move((1040,450)), "inputTitle": self.cadres[4].get_rect().move((760, 250)),
                        "save": self.image["save"].get_rect().move(910, 600), "inputWidth": self.cadres[5].get_rect().move((760, 310)),
                        "inputHeight": self.cadres[6].get_rect().move((965, 310)) }

        self.datas = []
        self.current = {"run": True, "type": False, "list": 0, "input": False}
        self.values = {"map": False, "title": "", "width": "", "height": ""}

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
                self.renderLevelCreating()
            elif self.current["type"] in ["worldEditing", "worldCreating"]:
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
                if self.current["type"] == False:
                    if event.key == pygame.K_UP and self.current["list"] > 0:
                        self.current["list"] -= 1
                    elif event.key == pygame.K_DOWN and self.current["list"] < len(self.datas) -1:
                        self.current["list"] += 1
                elif self.current["type"] in ["worldCreating", "worldEditing"]:
                    lettre = event.dict['unicode']
                    if ('a' <= lettre <= 'z' or 'A' <= lettre <= 'Z' or '0' <= lettre <= '9') and self.current["input"] == "title":
                        self.values["title"] = self.values["title"] + lettre
                    elif event.key == pygame.K_BACKSPACE:
                        self.values["title"] = self.values["title"][:-1]
                elif self.current["type"] in "levelCreating":
                    lettre = event.dict['unicode']
                    if ('a' <= lettre <= 'z' or 'A' <= lettre <= 'Z' or '0' <= lettre <= '9') and self.current["input"] == "title":
                        self.values["title"] = self.values["title"] + lettre
                    elif ('0' <= lettre <= '9') and self.current["input"] == "width":
                        self.values["width"] = self.values["width"] + lettre
                    elif ('0' <= lettre <= '9') and self.current["input"] == "height":
                        self.values["height"] = self.values["height"] + lettre
                    elif event.key == pygame.K_BACKSPACE:
                        self.values[self.current["input"]] = self.values[self.current["input"]][:-1]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.current["type"] == False:
                        if self.rects["edit"].collidepoint(mouse) and self.datas[self.current["list"]][1] == "level":
                            self.current["type"] = "levelEditing"
                        elif self.rects["create"].collidepoint(mouse) and self.datas[self.current["list"]][1] == "level":
                            self.values = {"map": False, "title": "", "width": "", "height": ""}
                            self.current["type"] = "levelCreating"
                        elif self.rects["create"].collidepoint(mouse) and self.datas[self.current["list"]][1] == "world":
                            self.current["type"] = "worldCreating"
                            self.values = {"title": "", "map": False}
                        elif self.rects["edit"].collidepoint(mouse) and self.datas[self.current["list"]][1] == "world":
                            self.current["type"] = "worldEditing"
                            self.values = {"title": self.datas[self.current["list"]][0], "map": self.datas[self.current["list"]][2]}
                        elif self.rects["remove"].collidepoint(mouse) and self.datas[self.current["list"]][1] == "world":
                            self.remove(self.datas[self.current["list"]][0], False)
                        elif self.rects["remove"].collidepoint(mouse) and self.datas[self.current["list"]][1] == "level":
                            self.remove(self.datas[self.current["list"]][2], self.datas[self.current["list"]][0])
                    elif self.current["type"] in ["worldCreating", "worldEditing"]:
                        if self.rects["countryside"].collidepoint(mouse):
                            self.values["map"] = "countryside"
                            self.current["input"] = False
                        elif self.rects["desert"].collidepoint(mouse):
                            self.values["map"] = "desert"
                            self.current["input"] = False
                        elif self.rects["snow"].collidepoint(mouse):
                            self.values["map"] = "snow"
                            self.current["input"] = False
                        elif self.rects["castle"].collidepoint(mouse):
                            self.values["map"] = "castle"
                            self.current["input"] = False
                        elif self.rects["forest"].collidepoint(mouse):
                            self.values["map"] = "forest"
                            self.current["input"] = False
                        elif self.rects["sugar"].collidepoint(mouse):
                            self.values["map"] = "sugar"
                            self.current["input"] = False
                        elif self.rects["inputTitle"].collidepoint(mouse):
                            self.current["input"] = "title"
                        elif self.rects["save"].collidepoint(mouse):
                            self.saveWorld(self.values["map"], self.values["title"])
                        else:
                            self.current["input"] = False
                    elif self.current["type"] == "levelCreating":
                        if self.rects["inputTitle"].collidepoint(mouse):
                            self.current["input"] = "title"
                        elif self.rects["inputWidth"].collidepoint(mouse):
                            self.current["input"] = "width"
                        elif self.rects["inputHeight"].collidepoint(mouse):
                            self.current["input"] = "height"
                        elif self.rects["save"].collidepoint(mouse):
                            self.saveLevel(self.datas[self.current["list"]][2], self.values["title"], self.values["width"], self.values["height"])
                        else:
                            self.current["input"] = False
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
        if self.current["input"] == "title":
            self.cadres[4].fill((70, 70, 70))
        else:
            self.cadres[4].fill((60, 60, 60))
        self.fenetre.blit(self.cadres[4], (760, 250))
        titleLabel = self.ecriture[0].render(str(self.values["title"]), 1, (255,255,255))
        self.fenetre.blit(titleLabel, (770, 250))

        self.fenetre.blit(self.image["countryside"], (780, 320))
        self.fenetre.blit(self.image["desert"], (910, 320))
        self.fenetre.blit(self.image["snow"], (1040, 320))
        self.fenetre.blit(self.image["castle"], (780, 450))
        self.fenetre.blit(self.image["forest"], (910, 450))
        self.fenetre.blit(self.image["sugar"], (1040, 450))
        self.fenetre.blit(self.image["save"], (910, 600))

        if self.values["map"] in ["countryside", "desert", "snow", "castle", "forest", "sugar"]:
            self.fenetre.blit(self.image["border"], (self.rects[self.values["map"]].x, self.rects[self.values["map"]].y))

        pygame.display.flip()

    def renderLevelCreating(self):
        self.fenetre.blit(self.cadres[0], (0, 0))
        self.fenetre.blit(self.cadres[1], (750, 240))

        self.cadres[4].fill((60, 60, 60))
        self.cadres[5].fill((60, 60, 60))
        self.cadres[6].fill((60, 60, 60))
        if self.current["input"] == "title":
            self.cadres[4].fill((70, 70, 70))
        elif self.current["input"] == "width":
            self.cadres[5].fill((70, 70, 70))
        elif self.current["input"] == "height":
            self.cadres[6].fill((70, 70, 70))
        self.fenetre.blit(self.cadres[4], (760, 250))
        self.fenetre.blit(self.cadres[5], (760, 310))
        self.fenetre.blit(self.cadres[6], (965, 310))

        titleLabel = self.ecriture[0].render(str(self.values["title"]), 1, (255,255,255))
        self.fenetre.blit(titleLabel, (770, 250))
        widthLabel = self.ecriture[0].render(str(self.values["width"]), 1, (255,255,255))
        self.fenetre.blit(widthLabel, (770, 310))
        heightLabel = self.ecriture[0].render(str(self.values["height"]), 1, (255,255,255))
        self.fenetre.blit(heightLabel, (970, 310))

        self.fenetre.blit(self.image["save"], (910, 600))

        pygame.display.flip()

    def loadWorlds(self):
        file = open('../data/map.json', 'r')
        content = json.load(file)
        self.datas = []
        for key in content:
            self.datas.append([key, "world", content[key]["limit"][4]])
            for cle in content[key]:
                if cle != "limit":
                    self.datas.append([cle, "level", key])
        file.close()

    def saveLevel(self, word, title, width, height):
        file = open('../data/map.json', 'r+')
        content = json.load(file)
        newMap = {"limit": [0, 0, int(width) * 100, int(height) * 50], "plateforme": {}, "piege": {}, "colorPlateforme": {}}
        content[word][title] = newMap
        file.seek(0)
        json.dump(content, file)
        file.truncate()
        file.close()
        self.loadWorlds()
        self.current["type"] = False

    def saveWorld(self, decor, title):
        file = open('../data/map.json', 'r+')
        content = json.load(file)
        if self.current["type"] == "worldEditing":
            newMap = content[self.datas[self.current["list"]][0]]
            newMap["limit"][4] = decor
            del content[self.datas[self.current["list"]][0]]
        elif self.current["type"] == "worldCreating":
            newMap = {"limit": [0, 0, 0, 0, decor]}
        content[title] = newMap
        file.seek(0)
        json.dump(content, file)
        file.truncate()
        file.close()
        self.loadWorlds()
        self.current["type"] = False

    def remove(self, world, level):
        print("remove")
        file = open('../data/map.json', 'r+')
        content = json.load(file)
        if level != False:
            del content[world][level]
        else:
            del content[world]
        file.seek(0)
        json.dump(content, file)
        file.truncate()
        file.close()
        self.loadWorlds()