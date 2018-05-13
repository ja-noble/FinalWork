# # #week 1 - set up function running game and created mc + box classes
# # 
# # week 2 - made own modules to use for later + start to figure out how to fix pygame interface i.e. change background wasn't working rn
# # 
# # week 3 - moved screen.fill() to main file to not deal with the weird problem. I also 
# # #   redid my main file without the help of the book so now everything works smoothly and i got character to show up on screen with movement
# # #   also 
# # #   moving onto working with sprite sheets with pygame.Sprite.sprite in mc class and i think i got surface detection using pygame.rect.colliderect()
# # #   but i have yet to test it yet! Once i get done with mc sprite + surface detection i'll move onto making the gameboard for the first level!
# # 
# # week 4: got continuous movement, pushed back sprite sheet work (i'll take care of that last), moving along with wall detection + using a gameboard
# # week 5: got surface detection working, with gameboard transversal working.

# # week 6: sprite sheet work borrowing from link_char_sprite sheet, need to fix weird problem where it blits another mc everytime it hits a wall... idk

# # week 7? fixed the problem that blit every time a collision occured and added images. Will make image blit correcting
# #   image when blitting in a direction and will start dirty rect animation blitting

# # week 8?: fixed problem of playing going through walls. Need to make the dimensions at least the same size! i made the char
# # #     able to face the direction you are going. Now working on making the actual level
# # #  and multiple levels like in http://programarcadegames.com/python_examples/f.php?file=maze_runner.py

# # week 9: finishing the actual level and multiple rooms. made boxes player can move based on collision.
# #       if i have time, going to work on key boxes to open rooms and fixing the background and making the boxes show something
# #       Fixed the background: using kids can code and drew lines
# #       I made surface detection between boxes and walls, made entire puzzle level and made finish block to proceed through rooms
# #       15 boxes each level
import pygame
import sys
from settings import Settings
from mc import Character as mc
from wall import Box
import game_functions as gf
from wall import Wall
from wall import Fin

clock = pygame.time.Clock()
walls = None  #to store wall objects
walls = pygame.sprite.Group() #makes walls a sprite group
boxes = None
boxes = pygame.sprite.Group() #sane as walls
temp = None
temp = pygame.sprite.Group()
game_over = False


gameboard_1 = [                             #this is the level 1                                        
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W     B                        W",
    "W     W                        W",
    "W     W                        W",
    "W     W                        W",
    "W     W                        W",
    "W     B                        W",
    "W     W                        W",
    "W     W                        W",
    "W     W                        W",
    "W     W                        W",
    "W     W                        W",
    "W     W                        W",
    "W     W                        W",
    "W     W                        W",
    "WW    W                        W",
    "W WWBWB          W             W",
    "W     B       B  W             F",
    "WBWWBWWWBWWWWWW  W             W",
    "W     B                        W",
    "W     WWWWWWWWWWWWWWWWWWWWWWWWWW",
    "WWWWBWW W   W                  W",
    "W   C B       B                W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
]

# def did_box_hit_wall(walls, boxes):
#     for box in boxes:
#         for wall in walls:
#             if wall.rect.contains(box.rect):
#                 return True
#             else:
#                 return False

#this is technically from python crash course but i do absolutely need this
def run_game():
    x_level_coor = 0
    y_level_coor = 0
    #^ these are used to tell the program where the walls should be!
    pygame.init()
    font_name = pygame.font.match_font('arial')
    settings = Settings()
    screen = pygame.display.set_mode([settings.screen_width, settings.screen_height])
    pygame.display.set_caption("Jacob's Game")

    def draw_text(surf, text, size, x, y):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, [255,255,255])
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)
    
#thank you kids can code
    def draw_grid():
        for x in range(0, settings.screen_width, settings.TILESIZE):
            pygame.draw.line(screen, (100, 100, 100), (x, 0), (x, settings.screen_height))
        for y in range(0, settings.screen_height, settings.TILESIZE):
            pygame.draw.line(screen, (100, 100, 100), (0, y), (settings.screen_width, y))

    #original code
    for row in gameboard_1:
        for column in row:
            #up here, i am transversing through the list to draw the level
            pos = [x_level_coor*settings.TILESIZE, y_level_coor*settings.TILESIZE]
            if column == "W":
                wall = Wall(pos, settings.wall_width, settings.wall_height, settings.wall_color)
                walls.add(wall)
                #print("this if works")
            elif column == "C":
                pos_hero = [x_level_coor*settings.TILESIZE, y_level_coor*settings.TILESIZE]
            elif column == "B":
                box = Box(pos, settings.wall_width, settings.wall_height, settings.box_color)
                boxes.add(box)
            elif column == "F":
                fin = Fin(pos, settings.wall_height, settings.wall_height, settings.fin_color)
            x_level_coor += 1
        y_level_coor += 1
        x_level_coor = 0
    hero = mc(screen, pos_hero)

#from kids can code, thank you for the begin screen
    def beginning_screen():
        draw_text(screen, "Welcome to the T-Maze", 64, settings.screen_width / 2, settings.screen_height / 4)
        draw_text(screen, "Use WASD to move. W to move up, A to move left, D to move right, and S to move down. You can push the red boxes! Press Space to do so, but be careful, you don't want to get tired...", 14,
        settings.screen_width / 2, settings.screen_height / 2)
        draw_text(screen, "Press the letter b to begin...", 21, settings.screen_width / 2, settings.screen_height * 3 / 4)
        pygame.display.flip()

    while True:
        if hero.waiting == True:
            beginning_screen()
            gf.check_events(hero, boxes, walls)
        elif hero.waiting == False:
            screen.fill([0, 0, 0])
            draw_grid()
            gf.check_events(hero, boxes, walls)
            hero.update()
            walls.draw(screen)
            boxes.draw(screen)
            screen.blit(fin.image, fin.rect)
            #this updates hero position all the time
            gf.update_screen(settings, screen, hero, walls, boxes)
            # if fin.rect.contains(hero.rect):

run_game()