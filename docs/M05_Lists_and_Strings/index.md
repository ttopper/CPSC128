# Introduction: Lists and strings 🧵 

Finally something other than numbers!

So far all of your programs have had a mathematical, or at least arithmetic, feel to them. That's because the main data type we've had to work with has been numbers, and single numbers at that. This week we will look at compound datatypes that let us represent words and lists of things. Together they vastly expand the types of things we can represent, and thus work with, in our programs. We will work with code like,

```python
grades = [78, 91, 84] # a list containing three numbers
name = 'Tim Topper' # a string, which is a sequence of characters
names = ['Tim', 'Anne', 'Mary', 'Geoff'] # a list containing 4 strings
```

We cover lists and strings in the same week because they are both _sequence_ types that share a lot of common operations.

Lists and strings are also both _object_ types and to work with them you will have to get comfortable with some new-ish notation, and a bit of jargon that goes with it. The notation isn't that hard to follow, for example,

```plaintext
>>> s = 'Topper'
>>> s.count('p')
2
>>> s.endswith('er')
True
>>> s.upper()
'TOPPER'
>>>
```
This notation features the name of an object `s`, a period `.`, the method to perform `count`, and then any information the method requires in parentheses `('p')`: `s.count('p')`. (This notation is not entirely new, e,g, we have seen and used `random.randint(1,6)`.)

The list and string object types support **a lot** of methods. Some are shown in the resources and the complete lists of them in the official Python documentation are linked to. To prepare for the assignment problems you will want to familiarize yourself with the operations available to you (so you don't reinvent the wheel!), and get a little practice using them in the Python shell, like the excerpt above.

I hope you find lists and strings interesting!

1. [Object-based
    programming](01-object-based-programming.md)
1. [Sequence Types](02-sequence-types.md)
1. [What can you do with a
    list?](03-what-can-you-do-with-a-list.md)
1. [What can you do with a
    string?](04-what-can-you-do-with-a-string.md)
1. [Example: CD
    Shuffle](05-example-cd-shuffle.md)
1. [Dice Odds](06-dice-odds.md)
1. [Bar Graphs](07-bar-graphs.md)
1. [Representing Playing
    Cards](08-representing-playing-cards.md)
1. [Poker hands](09-poker-hands.md)
1. [Playing Cards: An alternative
    representation](10-playing-cards-an-alternative-representation.md)
1. [What is this \[ \[ 'X', 'O', '' \], \[ 'O', 'X', 'O'
    \], \[ '', '', 'X'\] \]
    ?](11-what-is-this-x-o-o-x-o-x.md)
1. [Palindrome](12-palindrome.md)
1. [Built-in Type
    Conversions](13-built-in-type-conversions.md)
1. [The map()
    function](14-the-map-function.md)
1. [Tuples](15-tuples.md)
1. [Exercise sheet 5](70_Exercise_Sheet_5.md)
1. [Assignment 5](90_Assignment_5.md)