# What is this \[ \[ 'X', 'O', '' \], \[ 'O', 'X', 'O' \], \[ '', '', 'X'\] \] ?

Thinking like the computer,

-   we know `52` is an integer value,
-   we know `52.801` is a floating point value because of the decimal
    point, and
-   we know `'Tim'` is a string because of the quotes around it

Similarly we know `[['X', 'O', ''], ['O', 'X', 'O'], ['', '', 'X']]` is
a list because of the square brackets around it. Yes, it also has square
brackets inside it, but ignore those for a moment. What matters is that
it has the pattern `[ ...`*`stuff`*`...]` which makes it a list.

Now what is it a list of? Well the commas separate the items of the list
and the things between the commas,
i.e. `['X', 'O', '' ]`, `[ 'O', 'X', 'O' ]` and, `[ '', '', 'X']`, are
all surrounded by square brackets so they are *also* lists. That means
that the entire construct is *a list of lists*.

When the sizes of all the lists are the same as they are here (because
the outer list has three elements, and each inner element also has three
elements) the whole is often called a multi-dimensional list, in this
particular case a two-dimensional (2-D) list*. These are also sometimes
called arrays, especially in mathematical applications.

This 2-D list represents the state of a game of Tic-Tac-Toe. This is
easier to see if we write it differently (in a way that is still valid
Python by the way) and show it beside the game it is representing.

```
[['X', 'O',  ''],      X | O |   
                      ---+---+---
['O', 'X', 'O'],       O | X | O
                      ---+---+---
[ '',  '', 'X']]         |   | X 
```

We access the items in a 2-D list by first choosing the sublist we want
and then specifying the item in the sublist we want. For example if we
name our 2-D list `g`,

    g = [['X', 'O', ''], ['O', 'X', 'O'], ['', '', 'X']]

then `g[0]` refers to the entire first row,
i.e. `['X', 'O', '' ]` and `g[0][1]` refers to the second element in
that row or `'O'`. Here is a table listing the names of each cell
in `g`:

  ----------- ----------- -----------
  `g[0][0]`   `g[0][1]`   `g[0][2]`
  `g[1][0]`   `g[1][1]`   `g[1][2]`
  `g[2][0]`   `g[2][1]`   `g[2][2]`
  ----------- ----------- -----------

The general pattern here is `g[`*`row`*`][`*`col`*`]`, i.e. the first
index specifies the row, and the second index specifies the column.

So we can test to see if someone has won by filling in the top row using
code like this,

    if g[0][0]==g[0][1] and g[0][1]==g[0][2]:
        print(g[0][0], 'has won!')
    else:
        print('No one has won in the top row.')

which will display the message,

    No one has won in the top row.

Similarly we can check to see if someone has won along the main
(upper-left to lower-right) diagonal with code like this,

    if g[0][0]==g[1][1] and g[1][1]==g[2][2]:
        print(g[0][0], 'has won!')
    else:
        print('No one has won on the main diagonal.')

which will display the message,

    X has won!

---

* Lists can certainly have more than two dimensions, but it gets hard
to draw them!
