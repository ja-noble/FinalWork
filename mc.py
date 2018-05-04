#template from crash course, i retrofitted it
#sprite sheet from http://programarcadegames.com/python_examples/en/sprite_sheets/

import pygame
#import pygame.sprite
from wall import Wall
from box import Box
import pyganim
from settings import Settings

settings = Settings()

class Character(pygame.sprite.Sprite):
    def __init__(self, screen, pos):
        super().__init__()
        #this initializes what i need
        self.screen = screen
        #################################
        self.down1 = 'images/link_down1.png'
        self.down2 = 'images/link_down2.png'
        self.up1   = 'images/link_up1.png'
        self.up2   = 'images/link_up2.png'
        self.left1 = 'images/link_left1.png'
        self.left2 = 'images/link_left2.png'
        # self.right1 = pygame.transform.flip(self.left1, False, True), (settings.mc_height, settings.mc_width)
        # self.walkingAnim[DOWN] = pyganim.PygAnimation(((self.down1, ANIMRATE), (self.down2, ANIMRATE)))
        # self.walkingAnim[UP]   = pyganim.PygAnimation(((self.up1, ANIMRATE), (self.up2, ANIMRATE)))
        # self.walkingAnim[LEFT] = pyganim.PygAnimation(((self.left1, ANIMRATE), (self.left2, ANIMRATE)))
        # # create the right-facing sprites by copying and flipping the left-facing sprites
        # self.walkingAnim[RIGHT] = self.walkingAnim[LEFT].getCopy()
        # self.walkingAnim[RIGHT].flip(True, False)
        # self.walkingAnim[RIGHT].makeTransformsPermanent()
        # resize the Link images to match the window's magnification
        # for i in self.walkingAnim:
        #     self.walkingAnim[i].scale((settings.mc_width, settings.mc_height))
        #     self.walkingAnim[i].makeTransformsPermanent()
        ################################################## everything between these comments are straight from nes_link_game
        self.image = pygame.image.load(self.down1)
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.background = pygame.image.load('images/tile-background-4.jpg')
        self.direction = "U"
        #hp will be used not a hp but how much mc can push
        self.hp = 1000
        self.rect = self.image.get_rect()
        #this is the rectangle i'm working with for the MC
        self.screen_rect = screen.get_rect()
        #these will start the mc where i want
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False
        self.x_change = 0
        self.y_change = 0
        #^ these are movement flags
    def blitme(self):
        #this draws the character... or it should
        # self.screen.blit(self.background, pos[0], position[1])
        self.screen.blit(self.image, self.rect)
    def update(self):
        if self.move_up == True:
            self.direction = "U"
            self.rect.y-=1
            if self.y_change < 0:
                self.y_change = 0
            self.y_change -= 1
        if self.move_down == True:
            self.direction = "D"
            self.rect.y+=1
            if self.y_change < 0:
                self.y_change = 0
            self.y_change += 1
        if self.move_left == True:
            self.direction = "L"
            self.rect.x-=1
            if self.x_change > 0:
                self.x_change = 0
            self.x_change -= 1
        if self.move_right == True:
            self.direction = "R"
            self.rect.x+=1
            if self.x_change < 0:
                self.x_change = 0
            self.x_change += 1
    #version 2 wall detection... need to fix situation where it blits multiple mc's
    def did_hit(self, walls):
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if self.x_change > 0: # Moving right; Hit the left side of the wall
                    # self.rect.right = wall.rect.left
                    self.move_right = False
                if self.x_change < 0: # Moving left; Hit the right side of the wall
                    # self.rect.left = wall.rect.right
                    self.move_left = False
                if self.y_change > 0: # Moving down; Hit the top side of the wall
                    # self.rect.bottom = wall.rect.top
                    self.move_down = False
                    self.move_up = False
                if self.y_change < 0: # Moving up; Hit the bottom side of the wall
                    # self.rect.top = wall.rect.bottom
                    self.move_up = False
                    self.move_down = False

        
        