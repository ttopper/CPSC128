# Example: Playing Card Functions 2

Just to provide further examples for study here is a slightly more
complete playing cards module:

```python
# playing_cards_2.py
# Tim Topper
# Fall 2012
''' Contains functions and values for working with playing cards.
Cards are simply represented by the numbers from 0 to 51 mapped as follows:
0 : Ace of Clubs
1 : Two of Clubs
...
12 : King of Clubs
13 : Ace of Diamonds
...
25 : King of Diamonds
26 : Ace of Hearts
...
50 : Queen of Spades
51 : King of Spades
A deck of cards and hands of cards are both simply lists of card numbers.
'''

import random

SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
FACE_VALUES = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
            'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
            'Queen', 'King')

def suit(cardnum):
'''Returns the suit name, e.g. 'Clubs', of the card it is passed.'''
return SUITS[cardnum // 13]

def face_value(cardnum):
'''Returns the face value, e.g. 'Three', of the card it is passed.'''
return FACE_VALUES[cardnum % 13]

def label(cardnum):
'''Returns a string describing the card it is passed,
e.g. 'Queen of Hearts'.'''
return face_value(cardnum) + " of " + suit(cardnum)

def create_deck():
'''Returns a new unshuffled deck of cards.'''
return list(range(0,52))

def shuffle(deck):
'''Shuffles the card list it is passed by selecting pairs
of cards at random and swapping them.'''
shuffles = 2 * len(deck)
for shuffle in range(shuffles):
    posn1 = random.randint(0, len(deck)-1)
    posn2 = random.randint(0, len(deck)-1)
    deck[posn1], deck[posn2] = deck[posn2], deck[posn1]
return

def deal(deck):
'''Returns (deals) a card from deck.'''
return deck.pop()

if __name__ == '__main__':
# Unit tests
# N.B. More needed!
deck = create_deck()
print('New deck:', deck)
shuffle( deck)
print('Shuffled deck:', deck)
print('Dealing a card...')
card = deal(deck)
print('    Card number:', card)
print('    Face value:', face_value(card))
print('    Suit:', suit(card))
print('    Description:', label(card))
print('Deck after dealing:', deck)
```

Here is an output when it is run,

```plaintext
>>> 
New deck: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]
Shuffled deck: [13, 26, 10, 15, 6, 50, 12, 2, 27, 4, 0, 11, 5, 37, 16, 
49, 14, 30, 1, 18, 35, 42, 41, 34, 20, 25, 22, 51, 29, 21, 28, 31, 3, 32,
38, 7, 17, 33, 24, 43, 46, 39, 8, 47, 45, 23, 44, 19, 48, 9, 36, 40]
Dealing a card...
Card number: 40
Face value: Two
Suit: Spades
Description: Two of Spades
Deck after dealing: [13, 26, 10, 15, 6, 50, 12, 2, 27, 4, 0, 11, 5, 37,
16, 49, 14, 30, 1, 18, 35, 42, 41, 34, 20, 25, 22, 51, 29, 21, 28, 31, 
3, 32, 38, 7, 17, 33, 24, 43, 46, 39, 8, 47, 45, 23, 44, 19, 48, 9, 36]
>>> 
```
and here is the output from `help` after importing it,

```plaintext
>>> import playing_cards_2
>>> help( playing_cards_2)
Help on module playing_cards_2:
NAME
playing_cards_2

DESCRIPTION
Contains functions and values for working with playing cards.
Cards are simply represented by the numbers from 0 to 51 mapped as follows:
0 : Ace of Clubs
1 : Two of Clubs
...
12 : King of Clubs
13 : Ace of Diamonds
...
25 : King of Diamonds
26 : Ace of Hearts
...
50 : Queen of Spades
51 : King of Spades
A deck of cards and hands of cards are both simply lists of card numbers.

FUNCTIONS
create_deck()
    Returns a new unshuffled deck of cards.

deal(deck)
    Returns (deals) a card from deck.

face_value(cardnum)
    Returns the face value, e.g. 'Three', of the card it is passed.

label(cardnum)
    Returns a string describing the card it is passed,
    e.g. 'Queen of Hearts'.

shuffle(deck)
    Shuffles the card list it is passed by selecting pairs
    of cards at random and swapping them.

suit(cardnum)
    Returns the suit name, e.g. 'Clubs', of the card it is passed.

DATA
FACE_VALUES = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', ...
SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')

FILE
\\home\profiles\kchatfieldreed\documents\cpsc128_intro_oo\programs\playing_cards_2.py

>>> 
```