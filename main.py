import os, time, math, random, sys
import pygame as pg
from pygame.locals import *
from settings import *
from sprites import *

# 視窗環境設定
os.environ['SDL_VIDEO_WINDOW_POS'] = "50,50"

class Game:
    def __init__(self):
        # 初始化遊戲
        pg.init()           # 起手式
        pg.mixer.init()     # 有用聲音的起手式
        self.screen = pg.display.set_mode(SIZE)  # 設定介面大小
        pg.display.set_caption(TITLE)
        self.bkgd = pg.image.load("mountains.png").convert() # 匯入背景圖
        # self.background = pg.Surface(SIZE)  # ??跟screen有何不同
        # self.background.fill(( 0 , 0 , 120 ))  # 塗滿(之後可調整)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # 重新開始一個遊戲
        self.all_sprites = pg.sprite.Group()    # 初始化全部精靈群組
        self.donut = Superdonut()
        self.all_sprites.add(self.donut)
        self.run()  # 執行遊戲

    def run(self):
        # 遊戲迴圈：
        self.playing = True
        while self.playing:      # 每回畫面更新都要做的事情
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # 更新群組內每一個每個精靈的動作
        self.all_sprites.update()

    def events(self):
        for event in pg.event.get():
            # 遊戲結束
            if event.type == pg.QUIT:
                if self.playing:    # 不玩了
                    self.playing = False
                self.running = False    # 不執行了

    def draw(self):
        self.screen.fill(BLACK)    # 填滿背景（還需要嗎？？？
        self.all_sprites.draw(self.screen)
        ### 每次畫好畫滿所有的東西之後，就要flip。
        pg.display.flip()   # 把畫好的東西翻到正面的

    def show_start_screen(self):
        # 開始畫面
        pass

    def show_go_screen(self):
        # 遊戲結束／再來一場？的畫面
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pygame.quit()
sys.exit()
