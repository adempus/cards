from collections import namedtuple, deque
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
    _ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    _suits = list(Suit)

    def __init__(self):
        self.__create_deck()

    def __create_deck(self):
        self._cards = [Card(rank, suit) for suit in self._suits for rank in self._ranks]
        self.shuffle()

    def draw(self, num_cards=1) -> Generator[Card, None, None]:
        for _ in range(num_cards):
            yield self._cards.pop() if len(self) > 0 else None

    def shuffle(self):
        shuffle(self._cards)

    def reset(self):
        self.__create_deck()

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        card = self._cards[index]
        return card

    def __str__(self):
        return str([f"{card}" for card in self._cards])
