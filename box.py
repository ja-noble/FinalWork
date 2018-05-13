#original

#was going to make this it's whole py file but i realized that's dumb and just put all walls in wall.py

# class Box():
#     def __init__(self, screen):
#         #this initiates the pushable boxes i need
#         self.screen = screen
#         self.image = pygame.image.load('images/new_box.png')
#         self.rect = self.image.get_rect()
#         self.screen_rect = screen.get_rect()
#         #i don't think i need these below, i should draw based on gameboard
#         self.rect.centery = self.screen_rect.centery
#         self.rect.top = self.screen_rect.top
#     def blitme(self):
#         self.screen.blit(self.image, self.rect)