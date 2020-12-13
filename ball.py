import pygame
import sys
import random
pygame.init()

white = (255,255,255)
ADD_FIRE_RATE = 25

x = 640
y = 480
size = (x,y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("House")

class Fireball:
    vel = 10
    def __init__(self):
        self.fireball = pygame.image.load("fireball.png")
        self.fireball_rect = self.fireball.get_rect()
        self.fireball_rect.right = x
        self.fireball_rect.top = random.randint(50,460)
    
    def update(self):
        screen.blit(self.fireball, self.fireball_rect)

        if self.fireball_rect.left > 0:
            self.fireball_rect.left -= self.vel

sun_x = 500
clock = pygame.time.Clock()

done = True

while done:
    fireball = Fireball()
    fire_list = []
    add_fire_rate = 0
    while True:
        screen.fill((0,0,0))
        add_fire_rate += 1
        if add_fire_rate == ADD_FIRE_RATE:
            add_fire_rate = 0
            new_flame = Fireball()
            fire_list.append(new_flame)
        for f in fire_list:
            if f.fireball_rect.left < 0:
                fire_list.remove(f)
            f.update()
        #screen.blit(fireball, (sun_x,100))
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                pygame.quit()
                exit(0)
            pygame.display.update()

        #sun_x -= vel
        pygame.display.flip()
        clock.tick(20)