# An invisible method! (A polymorphic aside)

Our code in `playing_cards_1.py` is even runnable. Although it doesn't
do much, the output is instructive:

```plaintext
>>> 
d after shuffling = <__main__.Deck object at 0x000002C52FF39010>
d has None cards
Your hand of None cards contains: <__main__.Hand object at 0x000002C52CF18AD0>
Your hand of None cards contains: <__main__.Hand object at 0x000002C52FF67950>
There are None cards left in the deck.
>>> 
```

One thing to note is that functions without an
explicit `return` statement, like all of ours here, return the special
value `None`.

The more striking thing though is probably those inscrutable
strings `<__main__.Deck instance at 0x000002C52FF39010>` and `<__main__.Hand instance at 0x000002C52CF18AD0>`.
You can tell by where they appear that they are generated by
the `print` statements. Since print doesn't know how to
output `Deck` and `Hand` objects it tells us what it can, which is the
type and memory location of the object it has been asked to print.

We can help `print` out by providing methods that return string
representations of our `Deck` and `Hand` objects. By convention these
methods are called `__str__`. When `print` is called and passed an
object name it checks the object's class definition for
an `__str__` method and if one is defined it calls it and displays the
output the method returns. If no `__str__` method is found it displays
all it can, i.e. the object type and location as it did above.

This nicely illustrates the simple sleight of hand that lies behind
polymorphism. Until now it seemed that `print` knew how to print
everything, but in fact it knows very little and just delegates the job
to each class' `__str__` method while giving the impression that it is
masterful.
