#week 1 - set up function running game and created mc + box classes
#week 2 - made own modules to use for later + start to figure out how to fix pygame interface i.e. change background wasn't working rn
#week 3 - moved screen.fill() to main file to not deal with the weird problem. I also 
#   redid my main file without the help of the book so now everything works smoothly and i got character to show up on screen with movement
#   also 
#   moving onto working with sprite sheets with pygame.Sprite.sprite in mc class and i think i got surface detection using pygame.rect.colliderect()
#   but i have yet to test it yet! Once i get done with mc sprite + surface detection i'll move onto making the gameboard for the first level!


import pygame
import sys
from settings import Settings
from mc import Character as mc
from box import Box
import game_functions as gf
#from wall import Wall

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode([settings.screen_width, settings.screen_height])
    screen.fill(settings.color)
    pygame.display.set_caption("Jacob's Game")
    hero = mc(screen)
    box = Box(screen)
    #wall = Wall(screen)
    while True:
        gf.check_events(hero)
        mc.update()
        gf.update_screen(settings, screen, hero, box)
            
run_game()
