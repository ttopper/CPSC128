# Refining import

We saw in `playing_cards.py` that we had to refer to `label` by its full name `playing_cards.label`. This is not what we originally wanted. The original desire was to be able to write,

```python
# blackjack.py
...
print('You are holding,')
for card in hand:
print('The', label(card))
...
```

Python allows us to do this using variations in `import` syntax. If we only want to `import` the function `label` from the module `playing_cards.py` and to refer to it by its 'first name' alone, i.e. as `label`, we can write

```python
from playing_cards import label
...
print('You are holding,')
for card in hand:
print('The', label(card).)
...
```

If you want to `import` all the functions in `playing_cards` and refer to them just by their “first names” you can use,

```python
from playing_cards import *
...
print('You are holding,')
for card in hand:
print('The', label(card))
...
```

You can even rename a function as you `import` it. If you want to import `label` but refer to it as `card_name` you can use,

```python
from playing_cards import label as card_name
...
print('You are holding,')
for card in hand:
print('The', card_name(card))
...
```

## A warning!

There is a danger of making a habit of importing functions and referring
to them by first name as in the first two examples above. If multiple
modules have functions by the same name, e.g. you import two modules
both of which have a function named `label`, the second import
of `label` will redefine the function and you will only have access to
that version. Like all conveniences there is a cost!
