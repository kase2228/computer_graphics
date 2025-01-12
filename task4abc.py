import pygame
from pygame.locals import *

pygame.init()
canvas = pygame.display.set_mode((500, 400))
pygame.display.set_caption('exam')

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_F1:
                    pygame.quit()
                    quit()
            canvas.fill((255,255,255))
            pygame.draw.line(canvas, (255, 0, 0),
(50, 50), (3, 200))
            pygame.display.update()

main()

