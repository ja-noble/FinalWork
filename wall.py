#original code, based on what i need for walls and surface detection

class Wall():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/wall.PNG')
        self.rect = self.image.getrect()
        self.screen_rect = screen.get_rect()
    def blitme(self, screen):
        self.screen.blit(self.image, self.rect)


