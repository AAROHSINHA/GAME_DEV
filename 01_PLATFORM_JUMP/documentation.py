###########################################################################
##############################  BASICS ####################################
###########################################################################
import pygame
from sys import exit

# This is very important as it starts pygame and initiates all the sub-parts needed to run
# It's like starting the engine of a car. Some really complex stuff happen, and now we can use the functions of a car
pygame.init()

# We need to add a screen. It takes width and height for the game window
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('PLATFORM JUMPER') # setting new name

# To cater the framerate
clock = pygame.time.Clock()

# Our game runs in this while loop
while True:
    # Event loop. We check for what event is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Closes the window
            exit() # this also terminates the while loop (break won't work here)

    # draw all our elements
    # updates everything
    pygame.display.update()
    clock.tick(60) # maximum frame-rate is 60 now


###########################################################################
####################  DISPLAYING IMAGES ###################################
###########################################################################
import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('PLATFORM JUMPER')
clock = pygame.time.Clock()

# To create an image, sprite or text, we need to create a surface and place it on our display surface (window)
# plain surface -
# test_surface = pygame.Surface((100, 200)) # needs width and height
# test_surface.fill('Red')
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# text font surfaces
# create a font -> write text on the surface -> blit the text surface
test_font = pygame.font.Font('fonts/Pixeltype.ttf', 50) # font-type, font-size
text_surface = test_font.render('My Game', False, 'Black') # text-content, anti-alias, color

# snail
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600 # by default this is 600

# player
player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300)) # takes a surface and draws a rectangle around it
# we can place relative to different positions in rectangle...like mid-left, top-left, mid-bottom, corners

screen.blit(player_surf, player_rect)  # placing the player surface in position of the rectangle

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # To display test surface, we need to use blit. WHERE_TO_PUT.blit(WHAT_TO_PUT, POSITION)
    screen.blit(sky_surface, (0, 0)) # (surface to place, position)
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    # moving the snail x position everytime the while loop works (game works)
    snail_x_pos -= 4
    # reset snail position once it gets out of the screen
    if snail_x_pos < -100:
        snail_x_pos = 800

    screen.blit(snail_surface, (snail_x_pos, 250))
    screen.blit(player_surf, player_rect) # placing the player surface in position of the rectangle

    pygame.display.update()
    clock.tick(60)





