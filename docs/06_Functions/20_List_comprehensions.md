# List comprehensions

List comprehensions are not understandings of lists, but a shortcut notation for generating one list from another. The shortcut notation was created because we process a list to create another so often. Consider creating a list of playing card face values from a list of their card numbers. We could do it like this,

```python
hand = [12, 42, 8, 29, 11]
face_values = []
for card in hand:
face_values.append( card%13 )
```

Or we could use the shortcut notation provided by list comprehensions and do this,

```python
face_values = [card%13 for card in hand]
```

(The square parentheses are a reminder that the expression on the right is creating a list.)

A list comprehension is a general expression mechanism that generates lists instead of numbers or strings, e.g.

```python
[x**2 for x in range(5)]
```

will generate,

```plaintext
>>> [x**2 for x in range(5)]
[0, 1, 4, 9, 16]
>>>
```

You can even add a test at the end to filter out some of the results, e.g.

```plaintext
>>> [x**2 for x in range(5) if x**2 % 2 == 0]
[0, 4, 16]
>>>
```

## Syntax summary

<pre>[ <i>expression</i> <b>for</b> <i>name</i> <b>in</b> <i>sequence</i> <b>if</b> <i>test</i> ]</pre>
