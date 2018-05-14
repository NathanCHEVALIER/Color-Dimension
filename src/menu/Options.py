import pygame             ##importation des différents modules
import pygame.locals
import time
import json

class Options():

    def __init__(self, fenetre):
        """Constructeur de Menu"""
        ##place et taille de la page, donné par fenetre
        self.fenetre = fenetre
        self.text12 = pygame.font.Font('../font/impact.ttf', 40)
        self.text345 = pygame.font.Font('../font/impact.ttf', 32)
        self.text6 = pygame.font.Font('../font/impact.ttf', 60)
        self.image = {"title" : pygame.image.load('../img/menu/title2.png')}
        self.image["close"] = pygame.image.load('../img/menu/close.png')
        self.image["page"] = pygame.image.load('../img/menu/page.png')
        self.image["option1"] = pygame.image.load('../img/menu/option1.png')
        self.image["option2"] = pygame.image.load('../img/menu/option2.png')
        self.image["option3"] = pygame.image.load('../img/menu/option3.png')
        self.image["option4"] = pygame.image.load('../img/menu/option4.png')
        self.image["option5"] = pygame.image.load('../img/menu/option5.png')

        ##création et placements des images
        self.rect = {"title" : self.image["title"].get_rect().move(0, 0)}
        self.rect["close"] = self.image["close"].get_rect().move(1090, 390)
        self.rect["page"] = self.image["page"].get_rect().move(685, 440)
        self.rect["option1"] = self.image["option1"].get_rect().move(730, 472.5)
        self.rect["option2"] = self.image["option2"].get_rect().move(730, 572.5)
        self.rect["option3"] = self.image["option3"].get_rect().move(730, 672.5)
        self.rect["option4"] = self.image["option4"].get_rect().move(730, 772.5)
        self.rect["option5"] = self.image["option5"].get_rect().move(730, 872.5)

    def run(self):
        """fonction donnant la boucle qui actuallise la page 30 fois par secondee"""
        ##boucle appellant render() 30fois par seconde
        r = 0
        while r == 0:
            r = self.update()
            self.render()
            time.sleep(1/30)
        return r

    def render(self):
        """fonction appellée par run() donnant la place des éléments à actualliser"""
        self.fenetre.fill((255, 0, 255, 1))
        ##placement des images déclarées dans __init__()
        self.fenetre.blit(self.image["title"], (0, 0))
        self.fenetre.blit(self.image["close"], (1090, 390))
        self.fenetre.blit(self.image["page"], (685, 440))
        self.fenetre.blit(self.image["option1"], (730, 472.5))
        self.fenetre.blit(self.image["option2"], (730, 572.5))
        self.fenetre.blit(self.image["option3"], (730, 672.5))
        self.fenetre.blit(self.image["option4"], (730, 772.5))
        self.fenetre.blit(self.image["option5"], (730, 872.5))

        text_option1 = self.text12.render('D', 1, (242,242,242))
        self.fenetre.blit(text_option1, (1122.5, 485))
        text_option2 = self.text12.render('Q', 1, (242,242,242))
        self.fenetre.blit(text_option2, (1122.5, 585))
        text_option3 = self.text345.render('mh', 1, (242,242,242))
        self.fenetre.blit(text_option3, (1112, 687))
        text_option4 = self.text345.render('mb', 1, (242,242,242))
        self.fenetre.blit(text_option4, (1112, 785))
        text_option5 = self.text345.render("sp", 1, (242,242,242))
        self.fenetre.blit(text_option5, (1116, 885))

        ##rafraichissement d'écran
        pygame.display.flip()

    def update(self):
        """Gestion des évènements"""
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "stop"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect["close"].collidepoint(mouse):
                    return "close"
                elif self.rect["option1"].collidepoint(mouse):
                    self.setKey("gauche")
                elif self.rect["option2"].collidepoint(mouse):
                    self.setKey("droite")
                elif self.rect["option3"].collidepoint(mouse):
                    self.setKey("z+")
                elif self.rect["option4"].collidepoint(mouse):
                    self.setKey("z-")
                elif self.rect["option5"].collidepoint(mouse):
                    self.setKey("sauter")
        return 0
    def getInput(self):
        print("plapl")
        #(171, 113, 80)(174, 124, 111
        pygame.draw.rect(self.fenetre, (174, 148, 133, 1), pygame.Rect(650, 450, 620, 200))
        text = self.text6.render('Appuie sur une touche', 1, (242,242,242))
        self.fenetre.blit(text, (700, 500))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return event.type, event.button
                elif event.type == pygame.KEYDOWN:
                    return event.type, event.key
            time.sleep(1/30)


    def setKey(self, action):
        t, key = self.getInput()
        data = load()
        data["input"][action] = [t, key]
        save(data)


def load():
    file = open('../data/options.json')
    content = json.load(file)
    file.close
    return content

def save(content):
    file = open('../data/options.json', 'r+')
    file.seek(0)
    json.dump(content, file)
    file.truncate()
    file.close()