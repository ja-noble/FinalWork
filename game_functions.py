#code from crash course, mostly
#made did_hit myself after learning how to use colliderect
import sys
import pygame
from mc import Character as mc
from settings import Settings
from wall import Wall

settings = Settings() 
screen = pygame.display.set_mode([settings.screen_width, settings.screen_height])

def check_events(mc): 
    # while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #Movement of the character
            if event.key == pygame.K_RIGHT:
                mc.move_right = True
            if event.key == pygame.K_UP:
                mc.move_up = True
            if event.key == pygame.K_DOWN:
                mc.move_down = True
            if event.key == pygame.K_LEFT:
                mc.move_left = True
        elif event.type == pygame.KEYUP:
            #toggles T/F and in mc class, will move if key down
            if event.key == pygame.K_RIGHT:
                mc.move_right = False
            if event.key == pygame.K_UP:
                mc.move_up = False
            if event.key == pygame.K_DOWN:
                mc.move_down = False
            if event.key == pygame.K_LEFT:
                mc.move_left = False


# def check_pushing_command(mc):
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.type == pygame.K_SPACE:
#                 print("This will be the pushing the boxes for puzzle")
            
def update_screen(settings, screen, hero, box, walls):
    hero.blitme()
    hero.did_hit(walls)
    pygame.display.flip()
    pygame.display.update()