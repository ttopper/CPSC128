# A subtle point: Semantics

If it looks too easy so far, that's because it isn't quite this easy.
What we have at the moment looks like it works only because we have not
investigated what it has done closely enough. Let's add a few more
`print` statements and rerun that last program.

Code:

```python
print('Before:')
roxx = Hand()
roxx = roxx + Card(42) + Card(13) + Card(2)
print('roxx:', roxx)
chris = Hand()
chris = chris + Card(3) + Card(4)
print('chris:', chris)
print('After:')
new = roxx + chris
print('new:', new)
print('roxx:', roxx)
print('chris:', chris)
```

Output:

```plaintext
>>>
Before:
roxx: 4 of Spades, A of Diamonds, 3 of Clubs
chris: 4 of Clubs, 5 of Clubs
After:
new: 4 of Spades, A of Diamonds, 3 of Clubs, 4 of Clubs, 5 of Clubs
roxx: 4 of Spades, A of Diamonds, 3 of Clubs, 4 of Clubs, 5 of Clubs
chris: 4 of Clubs, 5 of Clubs
>>> 
```

Uh oh! The value of `roxx` is changed by what we've done in
creating `new` which may or may not be the _semantics_ we intended by
the statement `new = roxx + chris`. The problem here is that we are
building our return value from an existing object so we are changing the
existing object as we do so, and then ending up with a shared reference
to a single modified object. And we know from our first encounter with
shared references that they can be a serious problem. The fix is to
create a new `CardCollection` object in `__add__`, fill _it_ with the
necessary values, and then return it. The result is code like this,

```python
def __add__(self, other):
    # Create a new CardCollection.
    new_cc = CardCollection()
    # Put a copy of self's cards into it.
    new_cc.cards = self.cards[:]
    if isinstance(other, Card):
        new_cc.cards.append(other)
        return new_cc
    elif isinstance(other, CardCollection):
        new_cc.cards.extend(other.cards[:])
        return new_cc
    else:
        print('You can only add Cards to CardCollections!')
```

which produces the output,

```plaintext
Before:
roxx: 4 of Spades, A of Diamonds, 3 of Clubs
chris: 4 of Clubs, 5 of Clubs
After:
new: 4 of Spades, A of Diamonds, 3 of Clubs, 4 of Clubs, 5 of Clubs
roxx: 4 of Spades, A of Diamonds, 3 of Clubs
chris: 4 of Clubs, 5 of Clubs
>>> 
```

There are further _semantic_ issues. When we write `new = roxx + chris`,
to create a new `Hand` from `roxx` and `chris`,
should `roxx` and `chris` be emptied? That is, are we taking the cards
out of the hands `roxx` and `chris` to create `new` like a game of Go
Fish? Or does `new = roxx + chris` mean to make a hand called `new` that
is _like_ the combination of `new = roxx + chris`? Sorting out
the _meaning_ of operations is semantics, and the semantics of
collection types is notoriously tricky. There aren't universally right
and wrong answers to these questions. What we strive for are answers
that fit the problem domain, i.e. code that matches our experience of
the real-world situation we are modelling.
