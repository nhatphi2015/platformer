import pygame as pg
# game options
TITLE = "Jumpy!"
WIDTH = 600
HEIGHT = 800
FPS = 60
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"

# Player properties
PLAYER_ACC = 0.7
PLAYER_FRICTION = -0.100
PLAYER_GRAVITY = 0.8
PLAYER_JUMP = 67


# Starting platform
PLATFORM_LIST = [(0, HEIGHT - 60),
                (WIDTH / 2 - 50, HEIGHT * 3 / 4 - 50),
                (125, HEIGHT - 350),
                (350, 200),
                (175, 60)]

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (184, 51, 255)
ORANGE = (245, 187, 39)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = LIGHTBLUE