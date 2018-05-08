import pygame
import pygame.locals

class Options():
    def __init__(self, fenetre, main):
        self.fenetre = fenetre
        self.main = main
        self.image = {"title" : pygame.image.load('../img/menu/title2.png')}
        self.image["close"] = pygame.image.load('../img/menu/close.png')
        self.image["page"] = pygame.image.load('../img/menu/page.png')
        self.image["option1"] = pygame.image.load('../img/menu/option1.png')
        self.image["option2"] = pygame.image.load('../img/menu/option2.png')
        self.image["option3"] = pygame.image.load('../img/menu/option3.png')
        self.image["option4"] = pygame.image.load('../img/menu/option4.png')
        self.image["option5"] = pygame.image.load('../img/menu/option5.png')

        self.rect = {"title" : self.image["title"].get_rect().move(0, 0)}
        self.rect["close"] = self.image["close"].get_rect().move(1120, 340)
        self.rect["page"] = self.image["page"].get_rect().move(685, 400)
        self.rect["option1"] = self.image["option1"].get_rect().move(730, 432.5)
        self.rect["option2"] = self.image["option2"].get_rect().move(730, 532.5)
        self.rect["option3"] = self.image["option3"].get_rect().move(730, 632.5)
        self.rect["option4"] = self.image["option4"].get_rect().move(730, 732.5)
        self.rect["option4"] = self.image["option5"].get_rect().move(730, 832.5)

        #self.rect = {"option" : pygame.Rect(500, 400)}
        self.last = False

    def render(self):
        self.fenetre.fill((255, 0, 255, 1))
        self.fenetre.blit(self.image["title"], (0, 0))
        self.fenetre.blit(self.image["close"], (1120, 340))
        self.fenetre.blit(self.image["page"], (685, 400))
        self.fenetre.blit(self.image["option1"], (730, 432.5))
        self.fenetre.blit(self.image["option2"], (730, 532.5))
        self.fenetre.blit(self.image["option3"], (730, 632.5))
        self.fenetre.blit(self.image["option4"], (730, 732.5))
        self.fenetre.blit(self.image["option5"], (730, 832.5))

        pygame.display.flip()

    def update(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect["close"].collidepoint(mouse):
                    self.menu.StartMenu()
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

        return True
