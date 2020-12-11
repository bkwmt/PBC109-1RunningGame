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

    def donut(self):  # draw用來呼叫主角圖片
        raw_image = pygame.image.load('superdonut.png').convert_alpha()
        image = pygame.transform.scale(raw_image, (100, 100))  # 改變主角大小
        screen.blit(image,(self.x,self.y))  # 顯示主角

    def move(self):
        if pressed_keys[K_RIGHT] and self.x < 540:
            self.x+= 5
        if pressed_keys[K_LEFT] and self.x > 5:
            self.x -= 5

superdonut = Superdonut(50, 270)

while True:  # 遊戲迴圈
    clock.tick(FPS)
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                superdonut.isJump = True

    pressed_keys = pygame.key.get_pressed()
    superdonut.donut()
    superdonut.move()
    pygame.display.update()