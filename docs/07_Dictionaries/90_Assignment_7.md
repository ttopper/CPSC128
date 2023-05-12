# Assignment 7

## Problems

1.  ### Every letter counts

    First up a problem to give you a little practice working with the
    collection types (lists and dictionaries). Write the following
    implementations of the function `letter_frequency` that takes a
    string and returns a collection type showing how often each letter
    of the alphabet occurs in the string.

    a.  The first version (`letter_frequencyA`) should return a list
        with 26 integer elements representing the frequency of
        occurrence of each letter of the alphabet in order from a to z.

    b.  The second version (`letter_frequencyB`) should return a list of
        26 lists, each of which contains a letter and its associated
        count.

    c.  The third version (`letter_frequencyC`) should return a
        dictionary that uses the letters as keys and whose values are
        the letters' counts.

    The program that will call these functions is
    [`letter_frequency.py`](90_letter_frequency.py). Your job is to replace
    the `pass` statements with function bodies that implement the
    functionality specified above. Studying the embedded tests should
    answer any other questions you have about the functions'
    operations.

2.  ### Anagrams

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

3.  ### Win 32 Network Resource Anlayzer

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

    Embed your functions in a module with an `if __name__`\... block
    that runs them and displays their output. It should import the
    file`net_res.py`.

4.  ### Topography

    No dictionaries required for this one. It just gives you some more
    practice working with lists of lists. Suppose you are given some map
    elevation data stored as a list of lists, e.g.

        data = [ [20, 54, 50, 64, 60, 63, 60, 48, 20, 20],
                 [20, 56, 72, 76, 72, 20, 52, 62, 53, 20],
                 [20, 52, 62, 81, 67, 23, 48, 67, 52, 20],
                 [20, 54, 54, 82, 72, 22, 42, 64, 50, 20],
                 [20, 53, 49, 87, 69, 47, 48, 49, 21, 20],
                 [20, 20, 62, 71, 61, 36, 28, 31, 22, 20],
                 [20, 20, 20, 20, 20, 22, 21, 28, 24, 20],
                 [20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                 [20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                 [20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
               ]

    Write a function called `peaks` that is passed a list of lists like
    this one and returns a list of the coordinates (row, col) of all the
    peaks in the dataset. A peak is a point that is higher than its
    eight surrounding neighbours (the red values at (2,7) and (4,3)
    above are the peaks and the orange values aroung them are their
    eight neighbours). For the data set above the function should
    return,

        [(2, 6), (4, 3)]

## Logistics

-   Use the following naming scheme for your program files:
    `a`*assignment#*`p`*problem#*``yourname`.py` . So your first
    attempt at problem 1 on this assignment will be named `a7p1bob.py`
    and your solution for problem will be named `a7p2bob.py` (adjusted obviously to use your name) .

-   Please submit all your .py files to the Moodle dropbox.
     
