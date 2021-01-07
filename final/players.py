import random
import pygame as pg
from settings import *

### 向量用來製造加速與減速的感覺
vec = pg.math.Vector2

def keyPressed(keyCheck=""):
    global keydict
    keys = pg.key.get_pressed()
    if sum(keys) > 0:
        if keyCheck == "" or keys[keydict[keyCheck.lower()]]:
            return True
    return False

def loadImage(fileName, useColorKey=False, img_W=100, img_H=100):
    if os.path.isfile(fileName):
        image = pg.image.load(fileName)
        image = image.convert_alpha()
        image = pg.transform.scale(image, (img_W, img_H))
        # Return the image
        return image
    else:
        raise Exception("Error loading image: " + fileName + " - Check filename and path?")

def changeSpriteImage(sprite, index=0):
    sprite.changeImage(index)
    
def clock():
    current_time = pg.time.get_ticks()
    return current_time

class Superdonut(pg.sprite.Sprite):
    def __init__(self, game, filename, frames=1):
        # 注意這裡有來自Game裡Superdonut回傳的一個自己
        pg.sprite.Sprite.__init__(self)
        self.images = []
        img = loadImage(filename, img_W=DONUT_W*frames, img_H=DONUT_H)
        self.originalWidth = img.get_width() // frames
        self.originalHeight = img.get_height()
        frameSurf = pg.Surface((self.originalWidth, self.originalHeight), \
                               pg.SRCALPHA, 32)
        x = 0
        for frameNo in range(frames):
            frameSurf = pg.Surface((self.originalWidth, self.originalHeight), \
                                   pg.SRCALPHA, 32)
            frameSurf.blit(img, (x, 0))
            self.images.append(frameSurf.copy())
            x -= self.originalWidth
        self.image = pg.Surface.copy(self.images[0])

        self.currentImage = 0
        self.mask = pg.mask.from_surface(self.image)
        self.angle = 0
        self.scale = 1
        self.game = game    # 將game傳過來的指定給self.game，用來檢查與平台的碰撞

        ### 初始位置
        self.x = 50
        self.y = 100
        self.rect = self.image.get_rect()
        # self.rect.center = (self.x, self.y)
        ### 用向量來製造加減速的感覺
        self.pos = vec(self.x, self.y)
        self.vel = vec(0, 0)    # 初速度
        self.acc = vec(0, 0)    # 加速度一般為零
    
    def changeImage(self, index):
        self.currentImage = index
        if self.angle == 0 and self.scale == 1:
            self.image = self.images[index]
        else:
            self.image = pg.transform.rotozoom(self.images[self.currentImage], \
                                               -self.angle, self.scale)
        oldcenter = self.rect.center
        self.rect = self.image.get_rect()
        originalRect = self.images[self.currentImage].get_rect()
        self.originalWidth = originalRect.width
        self.originalHeight = originalRect.height
        self.rect.center = oldcenter
        self.mask = pg.mask.from_surface(self.image)

    def jump(self):
        # 檢查是否有站在某個平台上，有站在上面才能跳。
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        hitsground = pg.sprite.spritecollide(self, self.game.grounds, False)
        if hits or hitsground:
            self.vel.y = JMP

    def update(self):
        frame = 0
        self.acc = vec(0, GRAVITY)    # 初始值在y上面即有重力加速度向下
        pressed_keys = pg.key.get_pressed() # 設定按鍵
        if pressed_keys[pg.K_RIGHT]:
            self.acc.x = DONUT_ACC
        elif pressed_keys[pg.K_LEFT]:
            self.acc.x = -DONUT_ACC

        ### 麻擦力與加速度
        self.acc.x += self.vel.x * DONUT_FRICTION
        ### 運動公式與新的位置
        self.vel += self.acc
        self.pos += self.vel + 0.5 *self.acc
        ### 確定邊界
        if self.pos.x > WIDTH - (DONUT_W / 2):
            self.pos.x = WIDTH - (DONUT_W / 2)
        if self.pos.x < (DONUT_W / 2):
            self.pos.x = (DONUT_W / 2)
        ### 取得新的位置並準備顯示（主角的中間底部位置）
        self.rect.midbottom = self.pos

class Superdonut2(pg.sprite.Sprite):
    def __init__(self, game, filename, frames=1):   # 注意這裡有來自Game裡Superdonut回傳的一個自己 frame donut move picture change
        pg.sprite.Sprite.__init__(self)
        self.images = []
        img = loadImage(filename, img_W=DONUT_W*frames, img_H=DONUT_H)
        self.originalWidth = img.get_width() // frames
        self.originalHeight = img.get_height()
        frameSurf = pg.Surface((self.originalWidth, self.originalHeight), pg.SRCALPHA, 32)
        x = 0
        for frameNo in range(frames):
            frameSurf = pg.Surface((self.originalWidth, self.originalHeight), pg.SRCALPHA, 32)
            frameSurf.blit(img, (x, 0))
            self.images.append(frameSurf.copy())
            x -= self.originalWidth
        self.image = pg.Surface.copy(self.images[0])
        self.currentImage = 0
        self.mask = pg.mask.from_surface(self.image)
        self.angle = 0
        self.scale = 1
        self.game = game        # 將game傳過來的指定給self.game，用來檢查與平台的碰撞
        # self.image = pg.image.load(os.path.join(img_folder, "donut0.png")).convert_alpha()
        # 圖畫得不好導致遊戲體驗不佳暫時先用下面兩行生成的小方塊測試
        #self.image = pg.Surface((DONUT_W, DONUT_H))
        #self.image.fill(YELLOW)     # 圖確定了就可以把這兩行刪掉
        #moveSprite(self.image,400,500,True)
        #showSprite(self.image)
        #self.image = pg.image.load(os.path.join(img_folder, "donut0.png"))
        ### 初始位置
        self.x = WIDTH - 200
        self.y = 100
        self.rect = self.image.get_rect()
        # self.rect.center = (self.x, self.y)
        ### 用向量來製造加減速的感覺
        self.pos = vec(self.x, self.y)
        self.vel = vec(0, 0)    # 初速度
        self.acc = vec(0, 0)    # 加速度一般為零
    def changeImage(self, index):
        self.currentImage = index
        if self.angle == 0 and self.scale == 1:
            self.image = self.images[index]
        else:
            self.image = pg.transform.rotozoom(self.images[self.currentImage], -self.angle, self.scale)
        oldcenter = self.rect.center
        self.rect = self.image.get_rect()
        originalRect = self.images[self.currentImage].get_rect()
        self.originalWidth = originalRect.width
        self.originalHeight = originalRect.height
        self.rect.center = oldcenter
        self.mask = pg.mask.from_surface(self.image)
    

    def jump(self):
        # 檢查是否有站在某個平台上，有站在上面才能跳。
        # 檢查的方式是，看是否有發生碰撞：只要站在任一平台上，其實是一直有發生碰撞。
        # falls = pg.sprite.spritecollide(self, self.game.holes, False)
        # if not falls:
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        hitsground = pg.sprite.spritecollide(self, self.game.grounds, False)
        if hits or hitsground:
            self.vel.y = JMP

    def update(self):
        frame = 0
        self.acc = vec(0, GRAVITY)    # 初始值在y上面即有重力加速度向下
        pressed_keys = pg.key.get_pressed() # 設定按鍵
        # if pressed_keys[pg.K_RIGHT] and self.x < 1250:
        if pressed_keys[pg.K_d]:
            self.acc.x = DONUT_ACC
        # if pressed_keys[pg.K_LEFT] and self.x > 0:
        elif pressed_keys[pg.K_a]:
            self.acc.x = -DONUT_ACC

        ### 麻擦力與加速度（某種物理）
        self.acc.x += self.vel.x * DONUT_FRICTION
        ### 運動公式與新的位置
        self.vel += self.acc
        self.pos += self.vel + 0.5 *self.acc
        ### 確定邊界
        if self.pos.x > WIDTH - (DONUT_W / 2):
            self.pos.x = WIDTH - (DONUT_W / 2)
        if self.pos.x < (DONUT_W / 2):
            self.pos.x = (DONUT_W / 2)
        ### 取得新的位置並準備顯示（主角的中間底部位置）
        self.rect.midbottom = self.pos

class Blood(pg.sprite.Sprite):
    def __init__(self, filename, frames=1, pos=0):
        pg.sprite.Sprite.__init__(self)
        self.images = []
        img = loadImage(filename, img_W=800, img_H=50)
        self.originalWidth = img.get_width() // frames
        self.originalHeight = img.get_height()
        frameSurf = pg.Surface((self.originalWidth, self.originalHeight), pg.SRCALPHA, 32)
        x = 0
        for frameNo in range(frames):
            frameSurf = pg.Surface((self.originalWidth, self.originalHeight), pg.SRCALPHA, 32)
            frameSurf.blit(img, (x, 0))
            self.images.append(frameSurf.copy())
            x -= self.originalWidth
        self.image = pg.Surface.copy(self.images[0])
        self.currentImage = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = (10, pos)
        self.mask = pg.mask.from_surface(self.image)
        self.angle = 0
        self.scale = 1

    def changeImage(self, index):
        self.currentImage = index
        if self.angle == 0 and self.scale == 1:
            self.image = self.images[index]
        else:
            self.image = pg.transform.rotozoom(self.images[self.currentImage], -self.angle, self.scale)
        oldcenter = self.rect.center
        self.rect = self.image.get_rect()
        originalRect = self.images[self.currentImage].get_rect()
        self.originalWidth = originalRect.width
        self.originalHeight = originalRect.height
        self.rect.center = oldcenter
        self.mask = pg.mask.from_surface(self.image)


#集滿螢幕會倒轉
class Reverse(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(img_folder, "reverse.png"))
        self.image = pg.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH
        self.rect.top = 530

    def update(self):
        self.speed = PSPEED
        if self.rect.right >= - 400:
            self.rect.right -= self.speed
        else:
            self.rect.right = WIDTH + 80
