import random
import pygame as pg
from settings import *

class Ground(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))      # 設定地板在某寬度與高度
        self.image.fill(GOLDENROD)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Hole(pg.sprite.Sprite):
    global Direction
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((160, GHEIGHT))      # 設定洞的寬度，略低於地板
        self.image.fill(DARKSLATEBLUE)
        self.rect = self.image.get_rect()
        # self.rect.left = 3 * WIDTH + 50
        self.rect.left = WIDTH + 50
        self.rect.top = HEIGHT - GHEIGHT

    def update(self):
        if Direction == 1:
            if self.rect.right > -80:
                self.rect.right -= PSPEED
            if self.rect.right == -80:
                # 當他的最右邊到一個畫面外的位置之後，從另外一邊循環進入
                self.rect.left = 2 * WIDTH +50
        if Direction == -1:
            if self.rect.left < WIDTH + 80:
                self.rect.left += PSPEED
            if self.rect.left == WIDTH + 80:
                self.rect.right = -2 * WIDTH - 50

class Holeedge(pg.sprite.Sprite):
    # 用來彌補視覺上的誤差（就是還沒有碰到洞卻掉了下去）
    global Direction
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((260, GHEIGHT))
        self.image.fill(BLACK)  # 暫時用黑色，之後再調成一樣。
        self.rect = self.image.get_rect()
        # self.rect.left = 3 * WIDTH
        self.rect.left = WIDTH
        self.rect.top = HEIGHT - GHEIGHT

    def update(self):
        if Direction == 1:
            if self.rect.right > -30:
                self.rect.right -= PSPEED
            if self.rect.right == -30:
                self.rect.left = 2 * WIDTH
        if Direction == -1:
            if self.rect.left < WIDTH + 30:
                self.rect.left += PSPEED
            if self.rect.left == WIDTH + 30:
                self.rect.right = -2 * WIDTH

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))      # 設定平台在某寬度與高度
        self.image.fill(CHOCOLATE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.rect.right > -30:
            self.rect.right -= PSPEED


class Highplatform1(pg.sprite.Sprite):
    def __init__(self):
        self.x = random.randint(3*WIDTH + 10, 3*WIDTH + 50)
        self.y = 170 - random.randint(-10, 30)
        self.w = PW * 1.2 + (PW/random.randint(2, 5))
        self.h = THICK
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((self.w, self.h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        if self.rect.right > -30:
            self.rect.right -= 3*PSPEED
        if self.rect.right <= -30:
            self.rect.left = random.randint(WIDTH + 10, WIDTH + 50)

class Highplatform2(pg.sprite.Sprite):
    def __init__(self):
        self.x = HW + random.randint(10, 50) + \
                 random.randint(3*WIDTH + 10, 3*WIDTH + 50)
        self.y = 170 - random.randint(-10, 30)
        self.w = PW * 1.2 + (PW/random.randint(2, 5))
        self.h = THICK
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((self.w, self.h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        if self.rect.right > -30:
            self.rect.right -= 3*PSPEED
        if self.rect.right <= -30:
            self.rect.left = HW + random.randint(10, 50) + \
                             random.randint(WIDTH + 10, WIDTH + 50)

class Midplatform1(pg.sprite.Sprite):
    def __init__(self):
        self.x = HW + random.randint(2*WIDTH + 10, 2*WIDTH + 50)
        self.y = HH + random.randint(-10, 10)
        self.w = PW * 1.5 + (PW/random.randint(2, 5))
        self.h = THICK
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((self.w, self.h))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        if self.rect.right > -30:
            self.rect.right -= 2*PSPEED
        if self.rect.right == -30:
            self.rect.left = random.randint(WIDTH + 10, WIDTH + 50)

class Midplatform2(pg.sprite.Sprite):
    def __init__(self):
        self.x = WIDTH + random.randint(10, 50) + \
                 random.randint(2*WIDTH + 10, 2*WIDTH + 50)
        self.y = HH + random.randint(-10, 10)
        self.w = PW * 1.5 + (PW/random.randint(2, 5))
        self.h = THICK
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((self.w, self.h))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        if self.rect.right > -30:
            self.rect.right -= 2*PSPEED
        if self.rect.right <= -30:
            self.rect.left = HW + random.randint(10, 50) + \
                             random.randint(WIDTH + 10, WIDTH + 50)

class Lowplatform1(pg.sprite.Sprite):
    def __init__(self):
        self.x = random.randint(WIDTH + 100, WIDTH + 150)
        self.y = HEIGHT - GHEIGHT - random.randint(135, 145)
        self.w = PW * 1.2 + (PW/random.randint(2, 5))
        self.h = THICK
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((self.w, self.h))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        if self.rect.right > -30:
            self.rect.right -= PSPEED
        if self.rect.right <= -30:
            self.rect.left = random.randint(WIDTH + 100, WIDTH + 150)

class Lowplatform2(pg.sprite.Sprite):
    def __init__(self):
        self.x = HW + random.randint(10, 50) + \
                 random.randint(WIDTH + 50, WIDTH + 150)
        self.y = HEIGHT - GHEIGHT - random.randint(135, 145)
        self.w = PW * 1.2 + (PW/random.randint(2, 5))
        self.h = THICK
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((self.w, self.h))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.left = self.x
        self.rect.y = self.y

    def update(self):
        if self.rect.right > -30:
            self.rect.right -= PSPEED
        if self.rect.right == -30:
            self.rect.left = HW + random.randint(10, 50) + \
                             random.randint(WIDTH + 50, WIDTH + 150)
