# Putting the pieces together

Here's a module that combines the
new `CardCollection`, `Deck` and `Hand` classes with our
earlier `Card` class and a main routine that exercises them a little.
Try it out.

```python
# playing_cards_5.py
import random
class Card:
    face_values = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    suits = ['Clubs','Diamonds','Hearts','Spades']

    def __init__(self, cardnum):
        self.number = cardnum     

    def __str__(self):
        return self.face_value() + ' of ' + self.suit()

    def face_value(self):
        return Card.face_values[ self.number % 13 ]

    def suit( self ):
        return Card.suits[ self.number // 13 ]

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

class Deck(CardCollection):
    # Override ancestor's constructor, i.e. replace the default.
    def __init__(self):
        self.cards = []
        for cardnum in range(52):
            self.add( Card(cardnum) )

    # Alias the inherited method "size" as "cards_left",
    # because we usually ask how many cards are left in a
    # deck rather than asking about its size.
    def cards_left(self):
        return self.size()

    # Another alias. When using a deck of cards we talk about "dealing"
    # cards not "removing" them from the deck.
    def deal(self):
        return self.remove()

    # Add a new method, shuffle, that does not exist in ancestor class.
    def shuffle(self):
        for i in range(  2*self.size() ):
            self.cards.insert(random.randrange(len(self.cards)), self.cards.pop())

class Hand(CardCollection):
    pass    

if __name__ == '__main__':
    print('==================')
    print('Testing Card class')
    print('------------------')
    print()

    print('Your card number is 42.')
    c = Card(42)
    print('It\'s face value is:', c.face_value())
    print('It\'s suit is:', c.suit())
    print('It\'s printable representation is:', c)
    print()

    print('==================')
    print('Testing Deck class')
    print('------------------')
    print()

    print('Creating a new Deck...')
    print()

    d = Deck()
    print('The deck\'s printable representation:')
    print(d)
    print()

    print('Shuffling the deck...')
    d.shuffle()
    print('The deck after shuffling:')
    print(d)
    print()

    print('The deck has', d.cards_left(), 'cards.')
    print()

    print('Dealing a card...')
    card = d.deal()
    print('The card dealt is:', card)
    print('Dealing another card...')
    print('The card dealt is:', d.deal())
    print()

    print('Now the deck has', d.cards_left(), 'cards')
    print()
    
    print('==================')
    print('Testing Hand class')
    print('------------------')
    print()
    print('Creating a hand...')
    h = Hand()
    print('Dealing five cards from the deck into the hand...')
    for card in range(5):
        h.add(d.deal())
    print('Your hand of', h.size(), 'cards contains:', h)
```