# `class Deck`

Now we define our `Deck` and `Hand` classes by inheriting from
this `CardCollection` base class. The mechanism to show inheritance in
Python is simply to include the base class name in parentheses after the
derived class name,

     1 class Deck(CardCollection):
     2     # Override ancestor's constructor, i.e. replace the default.
     3     def __init__(self):
     4         self.cards = []
     5         for cardnum in range(52):
     6             self.add( Card(cardnum) )
     7
     8     # Alias the inherited method "size" as "cards_left",
     9     # because we usually ask how many cards are left in a
    10     # deck rather than asking about its size.
    11     def cards_left(self):
    12         return self.size()
    13 
    14     # Another alias. When using a deck of cards we talk about "dealing"
    15     # cards not "removing" them from the deck.
    16     def deal(self):
    17         return self.remove()
    18
    19     # Add a new method, shuffle, that does not exist in ancestor class.
    20     def shuffle(self):
    21         for i in range(  2*self.size() ):
    22             self.cards.insert(random.randrange(len(self.cards)), self.cards.pop())

This example shows most of what you can do with inheritance:

→ line 1
:   The syntax to define a class `Deck` that inherits from the
    class `CardCollection`. Jargon: Deck is
    the *derived* or *descendant* class; `CardCollection` is the *base
    class*, *superclass* or *ancestor class*.

→ lines 3-6

:   Replace a method from the base class with a customized version. This
    is just done by redefining the method, i.e. if you use the same name
    in the derived class it hides the version in the base class. The
    jargon for this is *specialization* because we specialize the
    operation of the method for our derived class' characteristics.

→ lines 11-12

:   We provide an "alias", i.e. a more meaningful name, for a method
    in the base class. In this case we can refer
    to `cards_left()` instead of `size()`. Note that this
    is *not* a **re**naming; it is providing a *second name*. We can
    still access the method `size()` if we wish.

→ lines 16-17

:   Another alias, this time allowing us to refer to the
    method `remove` by the name `deal`.

→ lines 20-22

:   We can add new methods in the derived class that do not exist in the
    base class. In this case we add a `shuffle` method to our derived
    class. Note that inheritance is one way: we cannot call
    the `shuffle` method on a `CardCollection` object only on
    a `Deck` object. The jargon for this is *augmentation* since we are
    augmenting the functionality of our base class.
