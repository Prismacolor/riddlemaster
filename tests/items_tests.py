import unittest
from items.players import Player


class InventoryTest(unittest.TestCase):
    def test_inventory(self):
        player1 = Player('Player1', 24, 36)
        item = 'fireberries'
        player1.pickup(item)
        self.assertEqual(player1.inventory, ['fireberries'], 'Failed to add to inventory')


class InventoryRemovalTest(unittest.TestCase):
    def test_remove_inventory(self):
        player2 = Player('Player2', 24, 36)
        player2.inventory = ['apples', 'oranges', 'pears']
        player2.give_item(player2.inventory[1])
        self.assertEqual(player2.inventory, ['apples', 'pears'], 'Failed to remove item from inventory')


class RiddleAnswerTest(unittest.TestCase):
    def test_wrong_riddle_answer(self):
        player3 = Player('Player3', 24, 36)
        riddle = {'question': 'What is your favorite color', 'answers': 'green', 'points': 42, 'worth': 15}
        riddle_ans = player3.answer_riddle(riddle, 'blue')
        self.assertEqual(riddle_ans, False, 'This did not return the correct answer')
        self.assertEqual(player3.lives, 2, 'This did not return the correct answer')

    def test_right_riddle_answer(self):
        player3 = Player('Player3', 24, 36)
        riddle = {'question': 'What is your favorite color', 'answers': 'green', 'points': 42, 'worth': 15}
        riddle_ans = player3.answer_riddle(riddle, 'green')
        self.assertEqual(riddle_ans, True, 'This did not return the correct answer')
        self.assertEqual(player3.points, 42, 'This did not return the correct answer')
        self.assertEqual(player3.purse, 15, 'This did not return the correct answer')


