import pygame
import sys
pygame.init()

white = (255,255,255)

size = (640,480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("House")

fireball = pygame.image.load("fireball.png")
sun_x = 500
clock = pygame.time.Clock()

while True:
    screen.fill(white)
    screen.blit(fireball, (sun_x,100))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            exit()
        pygame.display.update()

    sun_x -= 10
    pygame.display.flip()
    clock.tick(60)