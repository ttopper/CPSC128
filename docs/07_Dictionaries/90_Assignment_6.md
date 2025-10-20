# Assignment 6

## Problems

1.  ### Anagrams

    An anagram is produced by rearranging the letters of one word or
    phrase to produce another word or phrase, e.g. "cat" and "act"
    are anagrams, as are "scare", "races", "acres" and "cares".
    Write two functions called `anagramsA` and `anagramsB` each of which
    returns True if the two strings it is passed are anagrams of each
    other and False otherwise. `anagramsA` should be based on the
    observation that if two strings are anagrams they each have the same
    numbers of each letter in them. This means that their letter
    frequency counts will be identical. `anagramsB` should be based on
    the observation that anagrams are strings that could be rearranged
    to be the same. One easy way to rearrange things is to use Python's
    built-in sort methods, so you could test to see if two strings are
    anagrams by sorting them and comparing the sorted versions.

2.  ### Win 32 Network Resource Anlayzer

    Many of the Win32 Network Resource enumeration tools return a list
    of dictionaries:

        [ {'name':'YVB127','comment':'Rm A2507','type':WKSTATION},
          {'name':'YVB143','comment':'Rm T1010','type':SERVER},
          ...
        ]

    Write the following functions to work with the `import`'ed file
    [net_res.py](90_net_res.py):

    a.  `count_summary()` should return a dictionary where the machine
        type is the key and the count of machines of that type is the
        value.

    b.  `list_by_type(type)` should be passed a type, e.g. SERVER and
        return a list of the rooms containing machines of that type.

    c.  `max_count()` should return the name of the room, e.g. 'Rm
        A2507', that contains the most computers.

    Embed your functions in a module with an `if __name__`... block
    that runs them and displays their output. It should import the
    file`net_res.py`.

3.  ### Topography

    No dictionaries required for this one. It just gives you some more
    practice working with lists of lists. Suppose you are given a
    minesweeper board stored as a list of lists, e.g.

        minesweeper_board = [[0, 0,   0, 1,   1, 1,   0,   0,   0, 0],
    			     [0, 1,   1, 2, 'M', 2,   1,   1,   0, 0],
    			     [0, 1, 'M', 3,   2, 3, 'M',   1,   0, 0],
    			     [0, 1,   2, 2, 'M', 3,   2,   2,   1, 1],
    			     [0, 1,   1, 2,   1, 2, 'M',   2, 'M', 1],
    			     [0, 1, 'M', 1,   0, 1,   2,   3,   2, 1],
    			     [0, 2,   3, 2,   0, 0,   1, 'M',   1, 0],
    			     [0, 1, 'M', 1,   0, 1,   2,   2,   1, 0],
    			     [0, 1,   1, 1,   0, 1, 'M',   1,   1, 0],
    			     [0, 0,   0, 0,   0, 1,    1,  1,   0, 0]
			    ]

    Write a function called `minesweeper_mistakes` that is passed a list 
    of lists like this one and returns a list of the positions 
    (row, col) of all the positions in the dataset where the number of
    adjacent mines is wrong. The number of adjacent mines is wrong when
    it does not match the number of mines ('M') in its 8 neighbours
    (the values at (3,2), (3,7), (6,2) and (8,8) do not correctly count
    their eight neighbours). Do not bother checking the borders for now,
    that makes it way more complicated (focus on 
    range(1,len(minesweeper_board)-1). For the data set above the
    function should return,

        [(3, 2), (3, 7), (6, 2), (8, 8)]

    I created a python file [minesweeper.py](90_minesweeper.py) that
    provides a display function and example board to work with.

## Logistics

-   Use the following naming scheme for your program files:
    `a`*assignment#*`p`*problem#yourname*`.py` . So your solution
    to problem 1 on this assignment will be named `a6p1bob.py`
    and your solution for problem 2 will be named `a6p2bob.py` (adjusted obviously to use your name) .

-   Please submit all your .py files to the Moodle.
     
