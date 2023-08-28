# Documenting modules and functions

The goal of documentation is to provide enough information for other programmers (or ourselves in six months!) to know how to use our code (that is to run a program, or import and use its components), and to understand it well enough to verify it and/or modify it.

So far our documentation has consisted of a block of header comments identifying the module and programmer, and occasional comments inserted into the code to explain tricky points. Modules and the functions in them require further documentation. The primary mechanism used to provide it is docstrings. These are triple quoted strings that appear at the top of the module and immediately after each function definition. Here's an artificial example,

```python
# module_docn.py
'''This is the module documentation pointing out that
this is an artificial test module.'''

def test_fn_1():
    '''This is the first test function.
    It doesn't do anything.'''
    return

def test_fn_2():
    '''This is the second test function which also does nothing.'''
    return
```

In an actual module these docstrings would be helpful to a programmer reading your code by explaining what the module and each function in it were designed to do. You can see lots of real examples in the [standard library modules](https://docs.python.org/3/py-modindex.html).

Python also has built-in commands that extract this documentation. Recall that when we import a module in the shell we can use `dir` to see it's attributes. Here's an example for a real module, `math`,

```plaintext
>>> import math
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__',
'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh',
'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees',
'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'exp1', 'fabs',
'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma','gcd',
'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt',
'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2',
'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod',
'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh',
'tau', 'trunc', 'ulp']
>>>
```

and here's the `dir` for our artificial module,

```plaintext
>>> import module_docn
>>> dir(module_docn)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
'__name__', '__package__', '__spec__', 'test_fn_1', 'test_fn_2']
>>>
```

You can see that in addition to the Python reserved names, i.e. `__builtins__` to `__package__` there are our two functions `test_fn_1` and `test_fn_2`. We've already seen that the reserved name `__name__` gives the current name of this module which will be `module_docn` if it has been imported or `__main__` if it is running. Now let's see what `__doc__` is,

```plaintext
>>> print(module_docn.__doc__)
This is the module documentation pointing out that
this is an artificial test module.
>>>
```

`module_docn.__doc__` contains the module docstring. And now you may see why they are called docstrings: because they are the _strings_ that get assigned to the `__doc__` attributes. The docstrings for `tst_fn_1` and `test_fn_2` are also available in their `__doc__` attributes,

```plaintext
>>> print(module_docn.test_fn_1.__doc__)
This is the first test function.
It doesn't do anything.
>>> print(module_docn.test_fn_2.__doc__)
This is the second test function.
It also doesn't do anything.
>>>
```

The docstrings are so useful but this is such a cumbersome way to access them that Python provides the built-in command `help` to provide easy access to them and improve the formatting of their display, e.g.

```plaintext
>>> help(module_docn)
Help on module module_docn:

NAME
module_docn

DESCRIPTION
This is the module documentation pointing out that
this is an artificial test module.

FUNCTIONS
test_fn_1()
    This is the first test function.
    It doesn't do anything.

test_fn_2()
    This is the second test function which also does nothing.

FILE
\\home\profiles\kreed\documents\cpsc128\programs\module_docn.py

>>>
```

All the information displayed is automatically extracted from the docstrings in the module. The pydoc module which is used behind the scenes by `help` is also used to produce much of the HTML Python documentation you encounter on the web. Just for completeness I will point out that `help` can also be used on an individual member function,

```plaintext
>>> help(module_docn.test_fn_1)
Help on function test_fn_1 in module module_docn:
test_fn_1()
This is the first test function.
It doesn't do anything.
>>>
```

or more usefully on real functions,

```plaintext
>>> help(math.sqrt)
Help on built-in function sqrt in module math:
sqrt(...)
sqrt(x)

Return the square root of x.
>>>
```

## Summary

-   Place triple quoted docstrings at the top of each module and after
    each function definition. These should provide provide descriptions
    of what the module and each function do.
-   Use the `help()` built-in to access the docstrings of modules and
    functions you import.
