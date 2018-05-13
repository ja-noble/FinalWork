#template from crash course, i retrofitted it
#sprite sheet from http://programarcadegames.com/python_examples/en/sprite_sheets/

import pygame
#import pygame.sprite
from wall import Wall
from wall import Box
import pyganim
from settings import Settings

settings = Settings()
push = False

class Character(pygame.sprite.Sprite):
    def __init__(self, screen, pos):
        super().__init__()
        #this initializes what i need
        self.screen = screen
        ################################# i took the images from nes_zelda_map_data_master! from canvas
        self.down1 = 'images/link_down1.png'
        # self.down2 = 'images/link_down2.png'
        self.up1   = 'images/link_up1.png'
        # self.up2   = 'images/link_up2.png'
        self.left1 = 'images/link_left1.png'
        ################################################## everything between these comments are straight from nes_link_game
        
        #these are original between these, this is to switch between the four images
        self.image = pygame.image.load(self.down1)

        self.down_image = pygame.image.load(self.down1)
        self.down_image = pygame.transform.scale(self.down_image, (settings.mc_height,settings.mc_width))

        self.up_image = pygame.image.load(self.up1)
        self.up_image = pygame.transform.scale(self.up_image, (settings.mc_height,settings.mc_width))


        self.left_image = pygame.image.load(self.left1)
        self.left_image = pygame.transform.scale(self.left_image, (settings.mc_height,settings.mc_width))

        self.right1 = pygame.transform.flip(self.left_image, True, False)
        #i took transform.flip from pygame.org
        #these are original beween these comments ^^^

        self.direction = "U"
        #this is to set the direction link is facing

        # self.background = pygame.image.load('images/tile-background-4.jpg')
        # #this is the background that will be used for the game... but i didn't use it lol

        #hp will be used not a hp but how much mc can push
        self.hp = 1000
        self.rect = self.image.get_rect()
        #this is the rectangle i'm working with for the MC
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        #this sets link where I want in gameboard
        self.x = 0
        self.y = 0
        #this keeps track of where link is based on his origin at all times
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False
        #movement flags, mostly used to update link's movement

        self.x_change = 0
        self.y_change = 0
        #^ these are movement flags
        self.waiting = True

    def change_image(self):
        if self.direction == "U":
            self.image = self.up_image
        elif self.direction == "D":
            self.image = self.down_image
        elif self.direction == "L":
            self.image = self.left_image
        elif self.direction == "R":
            self.image = self.right1
        #this function changes the image to be blitted! based on direction link faces, self.image will be facing that direction

    def blitme(self):
        #this draws the character... or it should
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_up == True:
            self.direction = "U"
            if self.y_change < 0 or self.x_change != 0:
                self.x_change = 0
                self.y_change = 0
            self.rect.y -=1 
            self.y_change -= 1
        if self.move_down == True:
            self.direction = "D"
            if self.y_change < 0 or self.x_change != 0:
                self.x_change = 0
                self.y_change = 0
            self.rect.y += 1
            self.y_change += 1
        if self.move_left == True:
            self.direction = "L"
            if self.x_change > 0 or self.y_change != 0:
                self.x_change = 0
                self.y_change = 0
            self.rect.x -= 1
            self.x_change -= 1
        if self.move_right == True:
            self.direction = "R"
            if self.x_change < 0 or self.y_change != 0:
                self.x_change = 0
                self.y_change = 0
            self.rect.x +=1
            self.x_change += 1
#ok this function is a busy one.

    #version 2 wall detection... need to fix situation where it blits multiple mc's
    def did_hit(self, walls):
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if self.x_change > 0: # Moving right; Hit the left side of the wall
                    # self.rect.x = wall.rect.midright
                    self.move_right = False
                    # print(self.rect.colliderect(wall.rect))
                if self.x_change < 0: # Moving left; Hit the right side of the wall
                    # self.rect.left = wall.rect.right
                    self.move_left = False
                    # print(self.rect.colliderect(wall.rect))
                if self.y_change > 0: # Moving down; Hit the top side of the wall
                    # self.rect.bottom = wall.rect.top
                    self.move_down = False
                    self.move_up = False
                    # print(self.rect.colliderect(wall.rect))
                if self.y_change < 0: # Moving up; Hit the bottom side of the wall
                    # self.rect.top = wall.rect.bottom
                    self.move_up = False
                    self.move_down = False
                    # print(self.rect.colliderect(wall.rect))

    def did_hit_box(self, boxes):
        for box in boxes:
            if self.rect.colliderect(box.rect):
                if self.x_change > 0: # Moving right; Hit the left side of the wall
                    self.move_right = False
                    # print(self.rect.colliderect(wall.rect))
                if self.x_change < 0: # Moving left; Hit the right side of the wall
                    # self.rect.left = wall.rect.right
                    self.move_left = False
                    # print(self.rect.colliderect(wall.rect))
                if self.y_change > 0: # Moving down; Hit the top side of the wall
                    # self.rect.bottom = wall.rect.top
                    self.move_down = False
                    self.move_up = False
                    # print(self.rect.colliderect(wall.rect))
                if self.y_change < 0: # Moving up; Hit the bottom side of the wall
                    # self.rect.top = wall.rect.bottom
                    self.move_up = False
                    self.move_down = False
                    # print(self.rect.colliderect(wall.rect))

    def move_box(self, boxes, walls):
        global push
        for box in boxes: 
            if self.rect.colliderect(box.rect):
                push = True
                if self.x_change > 0:
                    box.rect.x += settings.TILESIZE
                    #self.hp -= 50
                elif self.x_change < 0:
                    box.rect.x -= settings.TILESIZE
                    #self.hp -= 50
                elif self.y_change > 0:
                    box.rect.y += settings.TILESIZE
                elif self.y_change < 0:
                    box.rect.y -= settings.TILESIZE

#this checks if a box is going to be inside a wall, then moves the box right back!
    def box_hit_wall(self, boxes, walls):
        for box in boxes:
            if push == True:
                for wall in walls:
                    if wall.rect.contains(box.rect):
                        if self.x_change > 0:
                            box.rect.x -= settings.TILESIZE
                            #self.hp -= 50
                        elif self.x_change < 0:
                            box.rect.x += settings.TILESIZE
                            #self.hp -= 50
                        elif self.y_change > 0:
                            box.rect.y -= settings.TILESIZE
                        elif self.y_change < 0:
                            box.rect.y += settings.TILESIZE
    
    # this function takes the boxes group and makes temp. Temp is the boxes group EXCEPT the box we are pushing.
    # this will check if a box will be inside another box, and does the same thing as box_hit_wall
    def box_hit_box(self, boxes):
        for box in boxes:
            temp = boxes
            temp.remove(box)
            # print(temp)
            if push == True:
                # print("yes")
                for box2 in temp:
                    if box2.rect.contains(box.rect):
                        if self.x_change > 0:
                            box2.rect.x -= settings.TILESIZE
                            #self.hp -= 50
                        elif self.x_change < 0:
                            box2.rect.x += settings.TILESIZE
                            #self.hp -= 50
                        elif self.y_change > 0:
                            box2.rect.y -= settings.TILESIZE
                        elif self.y_change < 0:
                            box2.rect.y += settings.TILESIZE
            temp.add(box)