import pygame
import sys
import random 
from pygame.locals import *

pygame.init()

WIDTH = 640
HEIGHT = 480
size = (WIDTH, HEIGHT)
bgcolor = ( 0 , 0 , 120 )

screen = pygame.display.set_mode(size)  # 設定介面大小
background = pygame.Surface((WIDTH, HEIGHT))  # 設定畫布大小
background.fill(bgcolor)  # 填入顏色

FPS = 60
clock = pygame.time.Clock()

class Enemy():
    def drop(self):
        dropimg = pygame.image.load("apple.png")
        drop_x = random.randint(0, WIDTH)
        drop_y = -80
        dropspeed = 2
        while drop_y < HEIGHT:
            drop_y += dropspeed
            screen.fill(bgcolor)
            screen.blit(dropimg, (drop_x, drop_y))
            pygame.display.flip()
            clock.tick(FPS)

enemy = Enemy()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    enemy.drop()

