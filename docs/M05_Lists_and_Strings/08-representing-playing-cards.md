# Representing Playing Cards

In addition to computational uses such as arrays of counters, lists can also be used to represent real-world “objects”, in particular composite objects that have multiple components. Consider representing a deck of playing cards. A deck of cards is made up of many similar, but not identical, objects. Plainly a deck of cards cannot be easily represented by a single integer, string or floating point value because it has so many constituents, but an ordered list seems like a promising alternative.

## Our representation: The simplest thing that could possibly work

A standard deck of playing cards consists of 52 unique cards. Each card combines one of 13 face values (Ace up to King) and one of four suits (Clubs, Diamonds, Hearts and Spades). If we agree on the ordering of face values and suits then we could just refer to each card by a number from 0 to 51, i.e. card 0 is the Ace of Clubs, card 3 is the 4 of Clubs, and card 50 is the Queen of Spades. If we follow standard contract bridge ordering we would number the cards as follows,

```plaintext
 0 Ace   Clubs    13 Ace   Diamonds    26 Ace   Hearts    39 Ace   Spades
 1 Two   Clubs    14 Two   Diamonds    27 Two   Hearts    40 Two   Spades
 2 Three Clubs    15 Three Diamonds    28 Three Hearts    41 Three Spades
 3 Four  Clubs    16 Four  Diamonds    29 Four  Hearts    42 Four  Spades
 4 Five  Clubs    17 Five  Diamonds    30 Five  Hearts    43 Five  Spades
 5 Six   Clubs    18 Six   Diamonds    31 Six   Hearts    44 Six   Spades
 6 Seven Clubs    19 Seven Diamonds    32 Seven Hearts    45 Seven Spades
 7 Eight Clubs    20 Eight Diamonds    33 Eight Hearts    46 Eight Spades
 8 Nine  Clubs    21 Nine  Diamonds    34 Nine  Hearts    47 Nine  Spades
 9 Ten   Clubs    22 Ten   Diamonds    35 Ten   Hearts    48 Ten   Spades
10 Jack  Clubs    23 Jack  Diamonds    36 Jack  Hearts    49 Jack  Spades
11 Queen Clubs    24 Queen Diamonds    37 Queen Hearts    50 Queen Spades
12 King  Clubs    25 King  Diamonds    38 King  Hearts    51 King  Spades
```

And a new ordered full deck of cards would be represented by the list,

```python
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ..., 47, 48, 49, 50, 51]
```

So in Python we can initialize a full deck just by saying:

```python
deck = list(range(52))
```

since the `range` command produces a `range` object, which can be cast to the list above.

To work with the card numbers we'll need to be able to figure out the suit and face value of a card given its card number.

## Suit from card number

To get the suit a card belongs to from its card number consider how the suits are grouped:

```plaintext
 0 Clubs    13 Diamonds    26 Hearts    39 Spades
 1 Clubs    14 Diamonds    27 Hearts    40 Spades
 2 Clubs    15 Diamonds    28 Hearts    41 Spades
 3 Clubs    16 Diamonds    29 Hearts    42 Spades
 4 Clubs    17 Diamonds    30 Hearts    43 Spades
 5 Clubs    18 Diamonds    31 Hearts    44 Spades
 6 Clubs    19 Diamonds    32 Hearts    45 Spades
 7 Clubs    20 Diamonds    33 Hearts    46 Spades
 8 Clubs    21 Diamonds    34 Hearts    47 Spades
 9 Clubs    22 Diamonds    35 Hearts    48 Spades
10 Clubs    23 Diamonds    36 Hearts    49 Spades
11 Clubs    24 Diamonds    37 Hearts    50 Spades
12 Clubs    25 Diamonds    38 Hearts    51 Spades
```

### Solution 1

One way to get the suit from the card number is to test the card number to see which group of 13 (i.e. which suit) it is in.

```python
if cardnum < 13 :
    suit = 'Clubs'
elif cardnum < 26 :
    suit = 'Diamonds'
elif cardnum < 39 :
    suit = 'Hearts'
else :
    suit = 'Spades'
```

### Solution 2

An alternative is to get the suit from the card number by dividing the card number by 13. The result tells us which of the groups of 13 our card number is in:

```python
suit = cardnum // 13
if suit == 0 :
    suit = 'Clubs'
elif suit == 1 :
    suit = 'Diamonds'
elif suit == 2 :
    suit = 'Hearts'
else :
    suit = 'Spades'
```

## Face value from card number

To get the face value from the card number we need to look at where our card occurs _within_ its group of 13.

```plaintext
 0 Ace       13 Ace       26 Ace       39 Ace
 1 Two       14 Two       27 Two       40 Two
 2 Three     15 Three     28 Three     41 Three
 3 Four      16 Four      29 Four      42 Four
 4 Five      17 Five      30 Five      43 Five
 5 Six       18 Six       31 Six       44 Six
 6 Seven     19 Seven     32 Seven     45 Seven
 7 Eight     20 Eight     33 Eight     46 Eight
 8 Nine      21 Nine      34 Nine      47 Nine
 9 Ten       22 Ten       35 Ten       48 Ten
10 Jack      23 Jack      36 Jack      49 Jack
11 Queen     24 Queen     37 Queen     50 Queen
12 King      25 King      38 King      51 King
```

### Solution 1

We could do this as we did above by writing the logic directly:

```python
if cardnum == 0 or cardnum == 13 or cardnum == 26 or cardnum == 39 :
    face_value = 'Ace'
elif cardnum == 1 or cardnum == 14 or cardnum == 27 or cardnum == 40 :
    face_value = 'Two'
elif cardnum == 2 or cardnum == 15 or cardnum == 28 or cardnum == 41 :
    face_value = 'Three'
elif cardnum == 3 or cardnum == 16 or cardnum == 29 or cardnum == 42 :
    face_value = 'Four'
elif cardnum == 4 or cardnum == 17 or cardnum == 30 or cardnum == 43 :
    face_value = 'Five'
elif cardnum == 5 or cardnum == 18 or cardnum == 31 or cardnum == 44 :
    face_value = 'Six'
elif cardnum == 6 or cardnum == 19 or cardnum == 32 or cardnum == 45 :
    face_value = 'Seven'
elif cardnum == 7 or cardnum == 20 or cardnum == 33 or cardnum == 46 :
    face_value = 'Eight'
elif cardnum == 8 or cardnum == 21 or cardnum == 34 or cardnum == 47 :
    face_value = 'Nine'
elif cardnum == 9 or cardnum == 22 or cardnum == 35 or cardnum == 48 :
    face_value = 'Ten'
elif cardnum == 10 or cardnum == 23 or cardnum == 36 or cardnum == 49 :
    face_value = 'Jack'
elif cardnum == 11 or cardnum == 24 or cardnum == 37 or cardnum == 50 :
    face_value = 'Queen'
else:
    face_value = 'King'
```

### Solution 2

Or we could do the same thing using list membership tests instead of equality tests,

```python
if cardnum in [0, 13, 26, 39]:
    face_value = 'Ace'
elif cardnum in [1, 14, 27, 40]:
    face_value = 'Two'
elif cardnum in [2, 15, 28, 41]:
    face_value = 'Three'
elif cardnum in [3, 16, 29, 42]:
    face_value = 'Four'
elif cardnum in [4, 17, 30, 43]:
    face_value = 'Five'
elif cardnum in [5, 18, 31, 44]:
    face_value = 'Six'
elif cardnum in [6, 19, 32, 45]:
    face_value = 'Seven'
elif cardnum in [7, 20, 33, 46]:
    face_value = 'Eight'
elif cardnum in [8, 21, 34, 47]:
    face_value = 'Nine'
elif cardnum in [9, 22, 35, 48]:
    face_value = 'Ten'
elif cardnum in [10, 23, 36, 49]:
    face_value = 'Jack'
elif cardnum in [11, 24, 37, 50]:
    face_value = 'Queen'
else:
    face_value = 'Kind'
```

### Solution 3

We could also do it by considering the remainder when we divide the card number by 13.

```python
face_value = cardnum % 13
if face_value == 0 :
    face_value = 'Ace'
elif face_value == 2 :
    face_value = 'Two'
elif face_value == 3 :
    face_value = 'Three'
elif face_value == 4 :
    face_value = 'Four'
elif face_value == 5 :
    face_value = 'Five'
elif face_value == 6 :
    face_value = 'Six'
elif face_value == 7 :
    face_value = 'Seven'
elif face_value == 8 :
    face_value = 'Eight'
elif face_value == 9 :
    face_value = 'Nine'
elif face_value == 10 :
    face_value = 'Ten'
elif face_value == 11 :
    face_value = 'Jack'
elif face_value == 12 :
    face_value = 'Queen'
else :
    face_value = 'King'
```

### Solution 4

A different and very compact modification to Solution 3 is to use _list lookup_ instead of `if` statements. We'll store the face values in a list, and then use the remainder of the division by 13 to access the appropriate entry in the list:

```python
FACE_VALUES = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', \
                'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

face_value = cardnum % 13
print('The face value of card number', cardnum, 'is', FACE_VALUES[face_value])
```

Study this code carefully. List lookups like this one are very convenient. They are brief and thus easier to read and understand than the lengthy `if` cascades above, and the list is easier to edit than either of the previous code-intensive approaches.

Now that we can work with individual cards let's move on to working with hands, i.e. groups of cards.

## Dealing a hand

How can we deal a hand of cards from our deck of cards?

### Solution 1

One approach is to shuffle the cards in the deck and then to deal from the top of deck using the list method `pop()`.

```python
import random

# Create the deck of cards.
deck = list(range(52))

# Shuffle the deck of cards
for swaps in range(104):
    posn1 = random.randint(0, 51)
    posn2 = random.randint(0, 51)
    # Swap the cards at posn1 and posn2
   (deck[posn1], deck[posn2]) = (deck[posn2], deck[posn1])

# Create the empty hand.
hand = []

# Deal 5 cards from the deck into the hand.
for card in range(0, 5):
    hand.append( deck.pop() )
```

(You can read about what is going on in the last line of the first `for` loop in [Tuples](15-tuples.md).)

### Solution 2

An alternative is to select cards at random from inside the deck to add to the hand.

```python
import random
deck = list(range(52))
hand = []
for card in range(5) :
    # Choose the card to deal.
    posn = random.randint(0, len(deck) - 1)
    # Append the number at that position to the hand.
    hand.append(deck[posn])
    # Delete that card from the deck.
    del(deck[posn])
```

<br>

## Putting it together

Pulling selected pieces together we can write code like this,

```python
import random

# Define handy string constants.
FACE_VALUES = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
                'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
                'Queen', 'King']
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

# Create deck of cards.
deck = list(range(52))

# Create empty hand.
hand = []

# Deal 5 cards into hand.
for deal in range(5) :
    posn = random.randint(0, len(deck) - 1)
    hand.append(deck[posn])
    del(deck[posn])

# Display the cards in the hand.
for card in hand:
    print(FACE_VALUES[card % 13], 'of', SUITS[card // 13])
```

Try it out! Then try making some changes to get a feel for how the code
works.
