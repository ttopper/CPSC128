# `class CardCollection`

First we define our base class that contains the functionality common to
collections of cards:

    class CardCollection:
        def __init__(self):
            self.cards = []

        def size(self):
            return len(self.cards)

        def add(self, card):
            self.cards.append(card)

        def remove(self):
            return self.cards.pop()

        def __str__(self):
            return ', '.join( str(card) for card in self.cards )

Everything here should be familiar: The attributes and methods have just
been extracted from our earlier `Deck` and `Hand` classes.
