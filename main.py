from cards import Deck

if __name__ == "__main__":
    # create a deck
    deck = Deck()

    # draw a card
    card = next(deck.draw())
    print(f"draw: {card}")

    # pick a card
    pick = deck[10]
    print(f"pick: {pick}")

    # shuffle deck
    deck.shuffle()

    # draw multiple cards
    cards = list(deck.draw(4))
    print(f"cards: {cards}")

    # get number of cards
    deck_size = len(deck)
    print(f"deck size: {deck_size}")

    # reset deck
    deck.reset()
    print(f"deck: {deck} \nsize: {len(deck)}")
