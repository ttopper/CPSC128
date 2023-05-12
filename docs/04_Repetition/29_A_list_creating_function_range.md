# A list-creating function: `range()`

The built-in function `range` creates arithmetic lists, and is often
used to produce the lists to drive `for` loops.

    range(start_value, stop_value, stepsize)

Example:

    >>> range(1, 20, 5)
    [1, 6, 11, 16]

You can tell that the value `range` returns is a list by the square
brackets and the commas.

Notes:

-   the_start_value_defaults to 0.
-   the_stepsize_defaults to 1.
-   the_stop_value_is NOT included in the list. This means that
    the `range` is asymmetric: because the starting value is included,
    but the stopping value is not included.

Try entering the following expressions in the Python shell and see what
results:

    >>> range(20)
    >>> range(10,20)
    >>> range(10,20,2)
    >>> range(20,2)

(Do you understand why the last one returns the value it does?)

Here's a little code snippet showing how `range` can be used to display
the squares of the numbers from 1 to 10.,

    print("Table of squares for 1-10")
    print("    x    x**2")
    for x in range(1,11):
        print("{:5d}{:8d}".format(x, x**2))

Note that since the stop value is NOT included in the list we have to
specify a stop value of 11 to include the value 10.
