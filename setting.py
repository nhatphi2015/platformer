import pygame as pg
# game options
TITLE = "Jumpy!"
WIDTH = 500
HEIGHT = 620
FPS = 60
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAVITY = 0.7
PLAYER_JUMP = 50
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POW_LAYER = 1
MOB_LAYER = 2
CLOUD_LAYER = 0 

# game properties
BOOST_POWER = 130
POW_SPAWN_PCT = 1
MOB_FREQ = 4000

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