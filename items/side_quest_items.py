import os
import pygame
import random
from game_methods.item_methods import collide, spawn

# gather images
FIRE_BERRIES = pygame.image.load(os.path.join('assets', 'fireberries.png'))
GOLD_KEY = pygame.image.load(os.path.join('assets', 'gold_key.png'))
WOODEN_STAFF = pygame.image.load(os.path.join('assets', 'wooden_staff.png'))
DRAGON_FANG = pygame.image.load(os.path.join('assets', 'dragon_fang.png'))

# resize images
resize_x = 100
resize_y = 100
FIRE_BERRIES = pygame.transform.scale(FIRE_BERRIES, (resize_x, resize_y))
GOLD_KEY = pygame.transform.scale(GOLD_KEY, (resize_x, resize_y))
WOODEN_STAFF = pygame.transform.scale(WOODEN_STAFF, (resize_x, resize_y))
DRAGON_FANG = pygame.transform.scale(DRAGON_FANG, (resize_x, resize_y))

# set width and height of game window
WIDTH, HEIGHT = 900, 900


# TODO figure out how to remove item from screen when picked up
# You'll need to spawn the item first in random location, then draw it.
class SideItem:
    def __init__(self):
        self.item_img = None
        self.x_pos = None
        self.y_pos = None

    def item_spawn_location(self, WIDTH, HEIGHT):
        image_x = self.item_img.get_width()
        image_y = self.item_img.get_height()
        x, y = spawn(image_x, image_y, WIDTH, HEIGHT)
        self.x_pos = x
        self.y_pos = y

    def draw(self, window):
        window.blit(self.item_img, (self.x_pos, self.y_pos))

    def found(self, obj):
        return collide(obj, self)


class FireBerries(SideItem):
    def __ini__(self):
        super().__init__()
        self.item_img = FIRE_BERRIES
        self.mask = pygame.mask.from_surface(self.item_img)
        self.spawn = random.randrange(0, 15)
        self.points = 15
        self.value = 25
        self.time = 10


class GoldKey(SideItem):
    def __ini__(self):
        super().__init__()
        self.item_img = GOLD_KEY
        self.mask = pygame.mask.from_surface(self.item_img)
        self.spawn = 3
        self.points = 500
        self.value = 2500
        self.time = 7


class WoodenStaff(SideItem):
    def __ini__(self):
        super().__init__()
        self.item_img = WOODEN_STAFF
        self.mask = pygame.mask.from_surface(self.item_img)
        self.spawn = 2
        self.points = 1000
        self.value = 5000
        self.time = 6


class DragonFang(SideItem):
    def __ini__(self, x_pos, y_pos):
        super().__init__()
        self.item_img = DRAGON_FANG
        self.mask = pygame.mask.from_surface(self.item_img)
        self.spawn = 1
        self.points = 1500
        self.value = 7500
        self.time = 5


