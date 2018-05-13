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
            if(self.hitbox[0].colliderect(rect)):
                self.alive = False


    def collisionPlatform(self):
        """collision plateform normal"""
        for rect in self.map.rects["plateforme"]:
            if self.hitbox[0].colliderect(rect):
                #haut
                if self.lasty + self.hitbox[0].h <= rect.y:
                    self.y = rect.y - self.hitbox[0].h
                    self.vy = 0
                    self.onground = True
                #bas
                elif self.lasty >= rect.y + rect.h:
                    self.y = rect.y + rect.h

                #milieu
                else:
                    if self.lastx >= rect.x + (rect.w / 2):
                        self.x = rect.x + rect.w
                    elif self.lastx + self.hitbox[0].w <= rect.x + (rect.w / 2):
                        self.x = rect.x - self.hitbox[0].w
                    else:
                        print("La c'est la merde")
                self.hitbox[0].x = self.x
                self.hitbox[0].y = self.y

    def collisionPlatformColor(self):
        """collision plateform de couleur"""
        for colorPlat in self.map.rects["colorPlateforme"]:
            rect = colorPlat[0]
            z = colorPlat[1]
            if self.z <= z + 200 and self.z >= z - 200:
                if self.hitbox[0].colliderect(rect):
                    #haut
                    if self.lasty + self.hitbox[0].h <= rect.y:
                        self.y = rect.y - self.hitbox[0].h
                        self.vy = 0
                        self.onground = True
                    #bas
                    elif self.lasty >= rect.y + rect.h:
                        self.y = rect.y + rect.h
                    #milieu
                    else:
                        if self.lastx >= rect.x + (rect.w / 2):
                            self.x = rect.x + rect.w
                        elif self.lastx + self.hitbox[0].w <= rect.x + (rect.w / 2):
                            self.x = rect.x - self.hitbox[0].w
                        else:
                            print("La c'est la merde");

                    self.hitbox[0].x = self.x
                    self.hitbox[0].y = self.y
    def setMap(self, map):
        self.map = map
        self.level = self.map.posZone

