import pygame

#idea for Settings class from python crash course... the variables are mostly me except screen width and height i guess
class Settings():
    def __init__(self):
        self.screen_width = 1024
        self.screen_height = 768
        self.wall_width = 32
        self.wall_height = 32
        self.wall_color = [0,0,255]
        self.box_color = [255, 0, 0]
        self.fin_color = [0, 255, 0]
        self.mc_height = 16
        self.mc_width = 16
        self.TILESIZE = 32