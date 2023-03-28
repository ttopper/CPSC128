# Example: dice_roll()

Now suppose we wish to write a function that rolls a die for us. We
would like to be able to write code like this,

```python
total = dice_roll() + dice_roll()
```
to simulate rolling a pair of dice. What can we tell by looking at this
code?

-   the name of our function will be `dice_roll`
-   it takes no arguments (because there is nothing inside the brackets)
-   it returns something that can be added together and stored (so
    not `None`).

This leads to the code,

```python
def dice_roll():
    return random.randint(1,6)
```
which we could use like this,

```python
import random

def dice_roll():
    return random.randint(1,6)

total = dice_roll() + dice_roll()
print("On your first roll you got:", total)
```

This code works, but could be improved by being generalized to dice with
other than six sides like these (with 4, 6, 8, 12, 20 and 10 sides
respectively),

![](06_DnD_Dice_Set.jpg)

We can do that by having our function take an argument specifying the
number of sides,

```python
import random

def dice_roll(sides):
    return random.randint(1,sides)

total = dice_roll(6) + dice_roll(6)
print("On your first roll you got:", total)
```