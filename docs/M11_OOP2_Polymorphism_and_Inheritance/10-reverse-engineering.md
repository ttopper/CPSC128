# Reverse engineering

You can figure out a lot about a class given an example of its use. From
the sample output of using our imagined `Fraction` class we can tell
that:

```python
    >>> d1 = Fraction(2,5)
    >>> print(d1)
    2/5
```

→ It will have a constructor that takes two arguments, the first one
    the numerator, the second the denominator.
    
```python
    >>> print(d1)
```
→ It defines a `__str__` method for display.
    

```python
    >>> d2 = Fraction(4)`
    4/1
```

→ The constructor can handle getting a single number. It does so by
    using it as the numerator and 1 as the denominator of
    the `Fraction` it constructs.
    

```python
    >>> d3 = d1 + d2
```

→ It defines the `__add__` function.
    

```python
    >>> if d1 <= d2:
```

→ It defines the `__le__` method.

```python
    >>> print(d1[0], d1[1])
```

→ It defines the `__getitem__` method.

```python
    >>> print(d1 + 2)
```

→ Its `__add__` method works when the second argument is an integer
    and not another `Fraction`.

```python
    >>> print(d1 - 2)
```

→ It defines `__sub__` and like `__add__`, `__sub__` works with
    integer values as well as Fraction values.
