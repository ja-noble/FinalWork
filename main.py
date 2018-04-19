"""i want to create a puzzle game that has the same
dynamics and surface interaction as this game: https://www.pygame.org/project/1313, and I will take
the block pushing elements from this game: https://www.pygame.org/project/1177/2100
Tile based game with walls that can be pushed, and walls that are solid and static.
It won't be a two player game like the first link, and it looks like I would either have to pull generic
tiles or make some in PS. I'm planning to create all the code myself, but using the game as a template
for how certain interations should work."""

#week 1 - set up function running game and created mc + box classes
#week 2 - made own modules to use for later + start to figure out how to fix pygame interface i.e. change background wasn't working rn
#week 3 - moved screen.fill() to main file to not deal with the weird problem, and got character to show up on screen

import pygame
import sys
from settings import Settings
from mc import Character
import game_functions as gf
from box import Box

def running_game():
    #Initializes game and makes the screen object
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode([settings.screen_width, settings.screen_height])
    #i'm making the main character
    hero = Character(screen)
    box = Box()
    pygame.display.set_caption("Insert")
    while True:
        gf.check_events(hero)
        gf.update_screen(settings, screen, hero, box)

running_game()

    
        
    


