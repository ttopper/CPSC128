# List comprehensions

List comprehensions are not understandings of lists, but a shortcut notation for generating one list from another. The shortcut notation was created because we process a list to create another so often. Consider creating a list of playing card face values from a list of their card numbers. We could do it like this,

```
hand = [12, 42, 8, 29, 11]
face_values = []
for card in hand:
    face_values.append( card%13 )
```

Or we could use the shortcut notation provided by list comprehensions and do this,

```
face_values = [card%13 for card in hand]
```

(The square parentheses are a reminder that the expression on the right is creating a list.)

A list comprehension is a general expression mechanism that generates lists instead of numbers or strings, e.g.

```
[x**2 for x in range(5)]
```

will generate,

```
>>> [x**2 for x in range(5)]
[0, 1, 4, 9, 16]
>>>
```

You can even add a test at the end to filter out some of the results, e.g.

```
>>> [x**2 for x in range(5) if x**2 % 2 == 0]
[0, 4, 16]
>>>
```

<br>

## Syntax summary

[ _expression_ **for** _name_ **in** _sequence_ **if** _test_ ]
