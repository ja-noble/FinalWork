#template from crash course, i retrofitted it
#sprite sheet from http://programarcadegames.com/python_examples/en/sprite_sheets/

import pygame
#import pygame.sprite
from wall import Wall
from box import Box
from sprite_sheets import SpriteSheets

class Character(pygame.sprite.Sprite):
    def __init__(self, screen, pos):
        super().__init__()
        #this initializes what i need
        self.screen = screen
        # self.image = pygame.image.load('images/char.PNG')
        # self.image = pygame.transform.scale(self.image, (35, 35))

        self.walking_frames_L = []
        self.walking_frames_R = []
        self.walking_frames_U = []
        self.walking_frames_D = []
        self.standing_frames = []

        #these hold my sprite sheets
        self.direction = "U"
        spritesheet = SpriteSheets("images/link_char_sprite.PNG")
        image = spritesheet.get_image(0, 0, 35, 35)
        self.walking_frames_U.append(image)
        image = spritesheet.get_image(66, 0, 35, 35)
        self.walking_frames_U.append(image)
        image = spritesheet.get_image(132, 0, 35, 35)
        self.walking_frames_U.append(image)
        image = spritesheet.get_image(0, 93, 35, 35)
        self.walking_frames_U.append(image)
        image = spritesheet.get_image(66, 93, 35, 35)
        self.walking_frames_U.append(image)
        image = spritesheet.get_image(132, 93, 35, 35)
        self.walking_frames_U.append(image)
        image = spritesheet.get_image(0, 186, 35, 35)
        self.walking_frames_U.append(image)
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
        self.screen.blit(self.image, self.rect)
    def update(self):
        if self.move_up == True:
            self.rect.y-=1
            if self.y_change < 0:
                self.y_change = 0
            self.y_change -= 1
        if self.move_down == True:
            self.rect.y+=1
            if self.y_change < 0:
                self.y_change = 0
            self.y_change += 1
        if self.move_left == True:
            self.rect.x-=1
            if self.x_change > 0:
                self.x_change = 0
            self.x_change -= 1
        if self.move_right == True:
            self.rect.x+=1
            if self.x_change < 0:
                self.x_change = 0
            self.x_change += 1
    def did_hit(self, walls):
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            #from http://programarcadegames.com/python_examples/show_file.php?file=maze_runner.py, retrofitted by me
            if self.x_change > 0:
                self.rect.x = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.x = block.rect.right
        for block in block_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.y_change > 0:
                self.rect.y = block.rect.top
            else:
                self.rect.y = block.rect.bottom


# #from code pilot
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

        
        