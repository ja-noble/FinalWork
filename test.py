import pygame
""" Submit a .py file with a project proposal in the comments including:

What's your project?

    i want to create a puzzle game that has the same
dynamics and surface interaction as this game: https://www.pygame.org/project/1313, and I will take
the block pushing elements from this game: https://www.pygame.org/project/1177/2100
Tile based game with walls that can be pushed, and walls that are solid and static.

What is your first major milestone?
    Learning surface detection and rectangles with pygame

What do you not know that you will need to learn?
    uhhh learning surface detection and pushing mechanics with surfaces
In what ways is your project too ambitious?
    I don't think it's too ambitious, after I make the first level it should be good to go for more. 
    The photoshopping tiles will take up a lot of time as well though.
In what ways is it possibly not ambitious enough 
    so far, using pygame has been easier than i thought, but to be fair
    I only just set up the foundation of even getting the game to work so far
    
    """

import pygame, sys
pygame.init()
screen = pygame.display.set_mode([800,600])
white = [255, 255, 255]
red = [255, 0, 0]
screen.fill(white)
pygame.display.set_caption("My program")
pygame.display.flip()



background = input("What color would you like?: ")
if background == "red":
    screen.fill(red)

running = True
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
            pygame.quit()

