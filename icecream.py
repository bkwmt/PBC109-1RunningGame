
class Icecream(pg.sprite.Sprite):
    
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(img_folder, "icecream.png"))
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0 , WIDTH)
        self.rect.centery = HEIGHT
        self.rect.width , self.rect.height = 50 , 50
        screen.blit(self.image,self.rect)
        self.pt = 0
        
    def update(self):
        if not pg.sprite.spritecollide( self.rect, platforms, False ):  # 從天空掉下來直到撞到平台
            self.rect.centery -= GRAVITY  # 掉下來的速度跟重力一樣
        if pg.sprite.spritecollide( self.rect , , TRUE ):  # 偵測甜甜圈有沒有吃到冰淇淋
            self.pt += 1  # 吃到分數+1
			self.rect.centerx = random.randint(0 , WIDTH)
            self.rect.centery = HEIGHT