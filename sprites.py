# 所有的精靈放在這裡
import pygame as pg
from settings import *
### 向量用來製造加速與減速的感覺
vec = pg.math.Vector2

class Superdonut(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        # self.image = pg.Surface((30, 40))
        self.image = pg.image.load(os.path.join(img_folder, "donut0.png")).convert_alpha()
        # self.image.fill(YELLOW)
        self.x = 50
        self.y = 450
        self.rect = self.image.get_rect()
        ### 初始位置
        self.rect.center = (self.x, self.y)
        ### 以下用來製造加減速的感覺
        self.pos = vec(self.x, self.y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        self.acc = vec(0, 0)
        pressed_keys = pg.key.get_pressed() # 設定按鍵
        # if pressed_keys[pg.K_RIGHT] and self.x < 1250:
        if pressed_keys[pg.K_RIGHT]:
            self.acc.x = DONUT_ACC
        # if pressed_keys[pg.K_LEFT] and self.x > 0:
        if pressed_keys[pg.K_LEFT]:
            self.acc.x = -DONUT_ACC

        ### 麻擦力與加速度（某種物理）
        self.acc += self.vel * DONUT_FRICTION
        ### 運動公式與新的位置
        self.vel += self.acc
        self.pos += self.vel + 0.5 *self.acc
        ### 確定邊界
        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
        if self.pos.x < 0:
            self.pos.x = 0
        ### 取得新的位置並準備顯示
        self.rect.center = self.pos

        # self.x = 50
        # self.y = 450
        # self.isjump = False
        # self.jumpspeed = 15  # 跳躍初速度，之後可調整
