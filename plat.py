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
        self.font_name = pg.font.match_font(FONT_NAME)

    def new(self):
        # start a game
        self.score = 0
        self.all_sprite = pg.sprite.Group()
        self.platform = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprite.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprite.add(p)
            self.platform.add(p)
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
        # check if player hit hits - only it falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platform, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
        # if player reach top 1/4 of screen
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platform:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    self.score += 10

        # die!
        if self.player.rect.bottom > HEIGHT:
            for sprite in self.all_sprite:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.platform) == 0:
            self.playing = False
        # spawn new platform to keep same average number
        while len(self.platform) < 6:
            width = random.randrange(50, 100)
            p = Platform(random.randrange(0, WIDTH - width),random.randrange(-75, -50. ),width, 20)
            self. platform.add(p)
            self.all_sprite.add(p)

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
        self.draw_text(str(self.score), 22, WHITE, WIDTH /2, 15)
        # after draw finish - fill the display
        pg.display.flip()

    def show_start_screen(self):
        # game over/control
        pass

    def show_go_screen(self):
        # game over/control
        pass

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface)

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()