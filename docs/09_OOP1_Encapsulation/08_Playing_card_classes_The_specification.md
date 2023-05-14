# Playing Card Classes: The Specification

Earlier we developed a series of functions to help write programs
involving playing cards. Now we'll take the next step and make our code
object-oriented. How shall we go about designing the class(es)? There
are many possible answers to this question, but for a smallish domain
like this one a good approach is _wish fulfillment_. That is, we specify
the kind of code we wish we could write but can't. In this case I wish
I could say things like,

```plaintext
Get a deck of cards
Shuffle the deck
Display the deck
Create a hand of cards for roxx
Create a hand of cards for chris
Deal five cards to roxx
Display roxx's cards
Deal five cards to chris
Display chris' cards
How many cards are left in the deck?
If roxx has a flush
    congratulate him
```

Using OOP our Python code can be almost that easy to read,

```python
d = Deck()
d.shuffle()
print('d after shuffling =', d)
print('d has', d.cards_left(), 'cards')
roxx = Hand()
chris = Hand()
for card in range(5):
    roxx.add(d.deal())
print('Your hand of', roxx.size(), 'cards contains:', roxx)
chris.add(d.deal(5))
print('Your hand of', chris.size(), 'cards contains:', chris)
print('There are', d.cards_left(), 'cards left in the deck.')
if roxx.is_flush():
    print('roxx rocks!')
```

This code will serve as our specification. We'll know we're done when
we've added sufficient code above this that it runs correctly.
