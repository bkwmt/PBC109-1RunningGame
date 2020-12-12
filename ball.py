import pygame
import sys
BLUE = (50,50,225)
pygame.init()

size = (640,480)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("House")

done = False
sun_x = 500
sun_y = 100

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    sun_x -= 10
    screen.fill((0,0,0))
    
    pygame.draw.circle(screen, BLUE, (sun_x,sun_y),40,0)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()