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

# # Class for the orange dude
# class Player(object):
    
#     def __init__(self):
#         self.rect = pygame.Rect(32, 32, 16, 16)

#     def move(self, dx, dy):
        
#         # Move each axis separately. Note that this checks for collisions both times.
#         if dx != 0:
#             self.move_single_axis(dx, 0)
#         if dy != 0:
#             self.move_single_axis(0, dy)
    
#     def move_single_axis(self, dx, dy):
        
#         # Move the rect
#         self.rect.x += dx
#         self.rect.y += dy

#         # If you collide with a wall, move out based on velocity
#         for wall in walls:
#             if self.rect.colliderect(wall.rect):
#                 if dx > 0: # Moving right; Hit the left side of the wall
#                     self.rect.right = wall.rect.left
#                 if dx < 0: # Moving left; Hit the right side of the wall
#                     self.rect.left = wall.rect.right
#                 if dy > 0: # Moving down; Hit the top side of the wall
#                     self.rect.bottom = wall.rect.top
#                 if dy < 0: # Moving up; Hit the bottom side of the wall
#                     self.rect.top = wall.rect.bottom

# # Nice class to hold a wall rect
# class Wall(object):
    
#     def __init__(self, pos):
#         walls.append(self)
#         self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

# # Initialise pygame
# os.environ["SDL_VIDEO_CENTERED"] = "1"
# pygame.init()

# # Set up the display
# pygame.display.set_caption("Get to the red square!")
# screen = pygame.display.set_mode((320, 240))

# clock = pygame.time.Clock()
# walls = [] # List to hold the walls
# player = Player() # Create the player

# # Holds the level layout in a list of strings.
# level = [
# "WWWWWWWWWWWWWWWWWWWW",
# "W                  W",
# "W         WWWWWW   W",
# "W   WWWW       W   W",
# "W   W        WWWW  W",
# "W WWW  WWWW        W",
# "W   W     W W      W",
# "W   W     W   WWW WW",
# "W   WWW WWW   W W  W",
# "W     W   W   W W  W",
# "WWW   W   WWWWW W  W",
# "W W      WW        W",
# "W W   WWWW   WWW   W",
# "W     W    E   W   W",
# "WWWWWWWWWWWWWWWWWWWW",
# ]

# # Parse the level string above. W = wall, E = exit
# x = y = 0
# for row in level:
#     for col in row:
#         if col == "W":
#             Wall((x, y))
#         if col == "E":
#             end_rect = pygame.Rect(x, y, 16, 16)
#         x += 16
#     y += 16
#     x = 0

# running = True
# while running:
    
#     clock.tick(60)
    
#     for e in pygame.event.get():
#         if e.type == pygame.QUIT:
#             running = False
#         if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
#             running = False
    
#     # Move the player if an arrow key is pressed
#     key = pygame.key.get_pressed()
#     if key[pygame.K_LEFT]:
#         player.move(-2, 0)
#     if key[pygame.K_RIGHT]:
#         player.move(2, 0)
#     if key[pygame.K_UP]:
#         player.move(0, -2)
#     if key[pygame.K_DOWN]:
#         player.move(0, 2)
    
#     # Just added this to make it slightly fun ;)
#     # if player.rect.colliderect(end_rect):
#     #     raise SystemExit, "You win!"
    
#     # Draw the scene
#     screen.fill((0, 0, 0))
#     for wall in walls:
#         pygame.draw.rect(screen, (255, 255, 255), wall.rect)
#     pygame.draw.rect(screen, (255, 0, 0), end_rect)
#     pygame.draw.rect(screen, (255, 200, 0), player.rect)
#     pygame.display.flip()

"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
From:
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
 
Explanation video: http://youtu.be/5-SbFanyUkQ
 
Part of a series:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/
"""

#this was all for testing the code i did take from, see how it works

import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
 
 
class Wall(pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the player controls """
 
    def __init__(self, x, y, width, height, color):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
 
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the
    player controls """
 
    # Set speed vector
    change_x = 0
    change_y = 0
 
    def __init__(self, x, y):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
    def changespeed(self, x, y):
        """ Change the speed of the player. Called with a keypress. """
        self.change_x += x
        self.change_y += y
 
    def move(self, walls):
        """ Find a new position for the player """
 
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
 
 
class Room(object):
    """ Base class for all rooms. """
 
    # Each room has a list of walls, and of enemy sprites.
    wall_list = None
    enemy_sprites = None
 
    def __init__(self):
        """ Constructor, create our lists. """
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
 
 
class Room1(Room):
    """This creates all the walls in room 1"""
    def __init__(self):
        super().__init__()
        # Make the walls. (x_pos, y_pos, width, height)
 
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [390, 50, 20, 500, BLUE]
                ]
 
        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 
 
class Room2(Room):
    """This creates all the walls in room 2"""
    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 20, 250, RED],
                 [0, 350, 20, 250, RED],
                 [780, 0, 20, 250, RED],
                 [780, 350, 20, 250, RED],
                 [20, 0, 760, 20, RED],
                 [20, 580, 760, 20, RED],
                 [190, 50, 20, 500, GREEN],
                 [590, 50, 20, 500, GREEN]
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 
 
class Room3(Room):
    """This creates all the walls in room 3"""
    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 20, 250, PURPLE],
                 [0, 350, 20, 250, PURPLE],
                 [780, 0, 20, 250, PURPLE],
                 [780, 350, 20, 250, PURPLE],
                 [20, 0, 760, 20, PURPLE],
                 [20, 580, 760, 20, PURPLE]
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 
        for x in range(100, 800, 100):
            for y in range(50, 451, 300):
                wall = Wall(x, y, 20, 200, RED)
                self.wall_list.add(wall)
 
        for x in range(150, 700, 100):
            wall = Wall(x, 200, 20, 200, WHITE)
            self.wall_list.add(wall)
 
 
def main():
    """ Main Program """
 
    # Call this function so the Pygame library can initialize itself
    pygame.init()
 
    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 600])
 
    # Set the title of the window
    pygame.display.set_caption('Maze Runner')
 
    # Create the player paddle object
    player = Player(50, 50)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)
 
    rooms = []
 
    room = Room1()
    rooms.append(room)
 
    room = Room2()
    rooms.append(room)
 
    room = Room3()
    rooms.append(room)
 
    current_room_no = 0
    current_room = rooms[current_room_no]
 
    clock = pygame.time.Clock()
 
    done = False
 
    while not done:
 
        # --- Event Processing ---
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)
 
        # --- Game Logic ---
 
        player.move(current_room.wall_list)
 
        if player.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 2:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 790
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 790
 
        if player.rect.x > 801:
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 1:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 0
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 0
 
        # --- Drawing ---
        screen.fill(BLACK)
 
        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)
 
        pygame.display.flip()
 
        clock.tick(60)
 
    pygame.quit()
 
if __name__ == "__main__":
    main()