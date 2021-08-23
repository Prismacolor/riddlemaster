import os
import pygame
import random
from items.creatures import *
from items.side_quest_items import *
from items.riddles import *

pygame.font.init()


'''  
def run_side_quest(creature):
        # enemy play
        generate sq item ?
        display instructions for quest (?.quest)

        Then:
        in side quest we must spawn items and put them in a list
        side_quest_item = ? this would be passed as parameter

        side_quest_items = []
        prev_used_locations = []
        dupe_locations = False
        num_of_items = ?.spawn

        for i in range(1, num_of_items):
            ?.item_spawn_location(WIDTH, HEIGHT)
            item_location = (?.x_pos, ?.y_pos)
            if item_location in prev_used_locations:
                i -= 1
                continue
            side_quest_items.append(?)
            prev_used_locations.append(item_location)

        all this needs to be in a timed loop!!!
        for enemy_ship in enemies:
            enemy_ship.draw(GAME_WINDOW)

        copy of list = enemies.copy()

        while time is not 0:
            for enemy in enemies_copy:
                if enemy.collision(player1):
                    player.pickup()
                    player1.score += ?.points
                    player1.purse += ?.value
                    enemies.remove(enemy)

        When time is 0, get length of list of thingies
        if player got 0 display sad message
        if player got some display not bad message
        if player got all give happy message
        have player give items to creature (for item in inventory, if item == side quest item, remove it)


def startup_game():
    # print welcome screen and ask if want to play
    # if yes, display instructions, if no quit
    # check first to see if won == true, if not, continue and play game


def main_play():
    # game variables
    level = 1
    side_quest_levels = [3, 6, 9, 12]
    
    # creature variables
    creature_x = 900
    creature_y = 900
    level_creature_map = {1: Basilisk(creature_x, creature_y), 2: Cerberus(creature_x, creature_y),
                          3: Owl(creature_x, creature_y), 4: Minotaur(creature_x, creature_y),
                          5: Unicorn(creature_x, creature_y), 6: Wyvern(creature_x, creature_y),
                          7: Phoenix(creature_x, creature_y), 8: Griffin(creature_x, creature_y),
                          9: Dryad(creature_x, creature_y), 10: Centaur(creature_x, creature_y),
                          11: Sphinx(creature_x, creature_y), 12: GoldDragon(creature_x, creature_y)}
    
    # player variables
    tries = 0
    
    # main riddle loop
    while your lives are not 0 and you didn't quit
        answeringRiddle = True
        level_creature = level_creature_map[level] # should this be in the game loop?
        spawn creature based on map
        create riddle and right answers using the get riddle function on your creature
        then use that info (riddle) to have your creature do intro and ask riddle
        
        create loop 
        while answeringRiddle == True:
            set up input so user can type in answer
            store answer in string and add one to the tries
            player_response = input(riddle) # how do we do user inputs in pygame
            tries += 1
            compare your answer and see if in right answers, then correctAnswer = true
            pass this info to riddle answered correctly function
            if correct answer is true and endquest is false, then display creature message and break loop
            if correct answer false and endquest is false, display creature message and continue
            if correct answer is false and endquest is true, display creature message and set game over break loop
        
        if game over then quit/break main loop
            
        if side quest level do side quest: put side level quest in separate function
        if level in side_quest_levels:
            run_side_quest()
        then call that function
        this will be the end of the main game loop
        
        level += 1
        
        check space invaders for end of loop setup 
'''


if __name__ == '__main__':
    startup_game()
