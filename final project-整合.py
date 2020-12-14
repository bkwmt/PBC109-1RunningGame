import pygame, time, math, random, sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640 , 400))  # 設定介面大小
background = pygame.Surface((640, 400))  # 設定畫布大小
background.fill(( 0 , 0 , 120 ))  # 填入顏色
FPS = 60
clock = pygame.time.Clock()
ADD_FIRE_RATE = 25
x = 640
y = 480

class Superdonut():
    def __init__(self):
        self.x = 50
        self.y = 270
        self.isjump = False
        self.jumpspeed = 15  # 跳躍初速度，之後可調整
        
    def donut(self):  # donut用來呼叫主角圖片
        raw_image = pygame.image.load('superdonut.png').convert_alpha()
        image = pygame.transform.scale(raw_image, (100, 100))  # 改變主角大小
        screen.blit(image,(self.x,self.y))  # 顯示主角

    def move(self):
        speed = 5  # 運動速度，之後可調整
        if pressed_keys[K_RIGHT] and self.x < 560:
            self.x += speed
        if pressed_keys[K_LEFT] and self.x > 0:
            self.x -= speed
    
    def jump(self):
        if self.isjump == True:  # 執行跳躍
            if self.jumpspeed >= -15:
                if self.jumpspeed > 0:
                    self.y -= self.jumpspeed** 2 * 0.1 * 1
                elif self.jumpspeed < 0:
                    self.y -= self.jumpspeed** 2 * 0.1 * -1
                self.jumpspeed -= 1
            else:
                self.isjump = False
                self.jumpspeed = 15
superdonut = Superdonut()

class Fireball:
    vel = 10
    def __init__(self):
        self.fireball = pygame.image.load("fireball.png")
        self.fireball_rect = self.fireball.get_rect()
        self.fireball_rect.right = x
        self.fireball_rect.top = random.randint(50,460)
    
    def update(self):
        screen.blit(self.fireball, self.fireball_rect)

        if self.fireball_rect.left > 0:
            self.fireball_rect.left -= self.vel
fireball = Fireball()
fire_list = []
add_fire_rate = 0    
while True:  # 遊戲迴圈
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == (pygame.K_SPACE):
                superdonut.isjump = True
    clock.tick(FPS)
    pressed_keys = pygame.key.get_pressed()
    screen.blit(background, (0,0))
    superdonut.donut()
    superdonut.move()
    superdonut.jump()
    add_fire_rate += 1
    if add_fire_rate == ADD_FIRE_RATE:
        add_fire_rate = 0
        new_flame = Fireball()
        fire_list.append(new_flame)
    for f in fire_list:
        if f.fireball_rect.left < 0:
            fire_list.remove(f)
        f.update()
    pygame.display.update()
    pygame.display.flip()