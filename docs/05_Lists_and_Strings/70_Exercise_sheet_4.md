# Tutorial 4

0.  ### Library 
    Write a list of lists that represents a library of books. Each book 
    in the list should have a title, author, and number of pages stored 
    as part of each book ["The Giver", "Lois Lowry", 240]. Try making 
    your own library of books. Then see if you can do the following 
    things with your library.

    a. Write some code asking for input to add a new book to the library.

    b. Write some code that prints all the titles in the library.

    c. Write some code that prints all the authors in the library.


1.  ### Poker Flush

    Write a program that decides if a list of card numbers is a flush.
    A flush is a hand in which all 5 cards share one suit. For example
    the list `[6, 0, 11, 2, 5]` is a flush because all the cards are 
    clubs.

    Use the first representation shown in the module notes, i.e. the one
    in [Representing Playing Cards](08_Representing_playing_cards.md).

    Do not remove your test values from the program so I can see how
    thoroughly you tested your code. You can show me your tests and 
    explain why you chose them when you show me your code.

2.  ### Dedup

    Write a program that removes duplicate values from a list, i.e. if
    the list starts out as `[4, 2, 5, 2, 4]`, then after your code
    fragment runs it should be `[4, 2, 5]`.

    Embed your code in the file [t4p2kate.py](90_t4p2_kate.py)

    (A real-life application would be to remove duplicates from a list
    of IP addresses so you have a list of unique visitors to your site.
    In this case the list might look like `[ '10.9.0.31',
    '199.247.52.3', '10.9.0.31', '43.98.12.4', '72.1.3.55',
    '199.247.52.3', ...]`).