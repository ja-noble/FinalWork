#template from crash course, i retrofitted it

import pygame
#import pygame.sprite
from wall import Wall
from box import Box

class Character():
    def __init__(self, screen, pos):
        #this initializes what i need
        self.screen = screen
        self.image = pygame.image.load('images/char.PNG')
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
        #^ these are movement flags
    def blitme(self):
        #this draws the character... or it should
        self.screen.blit(self.image, self.rect)
    def update(self):
        if self.move_up == True:
            self.rect.y-=1
        if self.move_down == True:
            self.rect.y+=1
        if self.move_left == True:
            self.rect.x-=1
        if self.move_right == True:
            self.rect.x+=1


#from code pilot
# class spritesheet:
# 	def __init__(self, filename, cols, rows):
# 		self.sheet = pygame.image.load(filename).convert_alpha()
		
# 		self.cols = cols
# 		self.rows = rows
# 		self.totalCellCount = cols * rows
		
# 		self.rect = self.sheet.get_rect()
# 		w = self.cellWidth = self.rect.width / cols
# 		h = self.cellHeight = self.rect.height / rows
# 		hw, hh = self.cellCenter = (w / 2, h / 2)
		
# 		self.cells = list([(index % cols * w, index / cols * h, w, h) for index in range(self.totalCellCount)])
# 		self.handle = list([
# 			(0, 0), (-hw, 0), (-w, 0),
# 			(0, -hh), (-hw, -hh), (-w, -hh),
# 			(0, -h), (-hw, -h), (-w, -h),])
		
# 	def draw(self, surface, cellIndex, x, y, handle = 0):
# 		surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])

        
        