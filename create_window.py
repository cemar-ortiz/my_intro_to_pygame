'''
Learning how to create a window with pygame and draw surfaces on top of it. Also how to set a framerate
'''

import pygame
from sys import exit

# Initialize the pygame engine
pygame.init()
# create a display surface passing a tuple with width and height
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("My window")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/Ground.png')
text_surface = test_font.render('My game', False, 'Green')


while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # block image transfer
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 350))
    screen.blit(text_surface, (300, 50))

    pygame.display.update()
    # set framerate
    clock.tick(60)
