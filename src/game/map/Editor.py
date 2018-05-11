import pygame
import time
import pygame.locals

class Editor():
    def __init__(self, fenetre):
        self.ecriture = [pygame.font.Font('../font/impact.ttf', 40)]
        self.fenetre = fenetre
        self.fond = pygame.Surface((1920, 1080))
        self.fond.fill((50,50,50))
        self.cadre = [pygame.Surface((400, 580)), pygame.Surface((360, 50))]
        self.cadre[0].fill((80,80,80))
        self.cadre[1].fill((70,70,70))

        self.image = {"sprite": 0}
        self.image["sprite"] =  pygame.image.load('../img/editeur/sprite.png')
        self.image["plus"] = self.image["sprite"].subsurface(0, 0, 100, 99)
        self.image["save"] = self.image["sprite"].subsurface(100, 0, 100, 40)
        self.image["selector"] = self.image["sprite"].subsurface(0, 0, 400, 300)
        self.image["countryside"] = self.image["sprite"].subsurface(0, 100, 100, 100)
        self.image["desert"] = self.image["sprite"].subsurface(100, 100, 100, 100)
        self.image["snow"] = self.image["sprite"].subsurface(0, 200, 100, 100)
        self.image["castle"] = self.image["sprite"].subsurface(100, 200, 100, 100)
        self.image["forest"] = self.image["sprite"].subsurface(0, 300, 100, 100)
        self.image["sugar"] = self.image["sprite"].subsurface(100, 300, 100, 100)
        self.image["border"] = self.image["sprite"].subsurface(0, 400, 100, 100)

        self.rects = {"plus": self.image["plus"].get_rect(), "save": self.image["save"].get_rect(),
        "menuMap": self.cadre[0].get_rect().move((500, 250)), "menuZone": self.cadre[0].get_rect().move((1120, 250)),
        "inputTitle": self.cadre[1].get_rect().move((780, 270)), "mapCountryside": self.image["countryside"].get_rect().move((790, 350)),
        "mapDesert": self.image["desert"].get_rect().move((910, 350)), "mapSnow": self.image["snow"].get_rect().move((1030, 350)),
        "mapCastle": self.image["castle"].get_rect().move((790, 470)), "mapForest": self.image["forest"].get_rect().move((910, 470)),
        "mapSugar": self.image["sugar"].get_rect().move((1030, 470)), "saveMap": self.image["save"].get_rect().move((910, 600))}

        self.last = False
        self.home = True
        self.editing = False
        self.creating = False
        self.title = ""
        self.selected = 0

    def loop(self):
        while self.updateMenu():
            self.renderMenu()
            while self.editing:
                while self.updateEditor():
                    self.renderEditor()
            while self.creating:
                while self.updateCreator():
                    self.renderCreator()

    def renderEditor(self):
        self.fenetre.blit(self.fond, (0,0))
        self.fenetre.blit(self.image["selector"], (0,0))

        pygame.display.flip()

    def updateEditor(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.editing = False
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                    print("GG WP")
        return True

    def renderCreator(self):
        self.fenetre.blit(self.fond, (0,0))
        self.fenetre.blit(self.cadre[0], (760, 250))
        self.fenetre.blit(self.cadre[1], (780, 270))
        titleLabel = self.ecriture[0].render(self.title, 1, (255,255,255))
        self.fenetre.blit(titleLabel, (790, 270))
        self.fenetre.blit(self.image["countryside"], (790, 350))
        self.fenetre.blit(self.image["desert"], (910, 350))
        self.fenetre.blit(self.image["snow"], (1030, 350))
        self.fenetre.blit(self.image["castle"], (790, 470))
        self.fenetre.blit(self.image["forest"], (910, 470))
        self.fenetre.blit(self.image["sugar"], (1030, 470))
        self.fenetre.blit(self.image["save"], (910, 600))

        pygame.display.flip()

    def updateCreator(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.creating = False
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.fond.get_rect().collidepoint(mouse):
                    self.selected = 0
                if self.rects["inputTitle"].collidepoint(mouse):
                    self.selected = 1
                    print(self.selected)
                elif self.rects["mapCountryside"].collidepoint(mouse):
                    self.selected = "countryside"
                elif self.rects["mapDesert"].collidepoint(mouse):
                    self.selected = "desert"
                elif self.rects["saveMap"].collidepoint(mouse):
                    self.saveMap(self.title, self.selected)
            if event.type == pygame.KEYDOWN :
                lettre = event.dict['unicode']
                if ('a' <= lettre <= 'z' or 'A' <= lettre <= 'Z') and self.selected == 1:
                    self.title = self.title + lettre
        return True

    def renderMenu(self):
        self.fenetre.blit(self.fond, (0,0))
        self.fenetre.blit(self.cadre[0], (500, 250))
        self.fenetre.blit(self.cadre[0], (1020, 250))
        self.fenetre.blit(self.image['plus'], (650, 450))
        self.fenetre.blit(self.image['plus'], (1170, 450))

        mapName = self.ecriture[0].render("Créer une Map", 1, (255,255,255))
        self.fenetre.blit(mapName, (580, 630))
        zoneName = self.ecriture[0].render("Créer une Zone", 1, (255,255,255))
        self.fenetre.blit(zoneName, (1100, 630))

        pygame.display.flip()

    def updateMenu(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rects["menuZone"].collidepoint(mouse):
                    self.editing = True
                if self.rects["menuMap"].collidepoint(mouse):
                    self.creating = True
        return True

    def saveMap(self, title, decor):
        newMap = {"limit": [0, 0, 6000, 12000]}
