# Testing with doctest

By example I've illustrated a large number of ways of writing testing
harnesses for code during this course. The way they were constructed
depended on the kinds of tests needed to verify the code works.

Python provides a nice built-in mechanism that makes it easy to express
tests for many kinds of programs and produces useful documentation at
the same time. The `doctest` module lets you include test specifications
in docstrings and then automatically extracts and uses them and reports
on the results. The rationale behind it is roughly that (i) we all agree
that documentation is good, and (ii) we all agree that testing is good,
so, why not combine the two and have the tests supplement the
documentation? This has the added benefit of keeping the tests right
with the code they test and not somewhere else in the module.

Here's a familiar bit of code with tests in it and a main routine that
will run and report on the tests:

```python
# WumpusAdjMatrixMap.py
#
# Adjacency matrix representation of a cave_system.
# A 1 at entry [i, j] indicates that you can get from room i to room j.
#
# Note that this cave_system is not a dodecahedron and that some tunnels
# are 1-way.
cave_system = []
cave_system.append([0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
cave_system.append([1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0])
cave_system.append([0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0])
cave_system.append([0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0])
cave_system.append([0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1])
cave_system.append([0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0])
cave_system.append([0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0])
cave_system.append([0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0])
cave_system.append([0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1])
cave_system.append([0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
cave_system.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0])
cave_system.append([1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0])
cave_system.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1])
cave_system.append([0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0])
cave_system.append([1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0])
cave_system.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1])
cave_system.append([0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0])
cave_system.append([1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0])
cave_system.append([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1])
cave_system.append([0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0])

def tunnels_from(cave_map, room_number):
    ''' returns a list of the rooms that can be reached from room room_number.
    >>> tunnels_from(cave_system, 0)
    [1, 4, 7]
    '''
    pass

def tunnels_to(cave_map, room_number):
    ''' returns a list of the rooms that have tunnels leading to room room_number.
    >>> tunnels_to(cave_system, 0)
    [1, 11, 14, 17]
    '''
    pass

if __name__=='__main__':
    import doctest
    doctest.testmod()
```

The `testmod` method will extract the lines in the docstrings that look
like interactive python sessions, i.e. the ones beginning with `>>>` and
the lines following them. It will execute the commands after the `>>>`s
and compare their output with the lines following them. If the actual
output matches the specified output it counts as a success. If they do
not match it counts as a failure, and reports on it. For example here is
the output from executing the module above:

```plaintext
>>> 
**********************************************************************
File "__main__", line 32, in __main__.tunnels_from
Failed example:
    tunnels_from(cave_system, 0)
Expected:
    [1, 4, 7]
Got nothing
**********************************************************************
File "__main__", line 39, in __main__.tunnels_to
Failed example:
    tunnels_to(cave_system, 0)
Expected:
    [1, 11, 14, 17]
Got nothing
**********************************************************************
2 items had failures:
   1 of   1 in __main__.tunnels_from
   1 of   1 in __main__.tunnels_to
***Test Failed*** 2 failures.
>>> 
```

You can see that the output shows what it expected to get and what it
actually got test by test, and at the end it summarizes the
failures. `testmod`'s default setting is to be silent on successes so
had there been successful tests they would have generated no output.

The strengths of the `doctest` approach to testing are that:

-   It enables you to embed your tests in your documentation.
-   It requires you to be specific about the exact result you expect.
-   The tests enhance the documentation by providing specific examples
    of how a function should operate.
-   The tests become part of the function definition. In concrete terms
    they are kept near the function rather than elsewhere in the module
    or worse, spread around the module.

The downside to the doctest approach is just that not all methods lend
themselves to being run in a shell session, and that is doctest's only
paradigm. It also can't help you catch runtime errors in interactive
programs, e.g. problems with bat snatching in Hunt the Wumpus.

On balance it is best to think about doctest as a good starting point,
but not necessarily sufficient on its own.

You can read more about doctest in [Section 26.2 of the Python
documentation](http://docs.python.org/library/doctest.html).


