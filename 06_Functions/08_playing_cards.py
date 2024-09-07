# playing_cards.py
#
# A file with some functions for working with playing cards defined.
#
# Kate Chatfield-Reed
# Winter 2023

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

print('My name is', __name__) # will print the program name
card = 15
print("Card", card, "is the", face_value(card), "of", suit(card))
print("Card", card, "is the", label(card))
