#template from crash course, i retrofitted it

import pygame
#import pygame.sprite
from wall import Wall
from box import Box

class Character():
    def __init__(self, screen):
        #this initializes what i need
        self.screen = screen
        self.image = pygame.image.load('images/char.PNG')
        #hp will be used not a hp but how much mc can push
        self.hp = 1000
        self.rect = self.image.get_rect()
        #this is the rectangle i'm working with for the MC
        self.screen_rect = screen.get_rect()
        #these will start the mc in the center bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False
        #^ these are movement flags
    def blitme(self):
        #this draws the character... or it should
        self.screen.blit(self.image, self.rect)
    def update(self):
        if self.move_up == True:
            self.rect.centery+=1
        if self.move_down == True:
            self.rect.centery-=1
        if self.move_left == True:
            self.rect.centerx-=1
        if self.move_right == True:
            self.rect.centerx+=1
        
        