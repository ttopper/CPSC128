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
    programming](01_Object_based_programming.md)
1. [Sequence Types](02_Sequence_types.md)
1. [What can you do with a
    list?](03_What_can_you_do_with_a_list.md)
1. [What can you do with a
    string?](04_What_can_you_do_with_a_string.md)
1. [Example: CD
    Shuffle](05_Example_cd_shuffle.md)
1. [Dice Odds](06_Dice_odds.md)
1. [Bar Graphs](07_Bar_graphs.md)
1. [Representing Playing
    Cards](08_Representing_playing_cards.md)
1. [Poker hands](09_Poker_hands.md)
1. [Playing Cards: An alternative
    representation](10_Playing_cards_An_alternative_representation.md)
1. [What is this \[ \[ 'X', 'O', '' \], \[ 'O', 'X', 'O'
    \], \[ '', '', 'X'\] \]
    ?](11_What_is_this_x_o_o_x_o_x.md)
1. [Palindrome](12_Palindrome.md)
1. [Built-in Type
    Conversions](13_Built_in_type_conversions.md)
1. [The map()
    function](14_The_map_function.md)
1. [Tuples](15_Tuples.md)
1. [Exercise 4](70_Exercise_sheet_4.md)
1. [Assignment 5](90_Assignment_5.md)