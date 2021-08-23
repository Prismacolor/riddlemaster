import os
import pygame
import random
from items.riddles import *

# gather images
BASILISK = pygame.image.load(os.path.join('assets', 'basilisk.png'))
CENTAUR = pygame.image.load(os.path.join('assets', 'centaur.png'))
CERBERUS = pygame.image.load(os.path.join('assets', 'cerberus.png'))
DRYAD = pygame.image.load(os.path.join('assets', 'dryad.png'))
GOLD_DRAGON = pygame.image.load(os.path.join('assets', 'gold_dragon.png'))
GRIFFIN = pygame.image.load(os.path.join('assets', 'griffin.png'))
MINOTAUR = pygame.image.load(os.path.join('assets', 'minotaur.png'))
OWL = pygame.image.load(os.path.join('assets', 'owl.png'))
PHOENIX = pygame.image.load(os.path.join('assets', 'phoenix.png'))
SPHINX = pygame.image.load(os.path.join('assets', 'sphinx.png'))
UNICORN = pygame.image.load(os.path.join('assets', 'unicorn.png'))
WYVERN = pygame.image.load(os.path.join('assets', 'wyvern.png'))

# resize images
resize_x = 100
resize_y = 100
BASILISK = pygame.transform.scale(BASILISK, (resize_x, resize_y))
CENTAUR = pygame.transform.scale(CENTAUR, (resize_x, resize_y))
CERBERUS = pygame.transform.scale(CERBERUS, (resize_x, resize_y))
DRYAD = pygame.transform.scale(DRYAD, (resize_x, resize_y))
GOLD_DRAGON = pygame.transform.scale(GOLD_DRAGON, (resize_x, resize_y))
GRIFFIN = pygame.transform.scale(GRIFFIN, (resize_x, resize_y))
MINOTAUR = pygame.transform.scale(MINOTAUR, (resize_x, resize_y))
OWL = pygame.transform.scale(OWL, (resize_x, resize_y))
PHOENIX = pygame.transform.scale(PHOENIX, (resize_x, resize_y))
SPHINX = pygame.transform.scale(SPHINX, (resize_x, resize_y))
UNICORN = pygame.transform.scale(UNICORN, (resize_x, resize_y))
WYVERN = pygame.transform.scale(WYVERN, (resize_x, resize_y))


class Creature:
    def __init__(self, x_pos, y_pos):
        self.intro = 'Hihi!'
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.creature_img = None
        self.riddles = []
        self.points = 0
        self.value = 0
        self.correct_answer = ''
        self.wrong_answer = ''
        self.end_quest = ''
        self.quest = None
        self.quest_success = None
        self.quest_failure = None
        self.quest_partial = None

    def ask_riddle(self, riddle):
        statement = self.intro + riddle
        return statement

    def give_side_quest(self):
        return self.quest


class Basilisk(Creature):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.intro = 'In me you have found death. Ansssswer my riddle and I will let you live. '
        self.creature_img = BASILISK
        self.mask = pygame.mask.from_surface(self.creature_img)
        self.level = 0
        self.riddles = riddles.basilisk_riddles
        self.answers = riddles.basilisk_answers
        self.points = 150
        self.value = 75
        self.correct_answer = 'Ssssss, fortune favors you...for now.'
        self.wrong_answer = 'Not quite, not quite...'
        self.end_quest = 'O.O *stare of death* O.O'


class Cerberus(Creature):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.intro = 'Once I guarded the gates of hell. But today I am on vacation. Wanna play riddles? '
        self.creature_img = CERBERUS
        self.mask = pygame.mask.from_surface(self.creature_img)
        self.level = 1
        self.riddles = riddles.cerberus_riddles
        self.answers = riddles.cerberus_answers
        self.points = 250
        self.value = 125
        self.correct_answer = 'Oooooh, you are good! Wanna play guard the stick?'
        self.wrong_answer = 'Awww, try again...'
        self.end_quest = 'Hmmm, maybe Hades will let me take you back to the underworld with me...'


class Owl(Creature):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.intro = 'Hoo-hoo, what a young thing you are. A fledgling! Let us see if you have any wisdom yet. '
        self.creature_img = OWL
        self.mask = pygame.mask.from_surface(self.creature_img)
        self.level = 3
        self.riddles = riddles.owl_riddles
        self.answers = riddles.owl_answers
        self.points = 350
        self.value = 175
        self.correct_answer = 'Well, I guess you are wiser than you look.'
        self.wrong_answer = 'That isn\'t right...'
        self.end_quest = 'Hmphf, a waste of my morning. Good day!'
        self.quest = 'Hoo-Hoo. Hoo-Hoo. With age comes wisdom. The key to a long life is fireberries! Go into the ' \
                     'garden and find as many as you can and bring them to me for a reward. Hoo-Hoo.'
        self.quest_success = 'Ah, you have my gratitude. May your life be long and prosperous.'
        self.quest_failure = 'Eh, a bit slow for one so young. Better luck next time.'
        self.quest_partial = 'Some is better than none, hoo-hoo!'


class Minotaur(Creature):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.intro = 'Bah, I was hoping for a warrior to cross my path today. Since you have no sword, let us test ' \
                     'your wits. '
        self.creature_img = MINOTAUR
        self.mask = pygame.mask.from_surface(self.creature_img)
        self.level = 4
        self.riddles = riddles.minotaur_riddles
        self.answers = riddles.minotaur_answers
        self.points = 550
        self.value = 275
        self.correct_answer = 'You are no warrior, but you have earned my respect.'
        self.wrong_answer = 'That answer is not correct.'
        self.end_quest = 'The minotaur has become enraged and chased you away with his axe.'


class Unicorn(Creature):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.intro = 'I see great wisdom in your face... '
        self.creature_img = UNICORN
        self.mask = pygame.mask.from_surface(self.creature_img)
        self.level = 5
        self.riddles = riddles.unicorn_riddles
        self.answers = riddles.unicorn_answers
        self.points = 750
        self.value = 375
        self.correct_answer = 'Ah my vision has proven true. Be well, fellow traveler.'
        self.wrong_answer = 'Think harder...'
        self.end_quest = 'They do say never judge a book by its cover...'


class Wyvern(Creature):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.intro = 'Gooooold, gooooold, go- Ah, a visitor! Come, let us see if you are a worthy creature. '
        self.creature_img = WYVERN
        self.mask = pygame.mask.from_surface(self.creature_img)
        self.level = 6
        self.riddles = riddles.wyvern_riddles
        self.answers = riddles.wyvern_answers
        self.points = 950
        self.value = 475
        self.correct_answer = 'Hmmmm. I approve.'
        self.wrong_answer = 'That is not the correct answer, human.'
        self.end_quest = 'The wyvern is not a merciful creature, and burns you to ash.'
        self.quest = 'You have solved my riddle, nice, nice. Since you are clearly a person of skill I shall give' \
                     'you a task. Three gold keys do I covet, bring them to me and I shall reward you.'
        self.quest_success = 'Gold, gold, glorious gold...'
        self.quest_failure = 'I was unwise. I overestimated your skills. I must find a champion more worthy...'
        self.quest_partial = 'Only one...I had higher expectations...'


class Phoenix(Creature):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.intro = 'Tee-tee-tee, tee-tee-tee. Here is a riddle for thee... '
        self.creature_img = PHOENIX
        self.mask = pygame.mask.from_surface(self.creature_img)
        self.level = 7
        self.riddles = riddles.phoenix_riddles
        self.answers = riddles.phoenix_answers
        self.points = 1250
        self.value = 625
        self.correct_answer = 'Well done, well done, and your praises will be sung!'
        self.wrong_answer = 'Teeteetee, teeteetee, think again, will ye?'
        self.end_quest = 'Teeteetee, teeteetee, alas, it was not meant to be.'


class Griffin(Creature):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.intro = 'My young are hungry...perhaps they will enjoy your bones. If you can answer my riddle, I will' \
                     'spare your life. '
        self.creature_img = GRIFFIN
        self.mask = pygame.mask.from_surface(self.creature_img)
        self.level = 8
        self.riddles = riddles.griffin_riddles
        self.answers = riddles.griffin_answers
        self.points = 1550
        self.value = 775
        self.correct_answer = 'Hmphf, I suppose I shall have to find more frogs for my young.'
        self.wrong_answer = 'I wonder if you have much marrow...'
        self.end_quest = 'The griffin carries you away to her young.'


class Dryad(Creature):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.intro = 'Hmmmmmmm. Hello, wanderer. '
        self.creature_img = DRYAD
        self.mask = pygame.mask.from_surface(self.creature_img)
        self.level = 9
        self.riddles = riddles.dryad_riddles
        self.answers = riddles.dryad_answers
        self.points = 1850
        self.value = 925
        self.correct_answer = 'Very good.'
        self.wrong_answer = '...'
        self.end_quest = 'The dryad turns you into a tree until you become a little wiser.'
        self.quest = 'I must sow the earth for the summer planting. But I have misplaced my staffs. Please find them' \
                     'for me...'
        self.quest_success = 'Ah, there they are. Now to begin the planting...'
        self.quest_failure = 'You were not able to find my staffs? Then I must find them myself...'
        self.quest_partial = 'Well, one staff will be enough to get me started.'


class Centaur(Creature):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.intro = 'The stars have foretold of your coming... '
        self.creature_img = CENTAUR
        self.mask = pygame.mask.from_surface(self.creature_img)
        self.level = 10
        self.riddles = riddles.centaur_riddles
        self.answers = riddles.centaur_answers
        self.points = 2350
        self.value = 1175
        self.correct_answer = 'May the stars always smile upon you.'
        self.wrong_answer = 'Open the third eye.'
        self.end_quest = 'The centaur is gravely disappointed and foretells your doom.'


class Sphinx(Creature):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.intro = 'Do you like my new nose? Oh, oh! '
        self.creature_img = SPHINX
        self.mask = pygame.mask.from_surface(self.creature_img)
        self.level = 11
        self.riddles = riddles.sphinx_riddles
        self.answers = riddles.spinx_answers
        self.points = 2650
        self.value = 1325
        self.correct_answer = 'You are like, so smart!'
        self.wrong_answer = 'Hmmm, that isn\'t the right answer, honey.'
        self.end_quest = 'Awww, I\'m sorry. Maybe you should crack open a book sometime?'


class GoldDragon(Creature):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.intro = 'Thou hast come to seek thy fortune? Thou must have wisdom and courage first. '
        self.creature_img = GOLD_DRAGON
        self.mask = pygame.mask.from_surface(self.creature_img)
        self.level = 12
        self.riddles = riddles.dryad_riddles
        self.answers = riddles.dryad_answers
        self.points = 3400
        self.value = 1700
        self.correct_answer = 'Thou hast passed the first trial.'
        self.wrong_answer = 'Do not prove thyself a fool.'
        self.end_quest = 'Thou hast not been blessed with the gift of wisdom...I shall banish thee to the darker ' \
                         'realms.'
        self.quest = 'It is almost time for the summer solstice. My people require a Dragon\'s Fang to complete the' \
                     'ritual of Gaia. Find one and I will grant thee a great reward.'
        self.quest_success = 'This a fine dagger. My people will be pleased. And now for thy reward...'
        self.quest_failure = 'Thou hast failed me. That is most unwise...Let us hope thou dost not come to regret thy' \
                             'failure.'
        self.quest_partial = 'There is no partial success here.'
        self.gold_dragon_bonus_pnt = 3000
        self.gold_dragon_bonus_coins = 2500
