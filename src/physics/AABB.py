class AABB:
    def __init__(self, x, y, z, w, h, d):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.h = h
        self.d = d

    def collide(self, aabb):
        if self.x > aabb.x + aabb.w or self.y > aabb.y + aabb.h or self.z > aabb.z + aabb.d:
            return False
        elif self.x + self.w < aabb.x or self.y + self.h < aabb.y or self.z + self.d < aabb.z:
            return False
        return True

    def collide(self, x, y, z):
        if self.x > x or self.y > y or self.z > z:
            return False
        if self.x + self.w < x or self.y + self.h < y or self.z + self.s < z:
            return False
        return True

    def render(self):
        pass
