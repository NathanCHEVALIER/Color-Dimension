import pygame
import pygame.locals
import time

class Options():
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.text12 = [pygame.font.Font('../font/impact.ttf', 40)]
        self.text345 = [pygame.font.Font('../font/impact.ttf', 32)]
        self.image = {"title" : pygame.image.load('../img/menu/title3.png')}
        self.image["close"] = pygame.image.load('../img/menu/close.png')
        self.image["page"] = pygame.image.load('../img/menu/page.png')
        self.image["option1"] = pygame.image.load('../img/menu/option1.png')
        self.image["option2"] = pygame.image.load('../img/menu/option2.png')
        self.image["option3"] = pygame.image.load('../img/menu/option3.png')
        self.image["option4"] = pygame.image.load('../img/menu/option4.png')
        self.image["option5"] = pygame.image.load('../img/menu/option5.png')


        self.rect = {"title" : self.image["title"].get_rect().move(0, 0)}
        self.rect["close"] = self.image["close"].get_rect().move(1090, 390)
        self.rect["page"] = self.image["page"].get_rect().move(685, 440)
        self.rect["option1"] = self.image["option1"].get_rect().move(730, 472.5)
        self.rect["option2"] = self.image["option2"].get_rect().move(730, 572.5)
        self.rect["option3"] = self.image["option3"].get_rect().move(730, 672.5)
        self.rect["option4"] = self.image["option4"].get_rect().move(730, 772.5)
        self.rect["option5"] = self.image["option5"].get_rect().move(730, 872.5)



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
        self.fenetre.blit(self.image["option1"], (730, 472.5))
        self.fenetre.blit(self.image["option2"], (730, 572.5))
        self.fenetre.blit(self.image["option3"], (730, 672.5))
        self.fenetre.blit(self.image["option4"], (730, 772.5))
        self.fenetre.blit(self.image["option5"], (730, 872.5))

        text_option1 = self.text12[0].render('D', 1, (242,242,242))
        self.fenetre.blit(text_option1, (1122.5, 485))
        text_option2 = self.text12[0].render('Q', 1, (242,242,242))
        self.fenetre.blit(text_option2, (1122.5, 585))
        text_option3 = self.text345[0].render('mh', 1, (242,242,242))
        self.fenetre.blit(text_option3, (1112, 687))
        text_option4 = self.text345[0].render('mb', 1, (242,242,242))
        self.fenetre.blit(text_option4, (1112, 785))
        text_option5 = self.text345[0].render("sp", 1, (242,242,242))
        self.fenetre.blit(text_option5, (1116, 885))


        pygame.display.flip()

    def update(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "stop"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect["close"].collidepoint(mouse):
                    return "close"
                elif self.rect["option1"].collidepoint(mouse):
                    print("#option1")
                elif self.rect["option2"].collidepoint(mouse):
                    print("#option2")
                elif self.rect["option3"].collidepoint(mouse):
                    print("#option3")
                elif self.rect["option4"].collidepoint(mouse):
                    print("#option4")
                elif self.rect["option5"].collidepoint(mouse):
                    print("#option5")
        return 0
