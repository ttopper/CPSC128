# What can you do with a list?

The full list of list methods is in [Python Library
Reference](https://docs.python.org/3/tutorial/datastructures.html).
Here's an idea of how you might use and combine these methods to carry
out common operations.

Create a list:

-   Using `range`, e.g. `nums = list(range(10))`.
-   By listing the items in the
    list: `mishmash = [14, 'a', 4.19, 'Kate', True]`\
    Notice that values of several types can be stored in the same list.

Access an item from a list:

-   `mishmash[0]` is the first item in the list, i.e. `14`
-   `mishmash[1]` is the second item in the list, i.e. `'a'`
-   `mishmash[2]` is the third item in the list, i.e. `4.19`

Access a sublist of a list (called a slice in Python):

-   `mishmash[1:4]` is the sublist of items in `mishmash` from position
    1 up to but not including position 4, i.e. `['a', 4.19, 'Kate']`

    Note: that the range is \[*inclusive*:*exclusive*\]
    thus `mishmash[1:1]` is \[\]

    Note: a slice always returns a list,
    so `mishmash[1:2]` is `['a']` not just `'a'`.

Adding items to a list:

-   `mishmash.append(2)` appends `2` to the list, i.e. it adds it to the
    end of the list
    so `mishmash` becomes `[14, 'a', 4.19, 'Kate', True, 2]`
-   `mishmash.insert(1, 'hi')` inserts the string `'hi'` into the list
    in position `1`, i.e. after 14 but before `'a'`.
-   `mishmash = mishmash + ['bye']` appends `'bye'` to the list. (Note
    the `[]`s around `'bye'`).

Removing items:

-   by position: `del( mishmash[2] )` deletes the item at
    position `2` from the list.
-   by value: `mishmash.remove( 'a' )` removes the first (and only the
    first) occurrence of `'a'` from the list.
-   from the end of the list: `mishmash.pop()` removes the last item in
    the list.

Getting information about a list and its contents:

-   `in` can be used to test and see if an item is in a list,
    e.g. `if 'a' in mishmash:`. Note that `in` has to loop through the
    list checking to see if each item is `'a'` to do that so it is a
    relatively slow operation.
-   `len( mishmash )` returns the length of the list, i.e. the number of
    items in the list.
-   `mishmash.index( 'Kate' )` returns the position in which the first
    occurrence of `'Kate'` can be found.
-   `mishmash.count( 'Kate' )` counts the number of `'Kate'`s in the
    list.

Miscellaneous commands you should try out (because they will probably be
useful on assignments!):

-   `mishmash.sort()`
-   `mishmash.reverse()`
-   `mishmash.extend()`
-   `2*mishmash`
