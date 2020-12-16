import pygame
import os
import pygame, time, math, random, sys
from pygame.locals import *

# define display surface            
W, H = 1250, 650
HW, HH = W / 2, H / 2
AREA = W * H

os.environ['SDL_VIDEO_WINDOW_POS'] = "50,50"
# setup pygame
pygame.init()
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((W, H)) # 設定介面大小
pygame.display.set_caption("Superdonut")
pressed_keys = pygame.key.get_pressed() # 設定按鍵
FPS = 120
ADD_FIRE_RATE = 500 #火球出現頻率

bkgd = pygame.image.load("mountains.png").convert() # 匯入背景圖


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE): # 離開方式
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN: # 跳躍方式
            if event.key == (pygame.K_SPACE):
                superdonut.isjump = True

class Fireball: #火球
    vel = 5 # 火球速度
    def __init__(self):
        self.fireball = pygame.image.load("fireball.png")
        self.fireball_rect = self.fireball.get_rect()
        self.fireball_rect.right = W
        self.fireball_rect.top = random.randint(450,600)
    
    def update(self):
        screen.blit(self.fireball, self.fireball_rect) # 建立火球

        if self.fireball_rect.left >= 0:
            self.fireball_rect.left -= self.vel # 火球自己移動

class Superdonut():
    def __init__(self):
        self.x = 50
        self.y = 450
        self.isjump = False
        self.jumpspeed = 15  # 跳躍初速度，之後可調整
        
    def donut(self):  # donut用來呼叫主角圖片
        raw_image = pygame.image.load('superdonut.png').convert_alpha()
        image = pygame.transform.scale(raw_image, (200, 200))  # 改變主角大小
        screen.blit(image,(self.x,self.y))  # 顯示主角

    def move(self):
        speed = 5  # 運動速度，之後可調整
        if pressed_keys[K_RIGHT] and self.x < 1250:
            self.x += speed
        if pressed_keys[K_LEFT] and self.x > 0:
            self.x -= speed
    
    def jump(self):
        if self.isjump == True:  # 執行跳躍
            if self.jumpspeed >= -15:
                if self.jumpspeed > 0:
                    self.y -= self.jumpspeed** 2 * 0.2 * 1
                elif self.jumpspeed < 0:
                    self.y -= self.jumpspeed** 2 * 0.2 * -1
                self.jumpspeed -= 1
            else:
                self.isjump = False
                self.jumpspeed = 15


superdonut = Superdonut()
fireball = Fireball()
fire_list = []
add_fire_rate = 0
x = 0
# main loop
while True:
    events()
    rel_x = x % bkgd.get_rect().width
    screen.blit(bkgd, (rel_x - bkgd.get_rect().width, -250)) # 捲動螢幕
    if rel_x < W:
        screen.blit(bkgd, (rel_x, -250))
    x -= 1
    pressed_keys = pygame.key.get_pressed() # 設定按鍵
    superdonut.donut()
    superdonut.move()
    superdonut.jump()
    
    add_fire_rate += 1 # 火球出現速率
    if add_fire_rate == ADD_FIRE_RATE:
        add_fire_rate = 0
        new_flame = Fireball() # 建立新火球
        fire_list.append(new_flame)
    for f in fire_list:
        if f.fireball_rect.left <= 0:
            fire_list.remove(f) # 移除火球
        f.update()
    pygame.display.flip()
    pygame.display.update()
    CLOCK.tick(FPS)
