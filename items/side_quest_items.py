import os
import pygame
import random
from game_methods.collisions import collide

FIRE_BERRIES = ''
GOLD_KEY = ''
DRAGON_FANG = ' '

WIDTH, HEIGHT = 900, 900


# TODO randomize generation of items
# TODO figure out how to remove item from screen when picked up
class SideItem:
    def __ini__(self, x_pos, y_pos):
        self.item_img = None
        self.x_pos = x_pos
        self.y_pos = y_pos

    def draw(self, window):
        window.blit(self.item_img, (self.x_pos, self.y_pos))

    def found(self, obj):
        return collide(obj, self)


class FireBerries(SideItem):
    def __ini__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        # self.item_img = 'a'
        # self.mask = pygame.mask.from_surface(self.item_img)
        self.spawn = random.randrange(0, 15)
        self.points = 15
        self.value = 25
        self.time = 10


class GoldKey(SideItem):
    def __ini__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        # self.item_img = 'a'
        # self.mask = pygame.mask.from_surface(self.item_img)
        self.spawn = 2
        self.points = 500
        self.value = 2500
        self.time = 5


class DragonFang(SideItem):
    def __ini__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        # self.item_img = 'a'
        # self.mask = pygame.mask.from_surface(self.item_img)
        self.spawn = 1
        self.points = 1500
        self.value = 7500
        self.time = 3


