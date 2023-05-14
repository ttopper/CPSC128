# Built-in Type Conversions

The built-in type names can be used as functions to convert a value from
one type to another. What happens is that the type name triggers the
specified type's constructor to build a new object from the given
existing one.

```plaintext
  >>> int(4.5) # Build an int from the floating point value 4.5
  4
  >>> float(4) # Build a floating point value from the integer value 4
  4.0
  >>> str(4) # Build a string from the integer 4
  '4'
  >>> int('4') # Build an integer from the string '4'
  4
  >>> float("4") # Build a floating point value from the string "4"
  4.0
  >>> list("Tim") # Build a list from the string "Tim"
  ['T', 'i', 'm']
  >>> str(['no','more']) # Build a string from a list of strings.
  "['no', 'more']"
  >>> # ^But you just get the printable representation of the list.
  >>> list(4) # Build a list from the integer 4.
  Traceback (most recent call last):
File "<pyshell#68>", line 1, in -toplevel-
  list(4)
  TypeError: iteration over non-sequence
  >>> # ^But it can't be done.
```
Note that some conversions are not helpful (in the second last case the
programmer probably wanted to concatenate the two strings and so should
have used the string method `join`), and others are not possible (as in
the last example of trying to build a `list` from an `int`).
