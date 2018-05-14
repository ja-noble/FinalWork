import pygame 
from settings import Settings
settings = Settings()
#the template for all of these classes are from programarcadegames.com

class Wall(pygame.sprite.Sprite):   
    def __init__(self, pos, width, height, color):
        super().__init__()
        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = pos[1]
        self.rect.x = pos[0]
class Box(pygame.sprite.Sprite):
    def __init__(self, pos, width, height, color):
        super().__init__()
        # Make a RED wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = pos[1]
        self.rect.x = pos[0]
class Fin(pygame.sprite.Sprite):
    def __init__(self, pos, width, height, color):
        super().__init__()
        #Make a GREEN wall
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = pos[1]
        self.rect.x = pos[0]