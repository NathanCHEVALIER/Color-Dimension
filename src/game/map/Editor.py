import json
import pygame
import time
import pygame.locals

class Editor():
    def __init__(self, fenetre):
        self.ecriture = [pygame.font.Font('../font/impact.ttf', 40), pygame.font.Font('../font/impact.ttf', 30), pygame.font.Font('../font/impact.ttf', 20)]
        self.fenetre = fenetre
        self.fond = pygame.Surface((1920, 1080))
        self.fond.fill((50,50,50))
        self.cadre = [pygame.Surface((400, 500)), pygame.Surface((360, 50)), pygame.Surface((170, 50)), pygame.Surface((170, 3)), pygame.Surface((300, 1080))]
        self.cadre[0].fill((80,80,80))
        self.cadre[1].fill((70,70,70))
        self.cadre[2].fill((70,70,70))
        self.cadre[3].fill((255,255,255))
        self.cadre[4].fill((50,50,50))

        self.image = {"sprite": 0}
        self.image["sprite"] =  pygame.image.load('../img/editeur/sprite.png')
        self.image["plus"] = self.image["sprite"].subsurface(0, 0, 100, 99)
        self.image["save"] = self.image["sprite"].subsurface(100, 0, 100, 40)
        self.image["countryside"] = self.image["sprite"].subsurface(0, 100, 100, 100)
        self.image["desert"] = self.image["sprite"].subsurface(100, 100, 100, 100)
        self.image["snow"] = self.image["sprite"].subsurface(0, 200, 100, 100)
        self.image["castle"] = self.image["sprite"].subsurface(100, 200, 100, 100)
        self.image["forest"] = self.image["sprite"].subsurface(0, 300, 100, 100)
        self.image["sugar"] = self.image["sprite"].subsurface(100, 300, 100, 100)
        self.image["border"] = self.image["sprite"].subsurface(0, 400, 100, 100)
        self.image["up"] = self.image["sprite"].subsurface(300, 0, 50, 25)
        self.image["down"] = self.image["sprite"].subsurface(300, 75, 50, 25)
        self.image["right"] = self.image["sprite"].subsurface(325, 25, 25, 50)
        self.image["left"] = self.image["sprite"].subsurface(300, 25, 25, 50)
        self.image["edit"] = self.image["sprite"].subsurface(200, 0, 100, 40)
        self.image["add"] = self.image["sprite"].subsurface(200, 50, 100, 40)
        self.image["empty"] = self.image["sprite"].subsurface(100, 50, 100, 50)

        self.rects = {"plus": self.image["plus"].get_rect(), "edit": self.image["edit"].get_rect().move((850, 700)),
        "menuMap": self.cadre[0].get_rect().move((500, 250)), "menuZone": self.cadre[0].get_rect().move((1120, 250)),
        "inputTitle": self.cadre[1].get_rect().move((780, 270)), "countryside": self.image["countryside"].get_rect().move((790, 350)),
        "desert": self.image["desert"].get_rect().move((910, 350)), "snow": self.image["snow"].get_rect().move((1030, 350)),
        "castle": self.image["castle"].get_rect().move((790, 470)), "forest": self.image["forest"].get_rect().move((910, 470)),
        "sugar": self.image["sugar"].get_rect().move((1030, 470)), "save": self.image["save"].get_rect().move((910, 680)),
        "inputWidth": self.cadre[2].get_rect().move((780, 600)), "inputHeight": self.cadre[2].get_rect().move((970, 600)),
        "listUp": self.image["up"].get_rect().move((1080, 460)), "listDown": self.image["down"].get_rect().move((1080, 500)),
        "btnDown": self.image["down"].get_rect().move((1750, 975)), "btnUp": self.image["up"].get_rect().move((1750, 870)),
        "btnRight": self.image["right"].get_rect().move((1815, 910)), "btnLeft": self.image["left"].get_rect().move((1710, 910))}

        self.last = False
        self.home = True
        self.editing = False
        self.creating = False
        self.selecting = False
        self.map = {"title": "", "width": "", "height": "", "selected": ""}
        self.dataMap = {}
        self.list = []
        self.mapSelected = 0
        self.inputSelected = 0
        self.listSelected = 0
        self.camPos = {"x": 5, "y": 9}
        self.current = {}
        self.cases = []

    def loop(self):
        while self.updateMenu():
            self.renderMenu()
            while self.editing:
                while self.updateEditor():
                    self.renderEditor()
            while self.creating:
                while self.updateCreator():
                    self.renderCreator()
            while self.selecting:
                file = open('../data/map.json', 'r')
                content = json.load(file)
                for key in content:
                    self.list.append([key, "map"])
                    for cle in content[key]:
                        if cle != "limit":
                            self.list.append([cle, "zone", key])
                file.close()

                while self.updateSelector():
                    self.renderSelector()

    def initEditor(self):
        file = open('../data/map.json', 'r+')
        self.dataMap = json.load(file)
        file.close()
        self.image["background"] = pygame.Surface((self.dataMap[self.current[0]][self.current[1]]["limit"][2] + 2000, self.dataMap[self.current[0]][self.current[1]]["limit"][3] + 2000))
        self.image["background"].fill((255,255,126))
        self.image["zone"] = pygame.Surface((self.dataMap[self.current[0]][self.current[1]]["limit"][2], self.dataMap[self.current[0]][self.current[1]]["limit"][3]))
        self.image["zone"].fill((255,0,0))

        self.cases = [["empty"] * int(self.dataMap[self.current[0]][self.current[1]]["limit"][2] / 100) for i in range(int(self.dataMap[self.current[0]][self.current[1]]["limit"][3] / 50))]

    def renderEditor(self):
        self.fenetre.blit(self.fond, (0,0))
        self.fenetre.blit(self.image["background"], (self.camPos["x"] * -100, self.camPos["y"] * -100))
        self.image["background"].blit(self.image["zone"], (1000, 1000))

        for i in range(0, len(self.cases)):
            for c in range(0, len(self.cases[i])):
                self.image["zone"].blit(self.image[self.cases[i][c]], (c * 100, i*50))

        self.fenetre.blit(self.cadre[4], (0,0))
        pygame.draw.circle(self.fenetre, (130,130,130), (1775, 935), 75)
        self.fenetre.blit(self.image["up"], (1750, 870))
        self.fenetre.blit(self.image["down"], (1750, 975))
        self.fenetre.blit(self.image["left"], (1710, 910))
        self.fenetre.blit(self.image["right"], (1815, 910))

        pygame.display.flip()

    def updateEditor(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.editing = False
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rects["btnDown"].collidepoint(mouse):
                    self.camPos["y"] += 1
                elif self.rects["btnUp"].collidepoint(mouse) and self.camPos["y"] >= 0:
                    self.camPos["y"] -= 1
                elif self.rects["btnRight"].collidepoint(mouse) and self.camPos["x"] <= self.dataMap[self.current[0]]["limit"][3]:
                    self.camPos["x"] += 1
                elif self.rects["btnLeft"].collidepoint(mouse) and self.camPos["x"] >= 0:
                    self.camPos["x"] -= 1
                else:
                    mousePos = pygame.mouse.get_pos()
                    self.cases[int(((self.camPos["y"] * 100) + mousePos[1] - 1000) / 50)][int(((self.camPos["x"] * 100) + mousePos[0] - 1000) / 100)] = "save"

        return True

    def renderSelector(self):
        self.fenetre.blit(self.fond, (0,0))
        self.fenetre.blit(self.cadre[0], (760, 250))
        self.fenetre.blit(self.image["up"], (1080, 460))
        self.fenetre.blit(self.image["down"], (1080, 500))
        self.fenetre.blit(self.image["edit"], (850, 700))
        self.fenetre.blit(self.image["add"], (970, 700))
        self.fenetre.blit(self.cadre[3], (780, 300 + (35 * self.listSelected)))
        i = 0
        c = 0
        for i in self.list:
            if i[1] == "map":
                self.fenetre.blit(self.ecriture[1].render(i[0], 1, (255,255,255)), (790, (35 * c) + 270 ))
            elif i[1] == "zone":
                self.fenetre.blit(self.ecriture[2].render(i[0], 1, (255,255,255)), (800, (35 * c) + 280 ))
            c += 1

        pygame.display.flip()

    def updateSelector(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.selecting = False
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rects["listUp"].collidepoint(mouse) and self.listSelected > 0:
                    self.listSelected = self.listSelected - 1
                if self.rects["listDown"].collidepoint(mouse):
                    self.listSelected = self.listSelected + 1
                if self.rects["edit"].collidepoint(mouse):
                    if self.list[self.listSelected][1] == "zone":
                        self.current[0] = self.list[self.listSelected][2]
                        self.current[1] = self.list[self.listSelected][0]
                        self.initEditor()
                        self.selecting = False
                        self.editing = True
                        return False

        return True

    def renderCreator(self):
        self.fenetre.blit(self.fond, (0,0))
        self.fenetre.blit(self.cadre[0], (760, 250))
        if self.inputSelected == 1:
            self.cadre[1].fill((90,90,90))
        else:
            self.cadre[1].fill((70,70,70))

        self.fenetre.blit(self.cadre[1], (780, 270))
        self.fenetre.blit(self.cadre[2], (780, 600))
        self.fenetre.blit(self.cadre[2], (970, 600))
        titleLabel = self.ecriture[0].render(self.map["title"], 1, (255,255,255))
        self.fenetre.blit(titleLabel, (790, 270))
        widthLabel = self.ecriture[0].render(self.map["width"], 1, (255,255,255))
        self.fenetre.blit(widthLabel, (790, 600))
        heightLabel = self.ecriture[0].render(self.map["height"], 1, (255,255,255))
        self.fenetre.blit(heightLabel, (980, 600))
        self.fenetre.blit(self.image["countryside"], (790, 350))
        self.fenetre.blit(self.image["desert"], (910, 350))
        self.fenetre.blit(self.image["snow"], (1030, 350))
        self.fenetre.blit(self.image["castle"], (790, 470))
        self.fenetre.blit(self.image["forest"], (910, 470))
        self.fenetre.blit(self.image["sugar"], (1030, 470))
        self.fenetre.blit(self.image["save"], (910, 680))
        if self.map["selected"] != "":
            self.fenetre.blit(self.image["border"], (self.rects[ self.map["selected"] ].x, self.rects[self.map["selected"]].y))

        pygame.display.flip()

    def updateCreator(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.creating = False
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.fond.get_rect().collidepoint(mouse):
                    self.inputSelected = 0
                if self.rects["inputTitle"].collidepoint(mouse):
                    self.inputSelected = 1
                elif self.rects["inputWidth"].collidepoint(mouse):
                    self.inputSelected = 2
                elif self.rects["inputHeight"].collidepoint(mouse):
                    self.inputSelected = 3
                elif self.rects["countryside"].collidepoint(mouse):
                    self.map["selected"] = "countryside"
                elif self.rects["desert"].collidepoint(mouse):
                    self.map["selected"] = "desert"
                elif self.rects["snow"].collidepoint(mouse):
                    self.map["selected"] = "snow"
                elif self.rects["castle"].collidepoint(mouse):
                    self.map["selected"] = "castle"
                elif self.rects["forest"].collidepoint(mouse):
                    self.map["selected"] = "forest"
                elif self.rects["sugar"].collidepoint(mouse):
                    self.map["selected"] = "sugar"
                elif self.rects["save"].collidepoint(mouse):
                    self.saveMap()
                    return False
            if event.type == pygame.KEYDOWN :
                lettre = event.dict['unicode']
                if ('a' <= lettre <= 'z' or 'A' <= lettre <= 'Z') and self.inputSelected == 1:
                    self.map["title"] = self.map["title"] + lettre
                if ('0' <= lettre <= '9') and self.inputSelected == 2:
                    self.map["width"] = self.map["width"] + lettre
                if ('0' <= lettre <= '9') and self.inputSelected == 3:
                    self.map["height"] = self.map["height"] + lettre
        return True

    def renderMenu(self):
        self.fenetre.blit(self.fond, (0,0))
        self.fenetre.blit(self.cadre[0], (500, 250))
        self.fenetre.blit(self.cadre[0], (1020, 250))
        self.fenetre.blit(self.image['plus'], (650, 420))
        self.fenetre.blit(self.image['plus'], (1170, 420))

        mapName = self.ecriture[0].render("Créer une Map", 1, (255,255,255))
        self.fenetre.blit(mapName, (580, 550))
        zoneName = self.ecriture[0].render("Créer une Zone", 1, (255,255,255))
        self.fenetre.blit(zoneName, (1100, 550))

        pygame.display.flip()

    def updateMenu(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rects["menuZone"].collidepoint(mouse):
                    self.selecting = True
                if self.rects["menuMap"].collidepoint(mouse):
                    self.creating = True
        return True

    def saveMap(self):
        file = open('../data/map.json', 'r+')
        content = json.load(file)
        newMap = {"limit": [0, 0, int(self.map["width"]) * 100 + 2000, int(self.map["height"]) * 50 + 2000, self.map["selected"]],
        "Z0": {"limite": [1000,1000, int(self.map["width"]) * 100, int(self.map["height"]) * 50]}}
        content[self.map["title"]] = newMap
        file.seek(0)
        json.dump(content, file)
        file.truncate()
        file.close()
        self.creating = False

    def setCamera(self, x, y):
        pos = self.fond.get_rect()
        pos = pos.move(-x, -y)
        self.level.blit(self.zone, self.posZone)
        self.fenetre.blit(self.level, pos)
        pygame.display.flip()