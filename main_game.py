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
snail_rectangle = snail_surface.get_rect(bottomright = (800, 350))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(80,350))


while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
            if player_rectangle.collidepoint(mouse_pos):
                print('collision with mouse')

    # block image transfer
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 350))
    screen.blit(text_surface, (300, 50))

    snail_rectangle.x -= 1
    screen.blit(snail_surface, snail_rectangle)
    if snail_rectangle.right == 0:
        snail_rectangle.left = 800
    
    player_rectangle.x += 1
    screen.blit(player_surface, player_rectangle)
    if player_rectangle.left == 800:
        player_rectangle.right = 0

    # if player_rectangle.colliderect(snail_rectangle):
    #     print('collision')

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rectangle.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())
         

    pygame.display.update()
    # set framerate
    clock.tick(60)
