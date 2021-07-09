#!/Users/jeff/.pyenv/shims/python

import random
from enum import Enum

class CardSuit(Enum):
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4

class CardValue(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        deck_list = []
        for suit in CardSuit:
            for value in CardValue:
                deck_list.append(str(value.name) + ' of ' + suit.name)

        print(f'\nDeck of cards list is: {deck_list}')
        print('\n')
        print('Hand of 5 random cards is:', random.choices(deck_list, k=5))

        return_str = self.value.name + ' of ' + self.suit.name
        return return_str

test_card = Card(CardSuit.HEARTS, CardValue.FIVE)
print(f'\nTesting Card class by creating a 5 of Hearts card: {test_card}\n')
