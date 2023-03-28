# Functions

So far my description of modularization may seem hopelessly abstract.
What do these modules look like? In Python the simplest form of
modularization is to create functions. We have already used many of
Python's built-in functions,
e.g. `range()`, `len()`, `math.sqrt()`,
and `random.randint()`, and now it is time to learn to write our own
functions.

There is a bit of terminology that will help us talk about functions. We
say that “the function `len()` when called, returns an integer
specified by its argument”. What do the
terms _called_, _return_, and _argument_ refer to? Consider the specific
statement,

```python
mismash = [0, True, 3.8, "Don't Panic"]

print(len(mismash))
```
To _call_ a function is to invoke it and we do that by entering its name
followed by parentheses. The name of the function being used here
is `len`. To do its job it needs to find the length of a list. We tell
it which one by providing the list we need to know the length of. This value is
the _argument_ to the function. It is sometimes also called the
function _parameter_. The function `len` will calculate the length of
the list `4`. This is the value it returns or its *return value*. You
can imagine the return value replacing the function call so the code
above is equivalent to

```python
print(4)
```
So every function has,

-   a _name_
-   a _list of parameters_ enclosed in parentheses after the name of the
    function (this list may be "empty", i.e. there may be no values
    specified, but the parentheses must still be present to mark the
    name as specifying a function rather than a variable), and
-   a _return value_, the value that will replace the expression calling
    the function (this value may be `None` if the
    function _does something_ rather than _calculating something_).
