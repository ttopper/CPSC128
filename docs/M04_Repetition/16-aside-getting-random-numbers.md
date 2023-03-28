# Aside: Getting "random" numbers

If you thought for a moment after reading the game description you might have wondered how the computer was going to pick the number to be guessed. The answer is that the computer needs some random or pseudorandom method for choosing that number. I say pseudorandom because computers are not random machines, they are deterministic machines so they can't generate something truly random unless they get access to the output of some random physical process. They can however generate numbers that seem unpredictable and so appear random even though they are being generated programmatically. Python makes this easy by providing a module we can `import` that hides the messy details, e.g.

```python
import random
print(random.randint(1,100))
```

The module is named `random` and one of its members is `randint` which returns a random number in the specified range.

_Exercise_: Try entering the lines above into a program file and running it several times. Most times you will get new numbers. ('Most' because since it is random you may get the same number twice in a row, but since there are 100 possibilities that is unlikely.)

_Exercise_: Does `randint` generate numbers **between** 1 and 100 or from 1 to 100 **including** 1 and 100? You can find out either by looking it up, or by writing a very small program and watching its output.

_Jargon_: If the range includes the endpoints, e.g. 1 and 100 above, we say it is an _inclusive_ range. If it doesn't, we say it is an _exclusive_ range.
