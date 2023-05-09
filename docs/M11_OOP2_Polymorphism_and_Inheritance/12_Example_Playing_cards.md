# Example: Playing cards

Our first example of polymorphism dealt with `Fraction`s, an immutable
type like other numbers and strings. There are some subtle issues that
arise when dealing with mutable objects like container types. Our card
classes provide a familiar container type for us to work with.

Let's say we would like to be able to use a plus sign, `+`, to add
cards to a `CardCollection` object. Specifically we want to enable code
like this to work,

```python
        cc = CardCollection()
        card = Card(42)
        cc = cc + card
```

Here's what it would take to be able to use a plus sign in this way,

```python
    class CardCollection:
        ...
        def __add__(self, other):
            self.cards.append(other)
            return self
```

All we need to do is append the card to the cards in
the `CardCollection` and return the `CardCollection` object. Why do we
have to return the whole object? For that matter why do we have to
return anything? Remember what the assignment operation is doing. It
evaluates the expression on the right hand side (RHS), `cc + card`, and
assigns the result of the expression to the name on the left hand
side, `cc`. But the RHS operation just calls the function `__add__` so
the result of the expression will be the value returned by `__add__`.
If `__add__` doesn't return a value then the value assigned
to `cc` will be `None` — we will have deleted our list! That's why we
have to be careful to return the modified object.

Notice that thanks to inheritance we can use the plus sign operator
on `Hand`s and `Deck`s too without writing any new code at all. Score
one for inheritance!

```python
        roxx = Hand()
        roxx = roxx + Card(42)
        roxx = roxx + Card(18)
        print(roxx)
```

will produce the output,

```plaintext
    >>>
    4 of Spades, 6 of Diamonds
    >>>
```

Python's internals are well enough designed that we can
chain `+` operations without having to write any additional code, e.g.

```python
        roxx = Hand()
        roxx = roxx + Card(42) + Card(13) + Card(2)
        print(roxx)
```

produces the output,

```plaintext
    >>>
    4 of Spades, A of Diamonds, 3 of Clubs
    >>> 
```

This is nice, very nice in fact, but the built-in `+` operator does more
than this when used with the built-in types. It can add two integers,
but it can also add an integer and a float. So far we are adding
a `Card` to a `CardCollection`, but what if we also wanted to be able to
add two `CardCollection`s together? We would have to modify our code to
detect the type of object it is being asked to add (just like we did
with `__add__` for `Fraction`s previously).

```python
        def __add__(self, other):
            if isinstance(other, Card):
                self.cards.append(other)
                return self
            elif isinstance(other, CardCollection):
                self.cards.extend(other.cards)
                return self
            else:
                print('You can only add Cards or other CardCollections to CardCollections!')
```

With this version we can now write code like this,

```python
        roxx = Hand()
        roxx = roxx + Card(42) + Card(13) + Card(2)
        print('roxx:', roxx)
        chris = Hand()
        chris = chris + Card(3) + Card(4)
        print('chris:', chris)
        new = roxx + chris
        print('new:', new)
```

which produces as output,

```plaintext
    >>>
    roxx: 4 of Spades, A of Diamonds, 3 of Clubs
    chris: 4 of Clubs, 5 of Clubs
    new: 4 of Spades, A of Diamonds, 3 of Clubs, 4 of Clubs, 5 of Clubs
    >>> 
```