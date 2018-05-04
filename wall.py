#original code, based on what i need for walls and surface detection

import pygame 
from settings import Settings

settings = Settings()

# class Wall():
#     def __init__(self, screen):
#         self.screen = screen
#         self.image = pygame.image.load('images/wall.PNG')
#         self.rect = self.image.getrect()
#         self.screen_rect = screen.get_rect()
#     def blitme(self, screen):
#         self.screen.blit(self.image, self.rect)


class Wall(pygame.sprite.Sprite):   
    def __init__(self, pos, width, height, color):
        super().__init__()
        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = pos[1]
        self.rect.x = pos[0]

class Ground(pygame.sprite.Sprite):   
    def __init__(self, pos, width, height, color):
        super().__init__()
        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(settings.color)
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = pos[1]
        self.rect.x = pos[0]