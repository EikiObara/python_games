import pyxel

import util
import ball
import cat
import enemy
import random

WINDOW_H = 120
WINDOW_W = 240
CAT_H = 16
CAT_W = 16
ENEMY_H = 12
ENEMY_W = 12

ENEMY_MAX = 3

CAT_SPEED_H = 2

IMG_CAT_PATH = "assets/cat_16x16.png"
IMG_ENEMY_PATH = "assets/pyxel_logo_38x16.png"

class App:
    def __init__(self):
        # title
        pyxel.init(WINDOW_W, WINDOW_H, caption="cute cat xxx")

        # cat config
        self.CAT_ID = 0
        self.ENEMY_ID = 1

        pyxel.image(self.CAT_ID).load(0, 0, IMG_CAT_PATH)
        pyxel.image(self.ENEMY_ID).load(0, 0, IMG_ENEMY_PATH)

        self.cat = cat.Cat(self.CAT_ID, CAT_W, (WINDOW_H - CAT_H)/2, 1)
        self.balls = []
        self.enemies = []

        pyxel.run(self.update, self.draw)


    def check_collision(self, index):
        enemy_count = len(self.enemies)
        for j in range(enemy_count):
            if ((self.enemies[j].pos.x < self.balls[index].pos.x)
                and (self.balls[index].pos.x < self.enemies[j].pos.x + ENEMY_W)
                and (self.enemies[j].pos.y < self.balls[index].pos.y)
                and (self.balls[index].pos.y < self.enemies[j].pos.y + ENEMY_H)):

                del self.enemies[j]

                break



    def add_ball(self):
        new_ball = ball.Ball()

        new_ball.update(self.cat.pos.x + CAT_W / 2,
                            self.cat.pos.y + CAT_H / 2,
                            self.cat.vec,
                            new_ball.size,
                            new_ball.color)

        self.balls.append(new_ball)


    def updateBalls(self):
        for i in range(len(self.balls)):
            if 0 < self.balls[i].pos.x and self.balls[i].pos.x < WINDOW_W:
                ball_speed = self.balls[i].speed
                if self.balls[i].vec > 0:
                    ball_speed *= -1


                self.balls[i].update(self.balls[i].pos.x - ball_speed,
                    self.balls[i].pos.y,
                    self.balls[i].vec,
                    self.balls[i].size,
                    self.balls[i].color)

                   
                # self.checkCollision(i)

            else:
                del self.balls[i]
                break

    def addEnemy(self, xOffset, yOffset):
            new_enemy = enemy.Enemy(self.ENEMY_ID)
            new_enemy.update(WINDOW_W/2 + xOffset, WINDOW_H/2 + yOffset, self.cat.vec)
            self.enemies.append(new_enemy)


    def update(self):
        # keyboard event
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if self.cat.pos.y > 0 and (pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP)):
            self.cat.update(0, -CAT_SPEED_H, 1)

        if self.cat.pos.y < (WINDOW_H - CAT_H) and (pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN)):
            self.cat.update(0, CAT_SPEED_H, 1)

        if pyxel.btnp(pyxel.KEY_SPACE):
            self.add_ball()

 
        # create objects
        # ball, enemy
        if len(self.enemies) < ENEMY_MAX:
            if random.random() > 0.5:
                self.addEnemy((WINDOW_W / 2) - (ENEMY_W), ((WINDOW_H / 2) * random.random() - (ENEMY_H / 2)))
            else:
                self.addEnemy((WINDOW_W / 2) - (ENEMY_W), ((WINDOW_H / 2) * random.random() - (ENEMY_H / 2)) * -1)

        # move all objects(coordinate, direction)
        # cat, balls, enemies
        self.updateBalls()

        # judge objects collision(detection, object delete)
        # 
        


    def draw(self):
        pyxel.cls(0)

        cat_w = CAT_W
        
        if self.cat.vec > 0:
            cat_w *= -1

        pyxel.blt(self.cat.pos.x, self.cat.pos.y, self.cat.img_cat, 0, 0, cat_w, CAT_H, 5)

        for ball in self.balls:
            pyxel.circ(ball.pos.x, ball.pos.y, ball.size, ball.color)

        for enemy in self.enemies:
            enemy_direct = ENEMY_W
            if enemy.vec > 0:
                enemy_direct *= -1
            pyxel.blt(enemy.pos.x, enemy.pos.y, enemy.img_enemy, 0, 0, enemy_direct, ENEMY_H, 11)


App()
