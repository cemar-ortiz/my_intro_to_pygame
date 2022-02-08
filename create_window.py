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
            # quits the pygame engine
            pygame.quit()
            # exits the entire module at this point in the code, preventing a pygame error
            exit()
    # draw all our elements
    # update everything
    pygame.display.update()
    # This tells the loop the max frame rate, 60 fps.
    clock.tick(60)
