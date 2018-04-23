import pygame
""" Submit a .py file with a project proposal in the comments including:

What's your project?

    i want to create a puzzle game that has the same
dynamics and surface interaction as this game: https://www.pygame.org/project/1313, and I will take
the block pushing elements from this game: https://www.pygame.org/project/1177/2100
Tile based game with walls that can be pushed, and walls that are solid and static.

What is your first major milestone?
    Learning surface detection and rectangles with pygame

What do you not know that you will need to learn?
    uhhh learning surface detection and pushing mechanics with surfaces
In what ways is your project too ambitious?
    I don't think it's too ambitious, after I make the first level it should be good to go for more. 
    The photoshopping tiles will take up a lot of time as well though.
In what ways is it possibly not ambitious enough 
    so far, using pygame has been easier than i thought, but to be fair
    I only just set up the foundation of even getting the game to work so far
    
    """

# import pygame, sys
# pygame.init()
# screen = pygame.display.set_mode([800,600])
# white = [255, 255, 255]
# red = [255, 0, 0]
# screen.fill(white)
# pygame.display.set_caption("My program")
# pygame.display.flip()



# background = input("What color would you like?: ")
# if background == "red":
#     screen.fill(red)

# running = True
# while True:
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             running = False
#             pygame.quit()

import os
import random
import pygame

# Class for the orange dude
class Player(object):
    
    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)

    def move(self, dx, dy):
        
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    
    def move_single_axis(self, dx, dy):
        
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

# Nice class to hold a wall rect
class Wall(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

# Set up the display
pygame.display.set_caption("Get to the red square!")
screen = pygame.display.set_mode((320, 240))

clock = pygame.time.Clock()
walls = [] # List to hold the walls
player = Player() # Create the player

# Holds the level layout in a list of strings.
level = [
"WWWWWWWWWWWWWWWWWWWW",
"W                  W",
"W         WWWWWW   W",
"W   WWWW       W   W",
"W   W        WWWW  W",
"W WWW  WWWW        W",
"W   W     W W      W",
"W   W     W   WWW WW",
"W   WWW WWW   W W  W",
"W     W   W   W W  W",
"WWW   W   WWWWW W  W",
"W W      WW        W",
"W W   WWWW   WWW   W",
"W     W    E   W   W",
"WWWWWWWWWWWWWWWWWWWW",
]

# Parse the level string above. W = wall, E = exit
x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0

running = True
while running:
    
    clock.tick(60)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
    
    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
    if key[pygame.K_UP]:
        player.move(0, -2)
    if key[pygame.K_DOWN]:
        player.move(0, 2)
    
    # Just added this to make it slightly fun ;)
    # if player.rect.colliderect(end_rect):
    #     raise SystemExit, "You win!"
    
    # Draw the scene
    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    pygame.draw.rect(screen, (255, 0, 0), end_rect)
    pygame.draw.rect(screen, (255, 200, 0), player.rect)
    pygame.display.flip()