import os
import pygame
import random
import logging

from items.creatures import *
from items.players import Player
from items.side_quest_items import *
from game_methods.item_methods import *
from game_methods.quest_methods import *
from game_methods.riddle_methods import *


pygame.font.init()

# ToDo add logging to necessary functions
# ToDo add spawn locations to all creatures in creature mapping dict

logger = logging.getLogger('game_play_logs')
logger.setLevel(logging.INFO)
lh = logging.FileHandler('../logs/gameplay.log')
logger.addHandler(lh)

WIDTH, HEIGHT = 850, 775
GAME_WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The Riddlemaster')

GAME_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('../assets/', 'green_background2.png')), (WIDTH, HEIGHT))


def initialize_game():
    title_font = pygame.font.SysFont('comicsans', 50)
    run = True

    while run:
        logger.info('Game start screen loading...')
        GAME_WINDOW.blit(GAME_BACKGROUND, (0, 0))
        title_label = title_font.render('Click your mouse to begin', True, (255, 255, 255))
        GAME_WINDOW.blit(title_label, (WIDTH / 2 - title_label.get_width() / 2, 325))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logger.info('Game session ended.')
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                logger.info('Game session starting...')
                main_game()

    pygame.quit()


def main_game():
    main_loop = True
    playing = True
    end_quest = False
    sidequest_levels = [3, 6, 9, 12]
    level = 1

    fps = 60
    clock = pygame.time.Clock()
    main_font = pygame.font.SysFont("comicsans", 45)

    creature_spawn_x, creature_spawn_y = WIDTH - (resize_x * 2 + 15), HEIGHT - (resize_y * 2 + 15)
    level_creature_mappings = {1: Basilisk(creature_spawn_x, creature_spawn_y),
                               2: Cerberus(creature_spawn_x, creature_spawn_y),
                               3: Owl(creature_spawn_x, creature_spawn_y),
                               4: Minotaur(creature_spawn_x, creature_spawn_y),
                               5: Unicorn(creature_spawn_x, creature_spawn_y),
                               6: Wyvern(creature_spawn_x, creature_spawn_y),
                               7: Phoenix(creature_spawn_x, creature_spawn_y),
                               8: Griffin(creature_spawn_x, creature_spawn_y),
                               9: Wyvern(creature_spawn_x, creature_spawn_y),
                               10: Centaur(creature_spawn_x, creature_spawn_y),
                               11: Sphinx(creature_spawn_x, creature_spawn_y),
                               12: GoldDragon(creature_spawn_x, creature_spawn_y)}

    user_player = Player('Tree Greenley', 25, HEIGHT - 110)
    level_creature = level_creature_mappings[level]

    def redraw_main_window():
        logger.info('Drawing window...')
        # set values for text variables
        GAME_WINDOW.blit(GAME_BACKGROUND, (0, 0))
        score = user_player.points
        coins = user_player.purse
        lives = user_player.lives

        # add text variables to window
        level_label = main_font.render(f'Level: {level}', True, (255, 255, 255))
        lives_label = main_font.render(f'Lives: {lives}', True, (255, 255, 255))
        score_label = main_font.render(f'Score: {score}', True, (255, 255, 255))
        coins_label = main_font.render(f'Coins: {coins}', True, (255, 255, 255))

        label_blocks = WIDTH/4

        # display the variables
        GAME_WINDOW.blit(level_label, (10, 10))
        GAME_WINDOW.blit(lives_label, (label_blocks, 10))
        GAME_WINDOW.blit(score_label, (label_blocks * 2, 10))
        GAME_WINDOW.blit(coins_label, (label_blocks * 3, 10))

        user_player.draw(GAME_WINDOW)
        level_creature.draw(GAME_WINDOW)

        pygame.display.update()  # update game window
        logger.info('Window completed...')

    while main_loop:
        clock.tick(fps)
        redraw_main_window()

        while playing:
            level_riddle, level_answers = get_riddle(level_creature)

'''         
            level_riddle, level_answers = get_riddle(level_creature)
            display the riddles in a banner
            have banner for user to input their response
            player_answer = that input
            
            right_answer, end_quest, creature_response = is_riddle_answer_correct(user_player, tries, player_answer, riddle_answers, level_creature)
            if end_quest:
                break
            else:
                display creature_response
                
            if level in sidequest_levels:
                run_side_quest(level, level_creature, user_player)
            
            level += 1
        
        if user_player.lives == 0 and end_quest:
               ask user if they want to continue
               if user_continue == 'y':
                   player.lives = 3
                   player.purse = 0
                   player.points = 0
                   continue
               else:
                   display end message
                   break
                   
    quit the game completely
    
    
def run_side_quest(level, creature, player):
    banner0 = 'Use arrow keys to move'
    side_quest_level_map = {3: Fireberries(), 6: GoldKey(), 9: WoodenStaff(), 12: DragonFang()}
    side_quest_item = side_quest_level_map[level]
        
    banner1 = creature.quest
    display banner1 
    user presses key and that goes away
    
    display banner0
    
    build screen/window for the side quest:
    spawn the items 
    sidequest_items_list = thingie
    create and start the timer
    
    need to somehow check list each time to see if any items still left
    remove item from screen if picked up
    when all items are collected and timer still running stop
    when timer runs out erase remaining items and stop
    return to original level screen
    
    evaluate the players' performance and update their scores
    sidequest_response = sidequest_completed(side_quest_item, sidequest_items_list, player, creature)
    display sidequest_response
'''


if __name__ == '__main__':
    initialize_game()
