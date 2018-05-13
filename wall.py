#original code, based on what i need for walls and surface detection

import pygame 
from settings import Settings

settings = Settings()

class Wall(pygame.sprite.Sprite):   
    def __init__(self, pos, width, height, color):
        super().__init__()
        # Make a BLUE wall, of the size specified in the parameters
        # self.screen = screen
        # self.image = pygame.image.load('images/wall1.png').convert()
        # self.image = pygame.transform.scale(self.image, (35,35))
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = pos[1]
        self.rect.x = pos[0]
    # def blitme(self):
    #     self.screen.blit(self.image, self.rect)
class Box(pygame.sprite.Sprite):
    def __init__(self, pos, width, height, color):
        super().__init__()
        # Make a RED wall, of the size specified in the parameters
        # self.screen = screen
        # self.image = pygame.image.load('images/wall1.png').convert()
        # self.image = pygame.transform.scale(self.image, (35,35))
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = pos[1]
        self.rect.x = pos[0]
class Fin(pygame.sprite.Sprite):
    def __init__(self, pos, width, height, color):
        super().__init__()
        # self.screen = screen
        # self.image = pygame.image.load('images/wall1.png').convert()
        # self.image = pygame.transform.scale(self.image, (35,35))
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = pos[1]
        self.rect.x = pos[0]