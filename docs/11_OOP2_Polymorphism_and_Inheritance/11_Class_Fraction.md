# class Fraction

The code needed to implement a class Fraction that can produce the shell
session shown earlier is,

```python
class Fraction:
    def __init__(self, n, d = 1):
        self.num = n # numerator
        self.den = d # denominator
        
    def __str__(self):
        return str(self.num) + '/' + str(self.den)
    
    def __add__(self, other):
        if isinstance(other, Fraction):
            bottom = self.den * other.den
            top = (self.num * other.den) + (other.num * self.den)
            return Fraction(top, bottom)
        elif isinstance(other, int):
            other = Fraction(other)
            bottom = self.den * other.den
            top = (self.num * other.den) + (other.num * self.den)
            return Fraction(top, bottom)
        
    def __le__(self, other):
        pass
    
    def __getitem__(self, key):
        if key == 0:
            return self.num
        elif key == 1:
            return self.den
        
    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        if isinstance(other, Fraction):
            bottom = self.den * other.den
            top = (self.num * other.den) - (other.num * self.den)
            return Fraction(top, bottom)
        
if __name__ == '__main__':
    d1 = Fraction(2, 5)
    print(d1, '(s/b 2/5)')
    d2 = Fraction(4)
    print(d2, '(s/b 4/1)')
    d3 = d1 + d2
    print(d3, '(s/b 22/5)')
    if d1 <= d2:
        print(d1, 'is less than or equal', d2)
    else:
        print(d2, 'is greater than', d1)
    print(d1[0], d1[1], '(s/b 2 5)')
    print(d1 + 2, '(s/b 12/5)')
    print(d1 - 2, '(s/b -8/5)')
```

The output when this module is run is (note that s/b is a short form for
"should be")

```plaintext
>>> 
2/5 (s/b 2/5)
4/1 (s/b 4/1)
22/5 (s/b 22/5)
2/5 is less than or equal 4/1
2 5 (s/b 2 5)
12/5 (s/b 12/5)
-8/5 (s/b -8/5)
>>> 
```

Notes:

-   Notice that `__str__` uses the `str()` method to change the
    numerical values of `num` and `den` to strings since it has to
    return a string in the end.
-   `__add__` has to check the type of the thing being added to it
    (using `isinstance`) to decide how to behave (more polymorphism!)
    In `__add__` I used a clear structure which converts `other` from
    an `int` to a `Fraction` when necessary, but it can be done more
    briefly as demonstrated in `__sub__`.
-   `__getitem__` is the special method called when the interpreter
    encounters `[]`s, i.e. when it encounters the
    expression `obj[key]` it calls `obj.__getitem__(key)`.

That is not very much code to add a new datatype to a language and bring
it toward first-class status!
