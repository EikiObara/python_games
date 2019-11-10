import util

class Enemy:
    def __init__(self, img_id):
        self.pos = util.Vec2(0,0)
        self.vec = 0
        self.speed = 0.02
        self.img_enemy = img_id

    def update(self, x, y, dx):
        self.pos.x = x
        self.pos.y = y
        self.vec = dx
