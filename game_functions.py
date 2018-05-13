#code from crash course, mostly
#made did_hit myself after learning how to use colliderect
import sys
import pygame
from mc import Character as mc
from settings import Settings
from wall import Wall
from wall import Box

settings = Settings() 
screen = pygame.display.set_mode([settings.screen_width, settings.screen_height])
dirty_rect = []

def check_events(mc, boxes, walls): 
    # while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #Movement of the character
            if event.key == pygame.K_d:
                mc.move_right = True
            if event.key == pygame.K_w:
                mc.move_up = True
            if event.key == pygame.K_s:
                mc.move_down = True
            if event.key == pygame.K_a:
                mc.move_left = True
            if event.key == pygame.K_SPACE:
                mc.move_box(boxes, walls)
                mc.box_hit_wall(boxes, walls)
                mc.box_hit_box(boxes)
            if event.key == pygame.K_y:
                print(mc.rect.x)
                print(mc.rect.y)
            if event.key == pygame.K_b:
                mc.waiting = False
        elif event.type == pygame.KEYUP:
            #toggles T/F and in mc class, will move if key down
            if event.key == pygame.K_d:
                mc.move_right = False
            if event.key == pygame.K_w:
                mc.move_up = False
            if event.key == pygame.K_s:
                mc.move_down = False
            if event.key == pygame.K_a:
                mc.move_left = False
                #this event is for debugging! And I guess if you want to 
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
            #this event is for my own debugging, i used this to tell where I am in the gameboard
            #and how to access specific points. I got mouse.get_pos() and mousebuttonup from pygame.org

#this function's idea is from python crash course, i then made my own functions
def update_screen(settings, screen, hero, walls, boxes):
    hero.blitme()
    #crash course
    hero.did_hit(walls)
    #original, for need of surface detection
    hero.did_hit_box(boxes)
    #ditto ^
    pygame.display.flip()
    #i still don't know what this does lol ^
    hero.change_image()
    #original code, to change direction of link

def finish(mc, finish, game_over):
    if finish.rect.contains(mc.rect):
        game_over = True  
# for game over screen, my own code