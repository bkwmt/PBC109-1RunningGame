from random import randint, uniform
import pygame as pg
from settings import *
from players import *

vec = pg.math.Vector2
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
            self.rect.top = randint(50,600)

# 上面掉落物
class Dropdown(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(img_folder, "icecream.png"))
        self.image = pg.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.right = random.randint(50, (WIDTH - 50))
        self.rect.top = -300    # 從螢幕外掉進來

    def update(self):
        # screen.blit(self.dropdown , self.dropdown_rect) 這行不需要
        if self.rect.top < HEIGHT:
            self.rect.top += DSPEED
        else:
            self.rect.right = random.randint(50, (WIDTH - 50))
            self.rect.top = -300

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
        self.rect.right = randint(50, (WIDTH - 50))
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
"""
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
        self.rect.top = randint(150, HEIGHT - 150)

    def update(self):
        # screen.blit(self.strangebomb , self.strangebomb_rect) 這行不需要
        theta = pg.time.get_ticks()/170
        self.speed_x = BSPEED
        self.speed_y = AMPLITUDE * math.sin(theta)
        if self.rect.left >= -30:
            self.rect.left -= self.speed_x
        else:
            self.rect.left = WIDTH + 100
            self.rect.top = randint(150, HEIGHT - 150)

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

class Chase(pg.sprite.Sprite):
    def __init__(self, game):
        # self.groups = all_sprites
        # pg.sprite.Sprite.__init__(self, self.groups)
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface(CHASERSIZE)
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.pos = vec(randint(HW, WIDTH), randint(HH, HEIGHT))
        self.vel = vec(MAX_SPEED, 0).rotate(uniform(0, 360))
        self.acc = vec(0, 0)
        self.rect.center = self.pos
        self.game = game

    # def get_target_pos(self):
    #     p1_get_item = pg.sprite.spritecollide(self.game.donut, self.game.items, False)
    #     p2_get_item = pg.sprite.spritecollide(self.game.donutp2, self.game.items, False)
    #
    #     if p1_get_item:
    #         # 讓drop重新再掉下來
    #         self.game.drop.rect.right = random.randint(50, (WIDTH - 50))
    #         self.game.drop.rect.top = -300
    #         position = (self.game.donut.pos.x, self.game.donut.pos.y)    # 追一號
    #
    #     elif p2_get_item:
    #         # 讓drop重新再掉下來
    #         self.game.drop.rect.right = random.randint(50, (WIDTH - 50))
    #         self.game.drop.rect.top = -300
    #         position = (self.game.donutp2.pos.x, self.game.donutp2.pos.y)
    #     else:
    #         position = (WIDTH, HEIGHT)
    #
    #     return position

    def seek_with_approach(self, target):
        # 讓他越靠近目標時，會稍微減速
        self.desired = (target - self.game.chaser.pos)
        dist = self.desired.length()
        ### 正常化初始速度（太慢了暫時取消
        # desired.normalize_ip()

        if dist < APPROACH_RADIUS:
            self.desired *= dist / APPROACH_RADIUS * MAX_SPEED
        else:
            self.desired *= MAX_SPEED

        steer = (self.desired - self.game.chaser.vel)
        if steer.length() > MAX_FORCE:
            steer.scale_to_length(MAX_FORCE)

        return steer

    def update(self):

        p1pos = self.game.chasetar_pos1
        p2pos = self.game.chasetar_pos2
        chase_pos = p1pos
        if not self.game.chase4p1:
            chase_pos = p2pos
        self.game.chaser.acc = self.seek_with_approach(chase_pos)
        # 運動方式
        self.game.chaser.vel += self.game.chaser.acc
        if self.game.chaser.vel.length() > MAX_SPEED:
            self.game.chaser.vel.scale_to_length(MAX_SPEED)
            self.game.chaser.pos += self.game.chaser.vel
        if self.game.chaser.pos.x > WIDTH:
            self.game.chaser.pos.x = 0
        if self.game.chaser.pos.x < 0:
            self.game.chaser.pos.x = WIDTH
        if self.game.chaser.pos.y > HEIGHT:
            self.game.chaser.pos.y = 0
        if self.game.chaser.pos.y < 0:
            self.game.chaser.pos.y = HEIGHT
        self.game.chaser.rect.center = self.game.chaser.pos

    # def follow_mouse(self):
    #     mpos = pg.mouse.get_pos()
    #     self.acc = (mpos - self.pos).normalize() * 0.5

    # def get_target_pos(self):
    #     sd1 = Superdonut()
    #     sd2 = Superdonutp2()
    #     chase4sd1 = True    # 暫定
    #     while chase4sd1:
    #         position = (sd1.pos.x, sd1.pos.y)
    #     else:
    #         position = (sd2.pos.x, sd1.pos.y)
    #     return position
    #
    # def follow_target(self):
    #     targetpos = self.get_target_pos()
    #     self.acc = (targetpos - self.pos).normalize() * 0.5
    #
    # def seek(self, target):
    #     self.desired = (target - self.pos).normalize() * MAX_SPEED
    #     steer = (self.desired - self.vel)
    #     if steer.length() > MAX_FORCE:
    #         steer.scale_to_length(MAX_FORCE)
    #     return steer
    #
    # def seek_with_approach(self, target):
    #     self.desired = (target - self.pos)
    #     dist = self.desired.length()
    #     self.desired.normalize_ip()
    #     if dist < APPROACH_RADIUS:
    #         self.desired *= dist / APPROACH_RADIUS * MAX_SPEED
    #     else:
    #         self.desired *= MAX_SPEED
    #         steer = (self.desired - self.vel)
    #     if steer.length() > MAX_FORCE:
    #         steer.scale_to_length(MAX_FORCE)
    #     return steer
    #
    # def update(self):
    #     # self.follow_mouse()
    #     self.acc = self.seek_with_approach(dpos)
    #     # equations of motion
    #     self.vel += self.acc
    #     if self.vel.length() > MAX_SPEED:
    #         self.vel.scale_to_length(MAX_SPEED)
    #         self.pos += self.vel
    #     if self.pos.x > WIDTH:
    #         self.pos.x = 0
    #     if self.pos.x < 0:
    #         self.pos.x = WIDTH
    #     if self.pos.y > HEIGHT:
    #         self.pos.y = 0
    #     if self.pos.y < 0:
    #         self.pos.y = HEIGHT
    #         self.rect.center = self.pos
