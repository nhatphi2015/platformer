import pygame as pg
from setting import *
from random import choice, randrange
vec = pg.math.Vector2

class Spritesheet:
    # utility class for loading and parsing Spritesheet
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert_alpha()

    def get_image(self, x, y, width, height):
        # grab on image out of a larger spritesheet
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image.set_colorkey((0, 0, 0)) 
        image = pg.transform.scale(image, (width // 2, height // 2))
        return image

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = PLAYER_LAYER
        self.group = game.all_sprite
        pg.sprite.Sprite.__init__(self, self.group)
        self.game = game
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
        self.load_image()
        self.image = self.standing_frame[0]
        self.rect = self.image.get_rect()
        self.rect.center = (40, HEIGHT - 100) 
        self.pos = vec(40, HEIGHT - 100)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def load_image(self):
        self.standing_frame = [self.game.spritesheet.get_image(614, 1063, 120, 191),
                               self.game.spritesheet.get_image(690, 406, 120, 201),]
        for frame in self.standing_frame:
            frame.set_colorkey(BLACK)
        self.walk_frame_r = [ self.game.spritesheet.get_image(678, 860, 120, 201),
                              self.game.spritesheet.get_image(692, 1458, 120, 207)]
        self.walk_frame_l = []
        for frame in self.walk_frame_r:
            frame.set_colorkey(BLACK)
            self.walk_frame_l.append(pg.transform.flip(frame, True, False))
        self.jump_frame = self.image = self.game.spritesheet.get_image(416, 1660, 150, 181)
        self.jump_frame.set_colorkey(BLACK)

    def jump_cut(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

    def jump(self):
        # jump only stand on the platform
        self.rect.y += 2
        hits = pg.sprite.spritecollide(self, self.game.platform, False)
        self.rect.y -= 2
        if hits and not self.jumping:
        # if not self.jumping:
            self.game.jump_sound.play()
            self.vel.y = -PLAYER_JUMP

    def update(self):
        self.animate()
        self.acc = vec(0, PLAYER_GRAVITY)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # apply friction
        self.acc += self.vel * PLAYER_FRICTION
        # equation of motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH + self.rect.width / 2:
            self.pos.x = 0 - self.rect.width / 2
        if self.pos.x < 0 - self.rect.width / 2:
            self.pos.x = WIDTH + self.rect.width / 2

        self.rect.midbottom = self.pos

    def animate(self):
        now = pg.time.get_ticks()
        if self.vel.x != 0:
            self.walking = True
        else:
            self.walking = False
            # show walk animation
        if self.walking:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_frame_l)
                bottom = self.rect.bottom
                if self.vel.x > 0:
                    self.image = self.walk_frame_r[self.current_frame]
                else:
                    self.image = self.walk_frame_l[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
        self.mask = pg.mask.from_surface(self.image)

        # show idle animation
        if not self.jumping and not self.walking:
            if now - self.last_update > 350:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.standing_frame)
                bottom = self.rect.bottom
                self.image = self.standing_frame[self.current_frame]
                self.rect.bottom = bottom

class Cloud(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = CLOUD_LAYER
        self.group = game.all_sprite, game.cloud
        pg.sprite.Sprite.__init__(self, self.group)
        self.game = game
        self.image = choice(self.game.cloud_image)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

class Platform(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = PLATFORM_LAYER
        self.group = game.all_sprite, game.platform
        pg.sprite.Sprite.__init__(self, self.group)
        self.game = game
        image = [self.game.spritesheet.get_image(0, 288, 380, 94), self.game.spritesheet.get_image(213, 1662, 201, 100)]
        self.image = choice(image)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        if randrange(100) < POW_SPAWN_PCT:
            Pow(self.game, self)

class Pow(pg.sprite.Sprite):
    def __init__(self, game, plat):
        self._layer = POW_LAYER
        self.group = game.all_sprite, game.powerups
        pg.sprite.Sprite.__init__(self, self.group)
        self.game = game
        self.plat = plat
        self.type = choice(['boost'])
        self.image = self.game.spritesheet.get_image(820, 1805, 71, 70)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.plat.rect.centerx
        self.rect.bottom = self.plat.rect.top -5

    def update(self):
        self.rect.bottom = self.plat.rect.top -5
        if not self.game.platform.has(self.plat):
            self.kill()

class Mob(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = MOB_LAYER
        self.group = game.all_sprite, game.mob
        pg.sprite.Sprite.__init__(self, self.group)
        self.game = game
        self.image_up = self.game.spritesheet.get_image(566, 510, 122, 139)
        self.image_up.set_colorkey(BLACK)
        self.image_down = self.game.spritesheet.get_image(568, 1534, 122, 135)
        self.image_down.set_colorkey(BLACK)
        self.image = self.image_up
        self.rect = self.image.get_rect()
        self.rect.centerx = choice([-100, WIDTH + 100])
        self.vx = randrange(1, 4)
        if self.rect.centerx > WIDTH:
            self.vx += 1
        self.rect.y = randrange(HEIGHT / 2)
        self.vy = 0
        self.dy = 0.5

    def update(self):
        self.rect.x += self.vx
        self.vy += self.dy
        if self.vy > 3 or self.vy < -3:
            self.dy *= -1
        center = self.rect.center
        if self.dy < 0:
            self.image = self.image_up
        else:
            self.image = self.image_down
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.center = center
        self.rect.y += self.vy
        if self.rect.left > WIDTH * 100 or self.rect.right < -100:
            self.kill()