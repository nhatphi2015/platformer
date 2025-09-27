import pygame as pg
# game options
TITLE = "Jumpy!"
WIDTH = 480
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAVITY = 0.8
PLAYER_JUMP = 57

# game properties
BOOST_POWER = 180
POW_SPAWN_PCT = 5

# Starting platform
PLATFORM_LIST = [(0, HEIGHT - 40),
                (WIDTH / 2 - 50, HEIGHT * 3 / 4),
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