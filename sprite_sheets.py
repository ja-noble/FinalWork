#from http://programarcadegames.com/python_examples/en/sprite_sheets/

import pygame
import settings

class SpriteSheets():
    def __init__(self, spritesheet):
        self.spritesheet = pygame.image.load(spritesheet).convert()
        #this takes the link sprite sheet and loads it... idk what convert does yet
    def get_image(self, x, y, width, height):
        #this grabs one image in sprite sheet and yeah. x, y are the position and width and height is of the rect
        image = pygame.Surface([width, height])
        image.blit(self.spritesheet, (0,0), (x,y,width,height))
        return image

#from code pilot
# class spritesheet():
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


