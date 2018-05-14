class Entity:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.z = z
        self.y = y
        self.vx = vx
        self.vz = vz
        self.vy = vy

    def __init__(self, x, y, z):
        self.x = x
        self.z = z
        self.y = y
        self.vx = 0
        self.vz = 0
        self.vy = 0

    def render():
        pass

    def update():
        pass

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
            if self.hitbox.colliderect(rect):
                #haut
                if self.lasty + self.hitbox.h <= rect.y:
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
                        print("La c'est la merde")
                self.updateHitbox()

    def collisionPlatformColor(self):
        """collision plateform de couleur"""
        for colorPlat in self.map.rects["colorPlateforme"]:
            rect = colorPlat[0]
            z = colorPlat[1]
            if self.z <= z + 200 and self.z >= z - 200:
                if self.hitbox.colliderect(rect):
                    #haut
                    if self.lasty + self.hitbox.h <= rect.y:
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

