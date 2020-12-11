import pygame, time, math, random, sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640 , 400))  # 設定介面大小
background = pygame.Surface((640, 400))  # 設定畫布大小
background.fill(( 0 , 0 , 120 ))  # 填入顏色
FPS = 60
clock = pygame.time.Clock()

class Superdonut():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isJump = False
        self.jumpCount = 10

    def draw(self):  # draw用來呼叫主角圖片
        raw_image = pygame.image.load('superdonut.png').convert_alpha()
        image = pygame.transform.scale(raw_image, (100, 100))  # 改變主角大小
        screen.blit(image,(self.x,self.y))  # 顯示主角

    def move(self):
        global bg_x
        if pressed_keys[K_RIGHT] and self.x < 540:
            self.x+= 5
        if pressed_keys[K_LEFT] and self.x > 5:
            self.x -= 5

    def jump(self):
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= self.jumpCount**2 * 0.1 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

superdonut = Superdonut(50, 270)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Start to jump by setting isJump to True.
                superdonut.isJump = True

    clock.tick(FPS)
    pressed_keys = pygame.key.get_pressed()
    screen.blit(background, (0,0))
    superdonut.move()
    superdonut.draw()
    superdonut.jump()
    pygame.display.update()