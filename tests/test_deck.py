from cards import Deck, Card
from typing import Generator
from copy import deepcopy


class TestDeck:
    deck = Deck()

    def test_starting_deck_size(self):
        assert len(self.deck) == 52

    def test_draw_returns_generator(self):
        draw = self.deck.draw()
        assert isinstance(draw, Generator)

    def test_draw_single_card(self):
        card = next(self.deck.draw())
        assert isinstance(card, Card) and len(self.deck) == 51

    def test_draw_multiple_cards(self):
        draw = list(self.deck.draw(10))
        assert len(draw) == 10 and all(isinstance(card, Card) for card in draw)

    def test_deck_shuffle(self):
        deck_copy = deepcopy(self.deck)
        self.deck.shuffle()
        assert list(deck_copy) != list(self.deck)

    def test_deck_index(self):
        deck_size = len(self.deck)
        card = self.deck[10]
        assert isinstance(card, Card) and len(self.deck) == deck_size - 1
