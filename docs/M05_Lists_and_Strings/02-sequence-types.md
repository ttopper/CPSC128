# Sequence Types

The built-in types we have worked with so far have each stored a single value (formally they are _scalar_ types). But there are many real-world objects whose representation requires more than one value, e.g. a street address, someone's full name, a map coordinate. Python provides several compound data types, but we will begin by looking at strings and lists. These are both sequence types because they store an ordered list of values, that is a sequence of values (as opposed to unordered collections of values, which are formally called a _set_ of values). In strings all the values are characters, but a list may contain values of any type (including other lists!).

The official list of string operations can be found in the  [Python Library Reference](https://docs.python.org/3/library/stdtypes.html#string-methods).

## Exercises

To find out how they work, try typing the following commands into the
Python shell and carefully observing the output that each one produces.
First strings:

```python
>>> name = "Kate"
>>> "t" in name
>>> "o" not in name
>>> min(name)
>>> max(name)
>>> name = name + " " + "Chatfield-Reed"
>>> print(name)
>>> name[0]
>>> name[2]
>>> name[-1]
>>> name[-2]
>>> name[2:7]
>>> len(name)
>>> name*3
```

Now a list:

```python
>>> nums = [1, 2, 3, 4, 5]
>>> 3 in nums
>>> 9 in nums
>>> min(nums)
>>> max(nums)
>>> nums = nums + [9, 10]
>>> print(nums)
>>> nums[0]
>>> nums[2]
>>> nums[-1]
>>> nums[-2]
>>> nums[2:5]
>>> len(nums)
>>> nums[2] = 11
>>> print(nums)
>>> nums[2:6] = [20,30]
```
Note that the third to last statement can ONLY be used with a list and
NOT with a string (try it and see). That is because in Python lists
are _mutable_ (i.e. changeable), but strings are _immutable_ (i.e.
cannot be changed) so you cannot assign to individual elements of a
string.
