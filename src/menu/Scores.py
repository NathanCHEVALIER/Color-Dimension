import json
import pygame
import pygame.locals
import time

score = 0
file = open('../data/scorelist.json', 'r+')
datascore = json.load(file)

class Scores():
    def __init__(self, fenetre):
        self.text = [pygame.font.Font('../font/impact.ttf', 54)]
        self.fenetre = fenetre
        self.image = {"title" : pygame.image.load('../img/menu/title3.png')}
        self.image["close"] = pygame.image.load('../img/menu/close.png')
        self.image["page"] = pygame.image.load('../img/menu/tabscore.png')
        self.image["scoretag"] = pygame.image.load('../img/menu/scoretag.png')

        self.rect = {"title" : self.image["title"].get_rect().move(0, 0)}
        self.rect["close"] = self.image["close"].get_rect().move(1090, 390)
        self.rect["page"] = self.image["page"].get_rect().move(685, 440)
        self.rect["scoretag"] = self.image["scoretag"].get_rect().move(750, 375)

        self.last = False

    def run(self):
        r = 0
        while r == 0:
            r = self.update()
            self.render()
            time.sleep(1/30)
        return r

    def render(self):
        self.fenetre.fill((255, 0, 255, 1))
        self.fenetre.blit(self.image["title"], (0, 0))
        self.fenetre.blit(self.image["close"], (1090, 390))
        self.fenetre.blit(self.image["page"], (685, 440))
        self.fenetre.blit(self.image["scoretag"], (750, 375))

        text_score1 = self.text[0].render(str(datascore[0]['scores']['1']), 1, (242,242,242))
        self.fenetre.blit(text_score1, (900, 525))
        text_score2 = self.text[0].render(str(datascore[0]['scores']['2']), 1, (242,242,242))
        self.fenetre.blit(text_score2, (900, 635))
        text_score3 = self.text[0].render(str(datascore[0]['scores']['3']), 1, (242,242,242))
        self.fenetre.blit(text_score3, (900, 745))



        pygame.display.flip()

    def update(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "stop"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect["close"].collidepoint(mouse):
                    return "close"
        return 0


    def score_udapte():
        if datascore[0]['scores']['3'] < score <=  datascore[0]['scores']['2']:
            datascore[0]['scores']['3'] = score
        if datascore[0]['scores']['2'] < score <=  datascore[0]['scores']['1']:
            datascore[0]['scores']['3'] = datascore[0]['scores']['2']
            datascore[0]['scores']['2'] = score
        if datascore[0]['scores']['1'] < score:
            datascore[0]['scores']['3'] = datascore[0]['scores']['2']
            datascore[0]['scores']['2'] = datascore[0]['scores']['1']
            datascore[0]['scores']['1'] = score
        file.seek(0)
        json.dump(datascore, file)
        file.truncate()
        file.close()

