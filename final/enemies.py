import random
import pygame as pg
from settings import *
from players import *

# 火球（正面飛行物）
class Fireball(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        # super().__init__() 這跟上面一行是一樣的作用，下面的都刪了
        self.image = pg.image.load(os.path.join(img_folder, "fireball.png"))
        self.rect = self.image.get_rect()
        self.rect.right =  10 * WIDTH
        self.rect.top = random.randint(50,600)

    def update(self):
        # screen.blit(self.fireball, self.fireball_rect) 不需要
        if self.rect.left > -400:
            self.rect.left -= FSPEED
        else:
            self.rect.right = 5 * WIDTH + WIDTH
            self.rect.top = random.randint(50,600)

# 上面掉落物
"""
class Dropdown(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(img_folder, "orange.png"))
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.right = random.randint(50, (WIDTH - 50))
        self.rect.top = -500    # 從螢幕外掉進來

    def update(self):
        # screen.blit(self.dropdown , self.dropdown_rect) 這行不需要
        if self.rect.top < HEIGHT:
            self.rect.top += DSPEED
        else:
            self.rect.right = random.randint(50, (WIDTH - 50))
            self.rect.top = -500
"""
class Dropdown(pg.sprite.Sprite):

    def __init__(self, filename, frames=1):
        pg.sprite.Sprite.__init__(self)
        self.images = []
        img = loadImage(filename, img_W=280, img_H=70)
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
        self.rect = self.image.get_rect()
        self.rect.right = random.randint(50, (WIDTH - 50))
        self.rect.top = -500    # 從螢幕外掉進來

    def update(self):
        if self.rect.top < HEIGHT:
            self.rect.top += DSPEED
        else:
            self.rect.right = random.randint(50, (WIDTH - 50))
            self.rect.top = -500

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
# 波狀飛行物
"""
class Strangebomb(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(img_folder, "apple.png"))
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH + 100
        self.rect.top = random.randint(150, HEIGHT - 150)

    def update(self):
        # screen.blit(self.strangebomb , self.strangebomb_rect) 這行不需要
        theta = pg.time.get_ticks()/170
        self.speed_x = BSPEED
        self.speed_y = WAVE * AMPLITUDE * math.sin(theta)
        if self.rect.left >= -30:
            self.rect.left -= self.speed_x
        else:
            self.rect.left = WIDTH + 100
            self.rect.top = random.randint(150, HEIGHT - 150)

        self.rect.top -= self.speed_y
"""
class Strangebomb(pg.sprite.Sprite):

    def __init__(self, filename, frames=1):
        pg.sprite.Sprite.__init__(self)
        self.images = []
        img = loadImage(filename, img_W=560, img_H=70)
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
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH + 100
        self.rect.top = random.randint(150, HEIGHT - 150)

    def update(self):
        # screen.blit(self.strangebomb , self.strangebomb_rect) 這行不需要
        theta = pg.time.get_ticks()/170
        self.speed_x = BSPEED
        self.speed_y = WAVE * AMPLITUDE * math.sin(theta)
        if self.rect.left >= -30:
            self.rect.left -= self.speed_x
        else:
            self.rect.left = WIDTH + 100
            self.rect.top = random.randint(150, HEIGHT - 150)

        self.rect.top -= self.speed_y

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

#地板怪物
class GEnemy(pg.sprite.Sprite):

    def __init__(self, filename, frames=1):
        pg.sprite.Sprite.__init__(self)
        self.images = []
        img = loadImage(filename, img_W=560, img_H=70)
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
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH + 500
        self.rect.top = 519

    def update(self):
        self.speed = PSPEED
        if self.rect.right >= - 700:
            self.rect.right -= self.speed
        else:
            self.rect.right = WIDTH + 80

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
