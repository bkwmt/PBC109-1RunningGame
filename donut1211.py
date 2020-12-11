import pygame
import sys

def start_game():
    canvas.fill(BLACK)
    start_img = start_img.get('start.png')
    start_img_react = start_img.get_rect()
    start_img_react.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    canvas.blit(start_img, start_img_react)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.Quit:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()