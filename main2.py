#week 1 - set up function running game and created mc + box classes
#week 2 - made own modules to use for later + start to figure out how to fix pygame interface i.e. change background wasn't working rn
#week 3 - moved screen.fill() to main file to not deal with the weird problem. I also 
#   redid my main file without the help of the book so now everything works smoothly and i got character to show up on screen with movement
#   also 
#   moving onto working with sprite sheets with pygame.Sprite.sprite in mc class and i think i got surface detection using pygame.rect.colliderect()
#   but i have yet to test it yet! Once i get done with mc sprite + surface detection i'll move onto making the gameboard for the first level!
# week 4: got continuous movement, pushed back sprite sheet work (i'll take care of that last), moving along with wall detection + using a gameboard
# week 5: got surface detection working, with gameboard transversal working.
# week 6: sprite sheet work borrowing from link_char_sprite sheet, need to fix weird problem where it blits another mc everytime it hits a wall... idk
#week 7? fixed the problem that blit every time a 
import pygame
import sys
from settings import Settings
from mc import Character as mc
from box import Box
import game_functions as gf
from wall import Wall

clock = pygame.time.Clock()
walls = None #to store wall objects
walls = pygame.sprite.Group()
gameboard_1 = [                                                                     # this will be the level
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                                                                              W",
    "W                                                                              W",
    "W                                                                              W",
    "W                                                                              W",
    "W                                                                              W",
    "W                                                                              W",
    "W                                                                              W",
    "W                                                                              W",
    "W                                                                              W",
    "W                                                                              W",
    "W                                                                              W",
    "W                                                                              W",
    "W                                                                              W",
    "W                                                                              W",
    "W                       WWWWWWWWWWWWWWWWWWWWWWWWWWWWW                          W",
    "W                                                                              W",
    "W                                                                              W",
    "W                                                                              W",
    "W                                                                              W",
    "W                                                                              W",
    "W                                                                              W",
    "W                                                                              W",
    "W                                                                              W",
    "W                                    C                                         W",
    "W                                                                              W",
    "W                                                                              W",
    "W                                                                              W",
    "W                                                                              W",
    "W                                                                              W",
    "W                                                                              W",
    "W                                                                              W",
    "W                                                                              W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
]


def run_game():
    x_level_coor = 0
    y_level_coor = 0
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode([settings.screen_width, settings.screen_height])
    screen.fill(settings.color)
    pygame.display.set_caption("Jacob's Game")
    for row in gameboard_1:
        for column in row:
            #up here, i am transversing through the list to draw the level
            pos = [x_level_coor*10, y_level_coor*10]
            if column == "W":
                wall = Wall(pos, settings.wall_width, settings.wall_height, settings.wall_color)
                walls.add(wall)
                #print("this if works")
            elif column == "C":
                pos_hero = [x_level_coor*10, y_level_coor*10]
            # else:
            #     screen.blit()
            x_level_coor += 1
        y_level_coor += 1
        x_level_coor = 0
    hero = mc(screen, pos_hero)
    box = Box(screen)
    while True:
        gf.check_events(hero)
        hero.update()
        walls.draw(screen)
        #this updates hero position all the time
        gf.update_screen(settings, screen, hero, box, walls)

run_game()
