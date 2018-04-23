#original code, based on what i need for walls and surface detection

# class Wall():
#     def __init__(self, screen):
#         self.screen = screen
#         self.image = pygame.image.load('images/wall.PNG')
#         self.rect = self.image.getrect()
#         self.screen_rect = screen.get_rect()
#     def blitme(self, screen):
#         self.screen.blit(self.image, self.rect)

walls = []

class Wall(object):   
    def __init__(self, pos, screen):
        self.screen = screen
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
        self.screen_rect = screen.get_rect()

