import pygame, time, math, random, sys
from pygame.locals import *
pygame.init()
x = 1250
y = 650
screen = pygame.display.set_mode((x , y))  # 設定介面大小
background = pygame.Surface((x , y))  # 設定畫布大小
background.fill(( 0 , 0 , 120 ))  # 填入顏色(之後可調整)
FPS = 60
clock = pygame.time.Clock()
ADD_FIRE_RATE = 25


class Superdonut():
    def __init__(self):
        self.x = 50
        self.y = 500
        self.isjump = False
        self.jumpspeed = 18  # 跳躍初速度，之後可調整
        
    def donut(self):  # donut用來呼叫主角圖片
        raw_image = pygame.image.load('superdonut.png').convert_alpha()
        image = pygame.transform.scale(raw_image, (150, 150))  # 改變主角大小
        screen.blit(image,(self.x,self.y))  # 顯示主角

    def move(self):
        speed = 10  # 運動速度，之後可調整
        if pressed_keys[K_RIGHT] and self.x < 1100:
            self.x += speed
        if pressed_keys[K_LEFT] and self.x > 0:
            self.x -= speed
    
    def jump(self):
        if self.isjump == True:  # 執行跳躍
            if self.jumpspeed >= -18:
                if self.jumpspeed > 0:
                    self.y -= self.jumpspeed** 2 * 0.1 * 1
                elif self.jumpspeed < 0:
                    self.y -= self.jumpspeed** 2 * 0.1 * -1
                self.jumpspeed -= 1
            else:
                self.isjump = False
                self.jumpspeed = 18
superdonut = Superdonut()

class Fireball(pygame.sprite.Sprite):
    vel = 10
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.fireball = pygame.image.load("fireball.png")
        self.fireball_rect = self.fireball.get_rect()
        self.fireball_rect.right = x
        self.fireball_rect.top = random.randint(50,600)
    
    def update(self):
        screen.blit(self.fireball, self.fireball_rect)

        if self.fireball_rect.left > 0:
            self.fireball_rect.left -= self.vel
fireball = Fireball()
fire_list = []
add_fire_rate = 0    

class Enemy(pygame.sprite.Sprite):
    dropspeed = 10
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.enemy = pygame.image.load("apple.png")
        self.enemy_rect = self.enemy.get_rect()
        self.enemy_rect.right = random.randint(50, 1050)
        self.enemy_rect.top = 0
        
    def drop(self):
        screen.blit(self.enemy , self.enemy_rect)
        if self.enemy_rect.top < y:
            self.enemy_rect.top += self.dropspeed
        else:
            self.enemy_rect.right = random.randint(50, 1050)
            self.enemy_rect.top = 0

enemy = Enemy()


# 波狀飛行物
class Strangebomb(pygame.sprite.Sprite):    
    w = 2 * (math.pi) / 3
    amplitude = 5
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.strangebomb = pygame.image.load("orange.png")
        self.strangebomb = pygame.transform.scale(self.strangebomb, (20, 20))
        self.strangebomb_rect = self.strangebomb.get_rect()
        self.strangebomb_rect.right = x
        self.strangebomb_rect.top = random.randint(300,400)
        
    def appear(self):
        screen.blit(self.strangebomb , self.strangebomb_rect)       
        speed_x = 10
        speed_y = (self.w) * (self.amplitude) * math.sin(theta)
        if self.strangebomb_rect.left > 0:
            self.strangebomb_rect.left -= speed_x
        self.strangebomb_rect.top -= speed_y


strangebomb = Strangebomb()

theta = 0  # 波狀飛行物用
while True:  # 遊戲迴圈
    
    theta += 0.1  # 波狀飛行物用
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
    enemy.drop()
    strangebomb.appear()  # 波狀飛行物用
    pygame.display.update()
    pygame.display.flip()