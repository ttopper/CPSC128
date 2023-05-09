# Poker hands

We've got a hand of cards; what now? Let's suppose we are playing poker and want to know how good our hand is. In the game of Poker the value of a hand is assessed from high to low as shown at [Wikipedia](http://en.wikipedia.org/wiki/List_of_poker_hands). Let's start by seeing how we could write code to detect if our hand is a flush, i.e. that all the cards in the hand are from the same suit. Since the face values of the cards are irrelevant let's create a second list containing just the suit numbers (0 for clubs, 1 for diamonds, 2 for hearts, and 3 for spades) of the cards in our hand.

```python
suit_list = []
for card in hand:
    suit_list.append(card//13)
```

For a typical hand `suit_list` might look like `[1, 0, 3, 0, 2]` (for a hand with a diamond, a club, a spade, another diamond and a heart), but for a flush it will look like `[1, 1, 1, 1, 1]`, i.e. all the numbers will be the same.

## Solution 1

If the cards in the hand all have the same suit then the suit number of the second card is the same as the suit number of the first, and the suit number of the third card is the same as the suit number of the second, and so on. For a five card hand then we could write our test in Python like this,

```python
if suit_list[1] == suit_list[0] and suit_list[2] == suit_list[1] and \
    suit_list[3] == suit_list[2] and suit_list[4] == suit_list[3]:
    print("That's a flush!")
else:
    print("Sorry no flush here.")
```

But hands in other card games may not always have five cards so let's generalize this code to work for any number of cards in the hand. To generalize the code above to any length of hand we need to place the comparison test into a loop and arrange for the loop to compare each neighbouring pair of cards, e.g. by comparing each card to the one before it. If they are the same then we may have a flush, but if they are different then we definitely do not have a flush. So if we get all the way to the end of `suit_list` and they were always the same then it is a flush.

The way we implement that logic in Python is to use a Boolean flag variable to keep track of whether it is a flush or not. We'll start out assuming the hand is a flush and so set our flush flag variable to be `True` at the start. As we loop through the hand, if the suit of a card ever differs from that of the previous card we'll set the flag variable to be `False`. In most hands we will actually set it to `False` more than once, which doesn't matter as long as it is `False` at the end. What does matter is that we never set it to `True` inside the loop or else we may inadvertently reset it to `True` after setting it to `False` because of an earlier mismatch. Remember even one mismatch means it isn't a flush! The pseudocode for this is,

```plaintext
Set the flag variable flush to True
Starting with the second card in the hand and proceeding to the last card in the hand
    If the suit of this card is NOT the same as the suit of the previous card
        Set the flag variable flush to False
If the flag variable flush is True
    This is a flush
Otherwise
    This is NOT a flush
```

This can be implemented in Python as,

```python
flush = True # Start by assuming it is a flush.

# The first test compares the second card to the first card,
# so the initial previous card is the first card in the hand.
prev_card = suit_list[0]
for card in suit_list[1:]:
    # Note: To loop starting with the second card we use a slice of the list,
    # that begins in the second position, i.e. position #1.
    if card != prev_card: # If this card's suit is not the same as the previous one's.
        flush = False # It's not a flush.
    prev_card = card # Update previous card: This card will be the previous card
                     # next time around.
if flush:
    print("That's a flush!")
else:
    print("Sorry, no flush here.")
```

We could also implement the same pseudocode using quite different Python statements, e.g. we could loop through `suit_list` using index position, i.e. accessing each entry by its position index, and dispense with the need for the variable `prev_card`.

```python
flush = True
for posn in range(1, len(suit_list)-1):
    if suit_list[posn] != suit_list[posn-1]:
        flush = False
if flush:
    print("That's a flush!")
else:
    print("Sorry, no flush here.")
```

## Solution 2

Another approach would be to count how many cards there are of each suit. If the count is ever the same as the length of the hand then it's a flush. For example if in a 5 card hand we get 5 diamonds then it's a flush. The pseudocode for this is,

```plaintext
Count the number of clubs
If the number of clubs equals the number of cards
    It is a flush
Count the number of diamonds
If the number of diamonds equals the number of cards
    It is a flush
Count the number of hearts
If the number of hearts equals the number of cards
    It is a flush
Count the number of spades
If the number of spades equals the number of cards
    It is a flush
```

There is some obvious repetition above which we can replace with a loop to get,

```plaintext
For each suit
    Count the number of cards in that suit
        If the number equals the number of cards
            It is a flush
```

Translating this into Python gives us,

```python
flush = False
for suit in [0,1,2,3]:
    count = 0
    for card_suit in suit_list:
        if card_suit == suit:
            count = count + 1
    if count == len(suit_list):
        flush = True
if flush:
    print("That's a flush!")
else:
    print("Sorry, no flush here.")
```

## Solution 3

Yet another approach takes advantage of some of python's built-in list methods. For example the `count` method counts how often a value occurs in a list. If `suit_list` represents a flush then the first value in it should occur as many times as there are elements in the list, e.g. 5 times in a 5 card hand. This gives us the very brief,

```python
if suit_list.count(suit_list[0]) == len(suit_list):
    print("That's a flush!")
else:
    print("Sorry, no flush here.")
```

## Solution 4

Another approach that leverages Python's built-in list methods begins by noticing that in a flush the first and last values in `suit_list` are the same, e.g. [**2**, 2, 2, 2, **2**]. Of course this can be true of non-flush hands as well, e.g. [**2**, 1, 3, 0, **2**], but if we sort the non-flush hand before comparing the first and last values we will catch that, e.g. [**2**, 1, 3, 0, **2**] sorted becomes [0, 1, **2**, **2**, 3] and now the first and last values are different. We can do this in Python like this,

```python
suit_list.sort()
if suit_list[0] == suit_list[len(suit_list) - 1]:
    print("That's a flush!")
else:
    print("Sorry, no flush here.")
```

<br>

## Summary

With solutions 3 and 4 being so short why waste time on long solutions
like 1 and 2? Well not all languages provide the rich set of list
methods that Python does, so you may have to resort to approaches like
solutions 1 and 2. Also, solutions 1 and 2 showed techniques that are
useful in a wide variety of problems:

-   comparing elements of a list pairwise
-   looping from part way through a list to the end
-   looping through a list by index position
-   using flag variables
-   using counters

In short because it was good for you, and to remind you that:

> There's (almost) always more than one way to solve it!
