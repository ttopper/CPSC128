# Scope

*This is a somewhat technical issue I wish we could delay. But you're going to bump into it at some point, and we'd better see it before you do. If it doesn't make perfect sense on first reading make a mental note of it, and come back to it when you suspect you are bumping into it hard.*

Look again at our card functions,

```python
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

We saw earlier that names passed into functions get assigned aliases. For example the object `15` is referred to by the name `card` outside the function above, and by the name `cardnum` inside the function. The function `suit` “knows” about `cardnum` because it assigns the name in its definition statement. But, how does it know about `SUITS`? `SUITS` exists outside the function, and isn't aliased in it, so how does `suit` know what it is?

## LEGB

The answer is that Python functions follow a clear process in trying to _resolve names_. This process is easy to remember using the mnemonic LEGB.

1. The letters remind us that Python first looks in the **Local** context, i.e. the current function.
2. Then it looks in any **Enclosing** functions, i.e. functions that contain the current one. (See `inner()` below for an example of this.)
3. Then it looks in the **Global** context, i.e. the module.
4. Finally it checks the **Built-in** names for a match.

In going through this list Python stops as soon as it finds a match, i.e. if it finds the name defined in the current function it stops looking. So in our code above it finds `cardnum` defined in the local function. When it looks for `SUITS` it doesn't find it defined in the function, and then doesn't find an enclosing function, so it looks in the module above the function, and finds it there. If it hadn't, it would have checked to see if there is a built-in variable called `SUITS`.

## Beware!

One way scope can trick new programmers is that local definitions hide
global ones which in turn can hide built-in values and functions. Work
through the following examples carefully noting the output. Sooner or
later one of these will happen to you.

```python
# scope_egs.py
print('Example 1: Local variable')
def f():
    x = 1
    print('Inside x is', x)
f()
print('Outside x is', x) # Error! Comment this line out once you understand why it is an error.
print()

print('Example 2: Global variable')
x = 1
def f():
    print('Inside x is', x)
f()
print('Outside x is', x)
print()

print('Example 3: Local variable hides global variable inside function')
x = 1
def f():
    x = 2
    print('Inside x is', 2)
f()
print('Outside x is', x)
print()

print('Example 4: Lots of hiding')
x = 1
def outer():
    x = 2
    def inner():
        x = 3
        print('Here in inner x is', x)
inner()
print('Here in outer x is', x)
inner() # Error! Comment this line out once you understand why it is an error.
outer()
print('Out here x is', x)

print('Example 5: Hiding the built-in len')
def len():
    print('I am not the real len')
len()
```