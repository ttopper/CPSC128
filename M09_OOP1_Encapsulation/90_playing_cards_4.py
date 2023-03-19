# playing_cards_4.py
#
# Add appropriate commenting to the classes and methods
#
# Kate, Winter 2023

import random

class Card:
    FACE_VALUES = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    SUITS = ['Clubs','Diamonds','Hearts','Spades']

    def __init__(self, cardnum):
        self.number = cardnum

    def __str__(self):
        return self.face_value() + ' of ' + self.suit()

    def face_value(self):
        return Card.FACE_VALUES[self.number % 13]

    def suit(self):
        return Card.SUITS[self.number // 13]
    
class Deck:
    def __init__(self):
        self.cards = []
        for cardnum in range(52):
            self.cards.append(Card(cardnum))
            
    def shuffle(self):
        for swap in range(2 * len(self.cards)):
            self.cards.insert(random.randrange(len(self.cards)), self.cards.pop())

    def cards_left(self):
        return len(self.cards)
    
    def deal(self, n=1):
        c = self.cards[-n:]
        del(self.cards[-n:])
        return c

    def __str__(self):
        s = ''
        for card in self.cards:
            s = s + str(card) + ', '
        return s

class Hand:
    def __init__(self):
        self.cards = []

    def add(self, cards):
        self.cards.extend(cards)

    def size(self):
        return len(self.cards)    

    def is_flush(self):
        pass

    def __str__(self):
        s = ''
        for card in self.cards:
            s = s + str(card) + ', '
        return s

if __name__ == '__main__':
    d = Deck()
    d.shuffle()
    print('d after shuffling =', d, '\n')
    print('d has', d.cards_left(), 'cards.\n')

    roxx = Hand()
    chris = Hand()

    for card in range(5):
        roxx.add(d.deal())
    print('Your hand of', roxx.size(), 'cards contains:', roxx)

    chris.add(d.deal(5))
    print('Your hand of', chris.size(), 'cards contains:', chris)

    print('\nThere are', d.cards_left(), 'cards left in the deck.')
    if roxx.is_flush():
        print('roxx rocks!')
