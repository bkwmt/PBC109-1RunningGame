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
        self.rect.left = WIDTH + 50
        self.rect.top = HEIGHT - GHEIGHT

    def update(self):
        if self.rect.right > -80:
            self.rect.right -= PSPEED
        if self.rect.right == -80:
            self.rect.left = WIDTH +50

class Holeedge(pg.sprite.Sprite):
    # 用來彌補視覺上的誤差（就是還沒有碰到洞卻掉了下去）
    global Direction
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((260, GHEIGHT))
        self.image.fill(BLACK)  # 暫時用黑色，之後再調成一樣。
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH
        self.rect.top = HEIGHT - GHEIGHT

    def update(self):
        if self.rect.right > -30:
            self.rect.right -= PSPEED
        if self.rect.right == -30:
            self.rect.left = WIDTH

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))      # 設定平台在某寬度與高度
        self.image.fill(CHOCOLATE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    #
    # def update(self):
    #     if self.rect.y > 0:
    #         self.rect.right -= PSPEED
    #     if self.rect.right <= 500:
    #         self.rect.right += PSPEED

class Highplatform(pg.sprite.Sprite):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((self.w, self.h))      # 設定平台在某寬度與高度
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    #
    # def update(self):
    #     if self.rect.y > 0:
    #         self.rect.right -= PSPEED
    #     if self.rect.right <= 500:
    #         self.rect.right += PSPEED
