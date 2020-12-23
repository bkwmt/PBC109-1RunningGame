class Blood:
    def __init__(self):
        self.raw_image = pygame.image.load("blood.png")
        self.image = pygame.transform.scale(self.raw_image, (70, 70)) 
        self.now_blood = 5  # 初始血量
    def show(self):  # 左上角顯示血量(可能需要美編)
        all_blood = [self.image]*self.now_blood
        position = [ 50 , 100 , 150 , 200 , 250 ]
        for i in range (len(all_blood)):
            screen.blit( self.image , (position[i],50) )
    def hurt(self):  # 撞到敵人就扣血
        if self.now_blood > 1:
            self.now_blood -= 1
        else:
            # 寫入遊戲結束機制
blood = Blood()

if pygame.sprite.spritecollide( superdonut , , True ):  #　中間放敵人的group(我找不到)
        blood.hurt()