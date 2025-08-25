import pygame as pg
import random
from plat import *

# Settings
WIDTH = 600
HEIGHT = 800
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (184, 51, 255)
ORANGE = (245, 187, 39)

class Game:
    def __init__(self):
        # initialize game window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("! Platformer Game !")
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # start a game
        self.all_sprite = pg.sprite.Group()
        self.run()

    def run(self):
        # game loop
        self.clock.tick(FPS)
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()

    def update(self):
        # game loop - update
        self.all_sprite.update()

    def event(self):
        # game loop - event
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False


    def draw(self):
        # game loop - draw
        self.screen.fill(BLACK)
        self.all_sprite.draw(self.screen)
        # after draw finish - fill the display
        pg.display.flip()

    def show_start_screen(self):
        # game over/control
        pass

    def show_go_screen(self):
        # game over/control
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()