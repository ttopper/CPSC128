# Dictionaries

In use dictionaries^*^ look like lists that can be indexed by strings.
For example where a list can be indexed by numbers like 1 and 5,
e.g. `lst[1]`, `lst[5]` a dictionary can be indexed by strings like
'Tim' or 'Apt 101', e.g. `data['Tim']` and `data['Apt 101']`. In
modern implementations they manage to do that almost as fast as lists
can access their contents. That may not seem surprising to you, but it
is an impressive achievement. To give you an appreciation for why it is
surprising, and a deeper understanding of how dictionaries are
implemented, we'll go through a modest derivation of the mechanisms
underlying typical dictionary implementations.

------------------------------------------------------------------------

^*^ Aside: Known aliases. The data structures known as dictionaries in
Python go by many names. These include:

-   **Dictionary**: Python, Smalltalk, Objective-C, .NET.
-   **Hash** or **hash table**: C, C++, Perl, Ruby, Visual Basic, Common Lisp.
-   **Collection**: Visual Basic, Visual Foxpro.
-   **Map**: C++, Java.
-   **Associative array**: Javascript, AWK.

To be precise hashes and hash tables are one way of implementing a
dictionary and so refer to a lower level of abstraction than the term
dictionary.
