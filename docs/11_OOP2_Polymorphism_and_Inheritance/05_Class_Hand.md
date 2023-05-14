# `class Hand`

The code for the Hand class may surprise you:

```python
class Hand(CardCollection):
    pass    
```

It is so short because `Hand` objects do not have any extra methods
that `CardCollection`s do not, nor do they need to customize
any `CardCollection` methods. In fact with the code above `Hand` is
effectively an alias for `CardCollection`.
