import pygame
from OpenGL.GL import *


pygame.init()
glClearColor(0.5, 0.5, 0.5, 1)


screen = pygame.display.set_mode((800,
600))


screen.fill((255, 255, 255))


glBegin(GL_TRIANGLES)
glColor3f(1, 0, 1) 
purple
glVertex2i(100, 100) 
glVertex2i(200, 100) 
glVertex2i(150, 200)
glEnd()


pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
