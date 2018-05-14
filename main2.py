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
# #       made starting screen, added limited pushes and game over screen...
        

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
boxes = pygame.sprite.Group() #same as walls
temp = None
temp = pygame.sprite.Group() # for the temp group, i use for box detection

gameboard_1 = [                             #this is the level 1                                        
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W  B  B        B               W",
    "W WW  WWBWWWBW WBWWWWWWWWWB WWBW",
    "W WW  W  W   W W   W   WWW W W W",
    "W B  BW  B   W W   W  B WW   W W",
    "W  BW WWBW  B    WW   W WW   W W",
    "W W   W   W WWWW WWB  W WWBBWW W",
    "WBW BWW   WBWWW  BW WWWW     W W",
    "W  B  WBWBW WWWW   B  B WWW WW W",
    "W  W WW   B   W   W WW  W  B W W",
    "WWBW  W WBWWWWW  W  W   W  W W W",
    "W   B B   W   W B   W   W  W W W",
    "W   WBWWBWW   WW W W W    WWWW W",
    "WB BW W  W   B  W BWBWW   W  B W",
    "W  W  W  WBWW  B W     WWWW  W W",
    "WW B  W    WW  W B     W  B  W W",
    "W WWBWWWBW   W   W  WWW W WWW  W",
    "W     B   WBWW  W  B    B  B   F",
    "WBWWBWWWBWW   WWBW W WBBWWBWWBWW",
    "W     B   WW   B   W    W      W",
    "W     WWWWWWBWWWWWWWWWWWWW WWWBW",
    "WWWWBWW W  W     B       B W   W",
    "W   C B       B      B   B W   W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
]

# def did_box_hit_wall(walls, boxes):
#     for box in boxes:
#         for wall in walls:
#             if wall.rect.contains(box.rect):
#                 return True
#             else:
#                 return False

def run_game():
    x_level_coor = 0
    y_level_coor = 0
    # ^ these are used to tell the program where the walls should be!
    pygame.init()
    font_name = pygame.font.match_font('times new roman')
    settings = Settings()
    screen = pygame.display.set_mode([settings.screen_width, settings.screen_height])
    pygame.display.set_caption("Jacob's Game")
    pygame.mixer.music.load("music/burbank-sorry-i-like-you_GgVcgbtHY9k.mp3")
    #i took everything from python crash course except music...

    #taken straight from kids can code, most initial set up for font stuff is kids can code
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

    #from kids can code, thank you for the beginning screen
    def beginning_screen():
        draw_text(screen, "Welcome to the T-Maze", 64, settings.screen_width / 2, settings.screen_height / 4)
        draw_text(screen, "Use WASD to move. W to move up, A to move left, D to move right, and S to move down.", 25,
        settings.screen_width / 2, settings.screen_height / 2)
        draw_text(screen, "You can push the red boxes! Press Space to do so, but be careful, you don't want to get tired...", 18,
        settings.screen_width / 2, settings.screen_height * 3  / 5)
        draw_text(screen, "Press the letter b to begin...", 35, settings.screen_width / 2, settings.screen_height * 3 / 4)
        pygame.display.flip()

    #original code
    def score():
        if hero.score > 1:
            draw_text(screen, "Pushes Left: "+ str(hero.score), 20,
            settings.screen_width / 2, settings.screen_height / 276)
        else:
            draw_text(screen, "One Push Left!", 20,
            settings.screen_width / 2, settings.screen_height / 276)
    #template from kids can code
    def end_screen():
        draw_text(screen, "Game Over!", 64, settings.screen_width / 2, settings.screen_height / 2)
        #i seperated this into two logic statements so that it makes grammatical sense.
        if hero.score == 1:
            draw_text(screen, "You had one push left.",64,  settings.screen_width / 2, settings.screen_height*3/4)
        else:
            draw_text(screen, "You had " +str(hero.score)+ " pushes left.",64,  settings.screen_width / 2, settings.screen_height*3/4)
        pygame.display.flip()
    while True:
        #this is for beginning screen, if waiting is true, player is waiting to start.
        if hero.waiting == True:
            beginning_screen()
            gf.check_events(hero, boxes, walls)
        #this is running the actual game
        elif hero.waiting == False and hero.game_over == False:
            screen.fill([0, 0, 0])
            draw_grid()
            gf.check_events(hero, boxes, walls)
            hero.update()
            walls.draw(screen)
            boxes.draw(screen)
            screen.blit(fin.image, fin.rect)
            score()
            gf.update_screen(settings, screen, hero, walls, boxes)
        #this is the game over screen, it shows it and fades out music
        if hero.rect.x > 1000 or hero.score == 0:
            hero.game_over = True
            pygame.mixer.music.fadeout(1000)
            gf.check_events(hero, boxes, walls)
            if hero.score == 0:
                screen.fill([89, 0, 0])
            else:
                screen.fill([0, 0, 105])
            end_screen()
          
run_game()