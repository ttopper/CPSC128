# Example: Fractions

Suppose we are working on a suite of programs for carpenters who want to
work with fractions, e.g 3/4 of an inch, 5/16 of an inch and so on. Not
surprisingly our design of this suite calls for a
`Fraction` class. Of course with one eye on the future we
don't want to just handle the fractions common in carpentry we want a
general `Fraction` class we will be able to reuse in many
settings. We'd like to be able to do things like this,

```python
    >>> d1 = Fraction(2,5)
    >>> print(d1)
    2/5
    >>> d2 = Fraction(4)
    >>> print(d2)
    4/1
    >>> d3 = d1 + d2
    >>> print(d3)
    22/5
    >>> if d1 <= d2:
            print('d1 is less than or equal to d2')
    else:
            print('d2 is greater than d1')
    d2 is greater than d1
    >>> print(d1[0], d1[1])
    2 5
    >>> print(d1 + 2)
    12/5
    >>> print(d1 - 2)
    -8/5
    >>>
```