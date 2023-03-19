# Inheritance example: Playing Cards

Think back to our earlier `Deck` and `Hand` playing card classes. While
there are obvious differences between decks of cards and hands of cards
there are also similarities. Let's focus on the similarities for a
moment.

-   Both of them are collections of the same kind of object, i.e.
    playing cards.
-   Both need to be displayed, and in quite similar ways.
-   At times we remove cards from both of them, and
-   at other times we add cards to them.
-   Finally we can ask how many cards are in each of them.

OOP recommends that we remove this common functionality from
both `Deck` and `Hand` to a separate base class and have
our `Deck` and `Hand` classes inherit this functionality from it. This
way if we need to modify some part of it, e.g. the card list
representation, we get to do it in a single place and the changes will
be automatically propagated to the descendant classes. It's a small win
in a shallow hierarchy like this one, but it's a huge win when the
hierarchy is deep because then we get to make a change in one place
rather than dozens. Here's how this is done in Python.
