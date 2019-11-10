import util

class Ball:
  
  def __init__(self):
    self.pos = util.Vec2(0, 0)
    self.vec = 0
    self.size = 2
    self.speed = 10
    self.color = 10 # 0 ~ 15

  def update(self, x, y, dx, size, color):
    self.pos.x = x
    self.pos.y = y
    self.vec = dx
    self.size = size
    self.color = color

