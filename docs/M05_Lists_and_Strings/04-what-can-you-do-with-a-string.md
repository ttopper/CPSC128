# What can you do with a string?

Here's an idea of how you might use and combine these methods to carry
out common operations.

Create a string:

-   Read it in using `input`, e.g. `name = input('Enter your name: ')`.
-   Assign it a literal string value, e.g. `name = "Tim Topper"`

Access a character from a string:

-   `name[0]` is the first character in the string, i.e. `'T'`
-   `name[1]` is the second character in the string, i.e. `'i'`
-   `name[2]` is the third character in the list, i.e. `'m'`

(Note that each individual character in a string is itself a string —
albeit of length 1.)

Access a substring of a string (called a *slice* in Python):

-   `name[1:5]` is the substring of the string from position 1 up to,
    but not including, character 5, i.e. `'im T'`

    Note: that the range is \[*inclusive*:*exclusive*\]
    thus `name[1:1]` is '', the empty string.

Adding to a string. Because strings are immutable you cannot change the
contents of one, but you can create a new one and assign it to the same
name (which has the effect of replacing the old string object with a new
one).

-   `name = name + ' Smith'` adds `' Smith'` to the end of the string
    so `'Tim Topper'` becomes `'Tim Topper Smith'`
-   You can insert into a string by careful use of slices,
    e.g. `name = name[0:5] + 'Nicholas' + name[5:]` changes `'Tim Topper'` to `'Tim Nicholas Topper'`.

Getting information about a string and its contents:

-   `in` can be used to test and see if a substring is contained in a
    longer string, e.g. `if 'a' in name:`
-   `len( name )` returns the length of the string `name`, i.e. the
    number of characters in it.
-   `name.find( 'ola' )` returns the position in which the first
    occurrence of `'ola'` begins, and -1 if it is not found (see
    also `rfind` which searches from the back of the string towards the
    front).

Miscellaneous commands you should try out (because they will probably be
useful on assignments!):

-   `name.count('p')`
-   `name[2].isalpha()`
-   `':'.join(['abc','def','ghi'])`
-   `"867-395-0892".split('-')`
-   `" Tim Topper ".strip()`
-   `40*"+"`
