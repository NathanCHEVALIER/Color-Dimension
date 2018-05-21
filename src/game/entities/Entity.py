"""Classe entity dont Player et Monster herite, on ne créra pas d'instance de cette classe """
class Entity:
    def __init__(self, x, y, z, vx, vy, vz):
        """constructeur avec les vitesses"""
        self.x = x
        self.z = z
        self.y = y
        self.vx = vx
        self.vz = vz
        self.vy = vy

    def __init__(self, x, y, z):
        """constructeur sans les vitesses"""
        self.x = x
        self.z = z
        self.y = y
        self.vx = 0
        self.vz = 0
        self.vy = 0

    def render():
        """on définie une fonction render vide pour pouvoir appeler render sur tous les objet qui sont des instance
        d'une classe héritant de entity meme si cette classe de redéfinie pas render"""
        pass

    def update():
        """on définie une fonction update vide pour pouvoir appeler update sur tous les objet qui sont des instance
        d'une classe héritant de entity meme si cette classe de redéfinie pas updater"""

    def collisionPiege(self):
        """collision piège"""
        for rect in self.map.rects["piege"]:
            if(self.hitbox.colliderect(rect)):
                self.alive = False

    def updateHitbox(self):
        """reposition de la hitbox"""
        self.hitbox.x = self.x + 10
        self.hitbox.y = self.y

    def collisionPlatform(self):
        """collision plateform normal"""
        for rect in self.map.rects["plateforme"]:
            self.collisionRect(rect)

    def collisionPlatformColor(self):
        """collision plateform de couleur"""
        for colorPlat in self.map.rects["colorPlateforme"]:
            rect = colorPlat[0]
            z = colorPlat[1]
            if (self.z <= z + 200 and self.z >= z - 200) or ((self.z <= (z + 200) % 1530 + 1530) and (self.z >= (z - 200) % 1530)):
                self.collisionRect(rect)

    def collisionRect(self, rect):
        if self.hitbox.colliderect(rect):
            #haut
            if self.lasty + self.hitbox.h <= rect.y:
                if self.vy > 110:
                    self.alive = False
                self.y = rect.y - self.hitbox.h
                self.vy = 0
                self.onground = True
            #bas
            elif self.lasty >= rect.y + rect.h:
                self.y = rect.y + rect.h
            #milieu
            else:
                if self.lastx >= rect.x + (rect.w / 2):
                    self.x = rect.x + rect.w
                elif self.lastx + self.hitbox.w <= rect.x + (rect.w / 2):
                    self.x = rect.x - self.hitbox.w
                else:
                    print("La c'est la merde");
            self.updateHitbox()


    def setMap(self, map):
        """defini la map de l'entité"""
        self.map = map
        self.level = self.map.posZone

