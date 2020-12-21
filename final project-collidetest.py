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
        self.rect.center = (self.x , self.y)
        self.rect.width , self.rect.height = ( 100 , 100 )
        self.isjump = False
        self.jumpspeed = 18  # 跳躍初速度，之後可調整
        
    def donut(self):  # donut用來呼叫主角圖片
        screen.blit(self.image , self.rect)  # 顯示主角

    def move(self):
        speed = 10  # 運動速度，之後可調整
        if pressed_keys[K_RIGHT] and self.x < x:
            self.rect.centerx += speed
        if pressed_keys[K_LEFT] and self.x > 0:
            self.rect.centerx -= speed
    
    def jump(self):
        if self.isjump == True:  # 執行跳躍
            if self.jumpspeed >= -18:
                if self.jumpspeed > 0:
                    self.rect.centery -= self.jumpspeed** 2 * 0.1 * 1
                elif self.jumpspeed < 0:
                    self.rect.centery += self.jumpspeed** 2 * 0.1 * 1
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
        self.rect.center = (x,random.randint(50,600))
        self.rect.width , self.rect.height = ( 30 , 30 )
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
        self.rect.center = (random.randint(50, 1050),25)
        self.rect.width , self.rect.height = ( 50 , 50 )

    def drop(self):
        screen.blit(self.enemy , self.rect)
        if self.rect.top < y:
            self.rect.centery += self.dropspeed
        else:
            self.rect.right = random.randint(50, 1050)
            self.rect.centery = 0

enemy = Enemy()

class Blood:
    def __init__(self):
        self.raw_image = pygame.image.load("blood.png")
        self.image = pygame.transform.scale(self.raw_image, (70, 70)) 
        self.now_blood = 5
        self.b_x = 0
    def show(self):
        all_blood = [self.image]*self.now_blood
        position = [ 50 , 100 , 150 , 200 , 250 ]
        for i in range (len(all_blood)):
            screen.blit( self.image , (position[i],50))
    def hurt(self):
        self.now_blood -= 1
blood = Blood()

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
    blood.show()
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
            blood.hurt()        
    if pygame.sprite.collide_rect( superdonut , enemy ):
        blood.hurt()
        #寫入遊戲結束機制or扣血
    pygame.display.update()
    pygame.display.flip()