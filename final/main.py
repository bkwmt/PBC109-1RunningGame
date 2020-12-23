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
        self.bkgd = pg.image.load(os.path.join(img_folder, "mountains.png")).convert() # 匯入背景圖
        # self.background = pg.Surface(SIZE)  # ??跟screen有何不同
        # self.background.fill(( 0 , 0 , 120 ))  # 塗滿(之後可調整)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # 重新開始一個遊戲
        self.all_sprites = pg.sprite.Group()    # 初始化全部精靈群組
        self.grounds = pg.sprite.Group()    # 初始化地面群組
        self.holes = pg.sprite.Group()    # 初始化洞群組
        self.platforms = pg.sprite.Group()    # 初始化平台群組
        self.enemies = pg.sprite.Group()   # 初始化敵人群組

        ### 送自己回去Superdonut，才能夠與這裡的platform群組檢查
        self.donut = Superdonut(self)   # !!!!!!!!!!!!!!!!
        self.all_sprites.add(self.donut)

        ### 讀入地板
        gnd = Ground(0, HEIGHT - GHEIGHT, WIDTH, GHEIGHT)     # 地板單獨設定
        self.all_sprites.add(gnd)
        self.grounds.add(gnd)

        ### 讀入洞
        hole = Hole()
        self.all_sprites.add(hole)
        self.holes.add(hole)

        ### 讀入其他平台
        for plat in PLATFORM_LIST:
            p = Platform(plat[0], plat[1], plat[2], plat[3])
            self.all_sprites.add(p)
            self.platforms.add(p)

        self.drop = Dropdown()
        self.all_sprites.add(self.drop)
        self.enemies.add(self.drop)

        self.sbomb = Strangebomb()
        self.all_sprites.add(self.sbomb)
        self.enemies.add(self.sbomb)

        self.fball = Fireball()
        self.all_sprites.add(self.fball)
        self.enemies.add(self.fball)

        ### 執行遊戲
        self.run()

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
        # 檢查「落下」碰撞（放入一個list）
        oops = pg.sprite.spritecollide(self.donut, self.holes, False)
        if not oops:
            if self.donut.vel.y > 0:    # 檢查落下（y>0）時的碰撞
                hits = pg.sprite.spritecollide(self.donut, self.platforms, False)
                hitsground = pg.sprite.spritecollide(self.donut, self.grounds, False)
                if hits:
                ### 撞到的話就讓他的位置維持在那個平台上，速度歸零。
                    self.donut.pos.y = hits[0].rect.top + 1
                    self.donut.vel.y = 0
                elif hitsground:
                ### 撞到的話就讓他的位置維持在地板上，速度歸零。
                    self.donut.pos.y = hitsground[0].rect.top + 1
                    self.donut.vel.y = 0
            if self.donut.vel.y < 0:    # 檢查向上碰撞
                hits = pg.sprite.spritecollide(self.donut, self.platforms, False)
                if hits:
                ### 撞到的話就瞬間降低一個主角的高度，並且速度歸零。
                    self.donut.pos.y = hits[0].rect.bottom + DONUT_H
                    self.donut.vel.y = 0

    def events(self):
        for event in pg.event.get():
            # 遊戲結束
            if event.type == pg.QUIT:
                if self.playing:    # 不玩了
                    self.playing = False
                self.running = False    # 不執行了

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.donut.jump()

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

pg.quit()
sys.exit()
