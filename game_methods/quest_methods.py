def quest_completed(og_sq_item_list, sq_item_list, creature):
    quest_success = ''
    if len(sq_item_list) == 0:
        # we picked up everything
        quest_success = 'success'
        return quest_success, creature.quest_success
    elif len(sq_item_list) == len(og_sq_item_list):
        # we picked up nothing
        quest_success = 'failed'
        return quest_success, creature.quest_failure
    else:
        # we picked up a few things
        quest_success = 'partial'
        return quest_success, creature.quest_partial


def display_quest_results(success_status, creature_message):
    pass
    # display results of quest
