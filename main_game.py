'''
Learning how to create a window with pygame and draw surfaces on top of it. Also how to set a framerate.
Learning how to run basic animations
'''

import pygame
from sys import exit

# Initialize the pygame engine
pygame.init()
# create a display surface passing a tuple with width and height
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("My window")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/Ground.png').convert()
text_surface = test_font.render('Dirtbound', False, 'Black')

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600



while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # block image transfer
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 350))
    screen.blit(text_surface, (300, 50))
    snail_x_pos -= 1.5
    screen.blit(snail_surface, (snail_x_pos, 315))
    if snail_x_pos <= -45:
        snail_x_pos = 805

    pygame.display.update()
    # set framerate
    clock.tick(60)