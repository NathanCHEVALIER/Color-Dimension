
class Map:
    def __init__(self):
        self.blocks = []
        self.enemies = []

    def update(self):
        for e in self.enemies:
            e.update()
    def render(self, fenetre):
        for e in self.enemies:
            e.render(fenetre)

    def loadMap(self, source):
        pass
