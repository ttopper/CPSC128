# Playing Card Functions 1

We've worked with playing cards a few times so far and will be doing so
again, so it would save us time if we had a standard set of tools for
working with them. In programming these tools are a set of functions
(and later classes) for manipulating them. Let's start with functions
that are passed a card number and return the face value of the card and
the suit of the card.

Recall that we determine the suit of a card by determining which block
of 13 it is in which we find by dividing the card number by thirteen.
Similarly we determine the face value of a card by determining its
offset within a group of thirteen using modulo. Packing those earlier
methods into functions gives us,

```python
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
```     

with output

```plaintext
>>> 
Card 15 is the Three of Diamonds
>>> 
```
We'll probably have to display card labels, e.g. “Three of Diamonds”,
fairly often so let's add a function for that too,

```python
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
```     

to get output like,

```plaintext
>>> 
Card 15 is the Three of Diamonds
Card 15 is the Three of Diamonds
>>> 
```

Note how we reused our `suit` and `face_value` functions to
define `label` in the same way we reused `is_even` to
define `is_odd` earlier.

Now if we have to write more programs that work with playing cards (and
you will dear student!) we can use these functions and avoid rewriting
this common functionality over and over again.
