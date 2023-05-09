# Tuples

In [Representing Playing Cards](08_Representing_playing_cards.md) there was the unfamiliar line,

```python
(deck[posn1], deck[posn2]) = (deck[posn2], deck[posn1])
```

The items on each side of the equals sign are _tuples_. You know you are looking at a tuple because of the round parentheses , i.e. `()`, surrounding it[^*]. Tuples are a bit of an odd duck data type. They work much like lists, except that they are immutable, i.e. they can't be changed (which means that many list methods can't be applied to them). What use is a list you can't change? Not very much generally, but there are some special cases where that combination of properties is just the ticket. This is one of them, so let's get back to that code. What is this code

```python
(deck[posn1], deck[posn2]) = (deck[posn2], deck[posn1])
```

doing? It is swapping the values of `deck[posn1]` and `deck[posn2]`. A simpler example would be,

```plaintext
>>> a = 5 # set the value of a
>>> b = 1 # set the value of b
>>> (a,b) = (b,a) # swap the values of a and b
>>> print(a)
1
>>> print(b)
5
>>>
```

Here a tuple is created on the right side and unpacked into the target tuple on the left hand side. The statement says, reading it left to right, assign the names `a` and `b` the values named by `b` and `a`. The magic of tuple packing and unpacking makes this seem to happen in parallel so no values get overwritten before their time. The net effect is to swap the names on the values 5 and 1.

Now you should be able to look at the earlier deck code and see what it is doing.

## Swapping in other languages

Tuples are a Python oddity. In most other languages you swap variables
using a temporary variable. To do the second swap above you would do
something like,

```plaintext
a = 5
b = 1
...
temp = a
a = b
b = temp
```
---

[^*]: Language lawyers will point out that the tuple constructor is the
comma, not the parentheses and they'd be right, but standard practice
is to surround tuples with a more visible marker like ()s, which I will
do, and so will you!


