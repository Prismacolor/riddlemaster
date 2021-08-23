import random
from items.creatures import GoldDragon


# TODO needs test!!!
def get_riddle(creature):
    riddle = ''
    right_answers = []

    riddle_num = random.randint(0, len(creature.riddles))
    riddle = creature.riddles[riddle_num]
    right_answers = creature.answers[riddle_num]

    return riddle, right_answers


def is_riddle_answer_correct(player, tries, player_answer, riddle_answers, creature):
    end_quest = False
    right_answer = False
    single_try_bonus = 150
    if player_answer in riddle_answers:
        creature_response = creature.correct_answer
        player.points += creature.points
        player.purse += creature.value
        if tries == 1:
            player.points += single_try_bonus

        right_answer = True

        return right_answer, end_quest, creature_response
    else:
        if player.lives == 0:
            creature_response = creature.end_quest
            end_quest = True
            return right_answer, end_quest, creature_response
        else:
            creature_response = creature.wrong_answer
            player.lives -= 1
            tries += 1
            return right_answer, end_quest, creature_response




