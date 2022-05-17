from cards import Suit


class TestSuit:
    suit = Suit

    def test_clubs_symbol(self):
        assert Suit.CLUBS.value[0] == "♣"

    def test_diamonds_symbol(self):
        assert Suit.DIAMONDS.value[0] == "♦"

    def test_hearts_symbol(self):
        assert Suit.HEARTS.value[0] == "♥"

    def test_spades_symbol(self):
        assert Suit.SPADES.value[0] == "♠"

    def test_clubs_precedence(self):
        assert Suit.CLUBS.value[1] == 1

    def test_diamonds_precedence(self):
        assert Suit.DIAMONDS.value[1] == 2

    def test_hearts_precedence(self):
        assert Suit.HEARTS.value[1] == 3

    def test_spades_precedence(self):
        assert Suit.SPADES.value[1] == 4
