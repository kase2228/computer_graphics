import pygame
from OpenGL.GL import *

# initialize pygame and openGL
pygame.init()
glClearColor(0.5, 0.5, 0.5, 1)

# create a surface object
screen = pygame.display.set_mode((800,
600))

# set the background color
screen.fill((255, 255, 255))

# draw a triangle
glBegin(GL_TRIANGLES)
glColor3f(1, 0, 1) # set color to
purple
glVertex2i(100, 100) # first vertex
glVertex2i(200, 100) # second vertex
glVertex2i(150, 200) # third vertex
glEnd()

# update the screen
pygame.display.flip()

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
