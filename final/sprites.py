# 所有的精靈放在這裡
import pygame as pg
from settings import *
### 向量用來製造加速與減速的感覺
vec = pg.math.Vector2

class Superdonut(pg.sprite.Sprite):
    def __init__(self, game):   # 注意這裡有來自Game裡Superdonut回傳的一個自己
        pg.sprite.Sprite.__init__(self)
        self.game = game        # 將game傳過來的指定給self.game，用來檢查與平台的碰撞
        # self.image = pg.image.load(os.path.join(img_folder, "donut0.png")).convert_alpha()
        # 圖畫得不好導致遊戲體驗不佳暫時先用下面兩行生成的小方塊測試
        self.image = pg.Surface((DONUT_W, DONUT_H))
        self.image.fill(YELLOW)     # 圖確定了就可以把這兩行刪掉
        ### 初始位置
        self.x = 50
        self.y = 100
        self.rect = self.image.get_rect()
        # self.rect.center = (self.x, self.y)
        ### 用向量來製造加減速的感覺
        self.pos = vec(self.x, self.y)
        self.vel = vec(0, 0)    # 初速度
        self.acc = vec(0, 0)    # 加速度一般為零

    def jump(self):
        # 檢查是否有站在某個平台上，有站在上面才能跳。
        # 檢查的方式是，看是否有發生碰撞：只要站在任一平台上，其實是一直有發生碰撞。
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        if hits:
            self.vel.y = JMP

    def update(self):
        self.acc = vec(0, GRAVITY)    # 初始值在y上面即有重力加速度向下
        pressed_keys = pg.key.get_pressed() # 設定按鍵
        # if pressed_keys[pg.K_RIGHT] and self.x < 1250:
        if pressed_keys[pg.K_RIGHT]:
            self.acc.x = DONUT_ACC
        # if pressed_keys[pg.K_LEFT] and self.x > 0:
        if pressed_keys[pg.K_LEFT]:
            self.acc.x = -DONUT_ACC

        ### 麻擦力與加速度（某種物理）
        self.acc.x += self.vel.x * DONUT_FRICTION
        ### 運動公式與新的位置
        self.vel += self.acc
        self.pos += self.vel + 0.5 *self.acc
        ### 確定邊界
        if self.pos.x > WIDTH - (DONUT_W / 2):
            self.pos.x = WIDTH - (DONUT_W / 2)
        if self.pos.x < (DONUT_W / 2):
            self.pos.x = (DONUT_W / 2)
        ### 取得新的位置並準備顯示（主角的中間底部位置）
        self.rect.midbottom = self.pos

        # self.x = 50
        # self.y = 450
        # self.isjump = False
        # self.jumpspeed = 15  # 跳躍初速度，之後可調整

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))      # 設定平台在某寬度與高度
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
