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
ADD_FIRE_RATE = 100


class Superdonut(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.x = 50
        self.y = 500
        self.raw_image = pygame.image.load('superdonut.png').convert_alpha()
        self.image = pygame.transform.scale(self.raw_image, (150, 150))  # 改變主角大小
        self.rect = self.image.get_rect()
        self.rect.center = ( self.x + 37.5 , self.y + 37.5 )
        self.rect.left , self.rect.height = (self.x , self.y)
        self.rect.right , self.rect.bottom = (self.x + 75 , self.y +75)
        self.isjump = False
        self.jumpspeed = 18  # 跳躍初速度，之後可調整
        
    def donut(self):  # donut用來呼叫主角圖片
        screen.blit(self.image,(self.x,self.y))  # 顯示主角

    def move(self):
        speed = 10  # 運動速度，之後可調整
        if pressed_keys[K_RIGHT] and self.x < x:
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
        self.rect = self.fireball.get_rect()
        self.rect.left = x
        self.rect.top = random.randint(50,600)
        self.rect.right = x + 50
        self.rect.bottom = self.rect.top + 50
        self.rect.center = ( self.rect.left + 25 , self.rect.top + 25 )
        #self.rect = pygame.Rect(self.fireball_rect.left, self.fireball_rect.top, 50, 50)
    def update(self):
        screen.blit(self.fireball, self.rect)

        if self.rect.left > 0:
            self.rect.left -= self.vel



fireball = Fireball()
fire_list = []
add_fire_rate = 0    

class Enemy(pygame.sprite.Sprite):
    dropspeed = 10
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.enemy = pygame.image.load("apple.png")
        self.rect = self.enemy.get_rect()
        self.rect.left = random.randint(50, 1050)
        self.rect.top = 0
        self.rect.right = x + 50
        self.rect.bottom = self.rect.top + 50
        self.rect.center = ( self.rect.left + 25 , self.rect.top + 25 )

    def drop(self):
        screen.blit(self.enemy , self.rect)
        if self.rect.top < y:
            self.rect.top += self.dropspeed
        else:
            self.rect.right = random.randint(50, 1050)
            self.rect.top = 0

enemy = Enemy()

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
        if f.rect.left < 0:
            fire_list.remove(f)
        f.update()
    enemy.drop()
    for f in fire_list:
        if f.rect.colliderect(superdonut.rect):
            print("die")
            #寫入遊戲結束機制or扣血   
    if pygame.sprite.collide_rect ( superdonut , enemy ):
        print('die')
        #寫入遊戲結束機制or扣血
    pygame.display.update()
    pygame.display.flip()