from collections import namedtuple
from typing import Generator
from random import shuffle
from enum import Enum


class Suit(Enum):
    """ Symbolic representation of French suits depicted on playing cards. """
    CLUBS = u'\u2663', 1
    DIAMONDS = u'\u2666', 2
    HEARTS = u'\u2665', 3
    SPADES = u'\u2660', 4


class Card(namedtuple('Card', ['rank', 'suit'])):
    """ Represents a single playing card of a deck. """
    __slots__ = ()

    def __str__(self):
        return f'{self.rank}|{self.suit.value[0]}'


class Deck:
    """ Represents a classic deck of 52 playing cards. """
    __ranks__ = [str(n) for n in range(2, 11)] + list('JQKA')
    __suits__ = list(Suit)

    def __init__(self):
        self.__create_deck()
        self.shuffle()

    def __create_deck(self):
        self.__cards = [Card(rank, suit) for suit in self.__suits__ for rank in self.__ranks__]

    def draw(self, num_cards=1) -> Generator[Card, None, None]:
        for _ in range(num_cards):
            yield self.__cards.pop(0) if len(self) > 0 else None

    def shuffle(self):
        shuffle(self.__cards)

    def reset(self):
        self.__create_deck()

    def __len__(self):
        return len(self.__cards)

    def __getitem__(self, index):
        return self.__cards[index]

    def __str__(self):
        return str([f"{card}" for card in self.__cards])
