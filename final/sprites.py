# 所有的精靈放在這裡
import random
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

# 火球（正面飛行物）
class Fireball(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        # super().__init__() 這跟上面一行是一樣的作用，下面的都刪了
        self.image = pg.image.load(os.path.join(img_folder, "fireball.png"))
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH
        self.rect.top = random.randint(50,600)

    def update(self):
        # screen.blit(self.fireball, self.fireball_rect) 不需要
        if self.rect.left > 0:
            self.rect.left -= FSPEED
        else:
            self.rect.right = WIDTH
            self.rect.top = random.randint(50,600)

# 上面掉落物
class Dropdown(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(img_folder, "apple.png"))
        self.rect = self.image.get_rect()
        self.rect.right = random.randint(50, (WIDTH - 50))
        self.rect.top = -500    # 從螢幕外掉進來

    def update(self):
        # screen.blit(self.dropdown , self.dropdown_rect) 這行不需要
        if self.rect.top < HEIGHT:
            self.rect.top += DSPEED
        else:
            self.rect.right = random.randint(50, (WIDTH - 50))
            self.rect.top = -500

# 波狀飛行物
class Strangebomb(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(img_folder, "orange.png"))
        self.image = pg.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH + 100
        self.rect.top = random.randint(150, HEIGHT - 150)

    def update(self):
        # screen.blit(self.strangebomb , self.strangebomb_rect) 這行不需要
        self.speed_x = BSPEED
        self.speed_y = (WAVE) * (AMPLITUDE) * math.sin(THETA)
        if self.rect.left >= -30:
            self.rect.left -= self.speed_x
        else:
            self.rect.left = WIDTH + 100
            self.rect.top = random.randint(150, HEIGHT - 150)

        self.rect.top -= self.speed_y
