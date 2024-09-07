
a = 'Tim'
b = 'Tom'
lst = [b, a]
a = 'Matt'
lst[1] = lst[0]
print(lst)


"""
# scope_egs.py
print('Example 1: Local variable')
def f():
    x = 1
    print('Inside x is', x)
f()
# print('Outside x is', x) # Error! Comment this line out once you understand why it is an error.
print()

print('Example 2: Global variable')
x = 1
def f():
    print('Inside x is', x)
f()
print('Outside x is', x)
print()

print('Example 3: Local variable hides global variable inside function')
x = 1
def f():
    x = 2
    print('Inside x is', 2)
f()
print('Outside x is', x)
print()

print('Example 4: Lots of hiding')
x = 1
def outer():
    x = 2
    def inner():
        x = 3
        print('Here in inner x is', x)
    inner()
    print('Here in outer x is', x)
#inner() # Error! Comment this line out once you understand why it is an error.
outer()
print('Out here x is', x)

print('Example 5: Hiding the built-in len')
def len():
    print('I am not the real len')
len()


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



SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
FACE_VALUES = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
               'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
               'Queen', 'King')

def suit(cardnum):
    return SUITS[cardnum // 13]

def face_value(cardnum):
    return FACE_VALUES[cardnum % 13]

def label(cardnum):
    return face_value(cardnum) + " of " + suit(cardnum)

card = 15
print("Card", card, "is the", face_value(card), "of", suit(card))
print("Card", card, "is the", label(card))



SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
FACE_VALUES = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
               'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
               'Queen', 'King')

def suit(cardnum):
    return SUITS[cardnum // 13]

def face_value(cardnum):
    return FACE_VALUES[cardnum % 13]

card = 15
print("Card", card, "is the", face_value(card), "of", suit(card))



import random

def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
        
num = random.randint(0,100)

if is_even(num):
    print("Good news your magic number is even! 10 bonus points for you.")
else:
    print("Bad news, your magic number is odd.")
"""