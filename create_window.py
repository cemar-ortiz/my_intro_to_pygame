'''
Learning how to create a window with pygame
'''


import pygame
from sys import exit

# Initialize the pygame engine
pygame.init()
# create a display surface passing a tuple with width and height
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("My window")
clock = pygame.time.Clock()


#
while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    # set framerate
    clock.tick(60)
