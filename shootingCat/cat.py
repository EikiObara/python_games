import pyxel
import util

class Cat:
    def __init__(self, img_id, x, y, direction):
        self.pos = util.Vec2(x, y)
        self.vec = direction
        self.img_cat = img_id

    def update(self, x, y, dx):
        self.pos.x += x
        self.pos.y += y
        self.vec = dx
