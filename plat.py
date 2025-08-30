import pygame as pg
import random
from setting import *
from sprite import *


class Game:
    def __init__(self):
        # initialize game window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Jumpy!")
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # start a game
        self.all_sprite = pg.sprite.Group()
        self.platform = pg.sprite.Group()
        self.player = Player()
        self.all_sprite.add(self.player)
        p1 = Platform(0, HEIGHT - 40, WIDTH, 40)
        self.all_sprite.add(p1)
        self.platform.add(p1)
        p2 = Platform(WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20)
        self.all_sprite.add(p2)
        self.platform.add(p2)
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
        hits = pg.sprite.spritecollide(self.player, self.platform, False)
        if hits:
            self.player.pos.y = hits[0].rect.top
            self.player.vel.y = 0

    def event(self):
        # game loop - event
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()


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