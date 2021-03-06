import os
import pygame

# TODO find image for the player!!!


class Player:
    def __init__(self, name, x_pos, y_pos):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.person_img = None
        self.inventory = []
        self.purse = 0
        self.points = 0
        self.lives = 3

    def answer_riddle(self, creature, riddle, riddle_answers, player_answer):
        # get player input in main game loop and use this to check it
        if player_answer in riddle_answers:
            self.points += creature.points
            self.purse += creature.worth
            return True
        else:
            self.lives -= 1
            return False

    def draw(self, window):
        pass

    def pickup(self, item):
        self.inventory.append(item)

    def give_item(self, item):
        self.inventory.remove(item)
