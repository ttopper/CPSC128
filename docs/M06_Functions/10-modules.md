# Modules

Any Python program is a module and other programs can use the functions and variables in it (and classes too etc.), but for its contents to be reused easily there are some standard practices to follow. We'll work with our previous program containing the playing card functions and now named `playing_cards.py`,

```
# playing_cards.py
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

Now suppose that in our new Blackjack program we have a hand of card numbers and would like to display the cards in the hand. We write code like this,

```
# blackjack.py
...
print('You are holding,')
for card in hand:
    print('The', label(card))
...
```

in hopes of generating output like this,

```
You are holding,
The Three of Diamonds
The Four of Spades
The Nine of Clubs
```

## A first try

One program accesses another program's functions by importing the program, so to be able to use `label` we need to import `playing_cards.py`. To access the functions in `playing_cards.py` we preface the function name with the module name separated by a dot (.). We need to do this because modules are objects (like lists and strings) and the definitions inside them are their attributes. So `label`'s full name will be its module name, `playing_cards`, followed by its function name, `label` (just like we have done with `math.sqrt` or `random.randint`, think of it as a _lastname.firstname_ system for now),

```
# blackjack.py
import playing_cards

hand = [15, 42, 8]
print('You are holding,')
for card in hand:
    print('The', playing_cards.label(card))
```

Note that when importing a module we omit the .py suffix, as we do when we refer to the module within the program, i.e. `import playing_cards` instead of `import playing_cards.py` and `playing_cards.label`, instead of `playing_cards.py.label`.

## A problem

This almost works but the output isn't quite what we wanted,

```
>>>
Card 15 is the Three of Diamonds
Card 15 is the Three of Diamonds
You are holding,
The Three of Diamonds
The Four of Spades
The Nine of Clubs
>>>
```

We have the output we want, but above it we have extraneous output from `playing_cards.py`. The reason we get the undesired output is that modules are _run upon import_, i.e. when you import a module the first thing Python does is to run it. It runs it becuse this interprets the code in the module making the definitions in the file available to the current program.

One fix to eliminate the undesired otuput would be to delete the `print` statements from `playing_cards.py`. But this is a ugly fix not an elegant solution. Those `print` statements in `playing_cards.py` may be serving a purpose. In fact standard practice is to include code in all modules to test the functions in the module (these are called unit tests). The last thing we want to do is remove code that tests our module to verify that it works.

## A solution

Fortunately Python can tell if a program is running on its own or being
imported. When it is running on its own, it is assigned the
name `__main__`. The double underscores are another Python standard
practice: they signal that this is an internal Python name. You should
never give a variable of your own a name beginning with double
underscores. When it is imported on the other hand it is assigned a name
based on its file name less the .py suffix. So when we
execute `playing_cards.py` on its own its name is `__main__`, but when
we import it it's name is `playing_cards`. Watch. If I add a statement
too display the module's `__name__` attribute (look for it on line 16)

    # playing_cards.pySUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    FACE_VALUES = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
                   'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
                   'Queen', 'King')

    def suit(cardnum):
        return SUITS[cardnum // 13]

    def face_value(cardnum):
        return FACE_VALUES[cardnum % 13]

    def label(cardnum):
        return face_value(cardnum) + " of " + suit(cardnum)

    print('My name is', __name__) # Line 16!
    card = 15
    print("Card", card, "is the", face_value(card), "of", suit(card))
    print("Card", card, "is the", label(card))

when I run `playing_cards.py` it displays,

    >>> 
    My name is __main__
    Card 15 is the Three of Diamonds
    Card 15 is the Three of Diamonds

but when I run `blackjack.py` look what it says its name is,

    >>> 
    My name is playing_cards
    Card 15 is the Three of Diamonds
    Card 15 is the Three of Diamonds
    You are holding,
    The Three of Diamonds
    The Four of Spades
    The Nine of Clubs

I know this has been a long explanation, but it points us to a simple
solution. We will introduce an if test into `playing_cards.py` that will
see what its current name is. If it is `__main__` it will run the tests
and otherwise it will not. This way the tests will not be run when the
file is imported, but are still available by running the module on its
own. Our modified `playing_cards.py` will look like this,

    # playing_cards.py
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

    if __name__ == '__main__':
        card = 15
        print("Card", card, "is the", face_value(card), "of", suit(card))
        print("Card", card, "is the", label(card))
     
