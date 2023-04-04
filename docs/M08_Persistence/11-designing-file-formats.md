# Designing file formats

In the previous example we stored our coordinates "one pair to a line separated by white space". That description specifies a file format. Of course it's not the only file format possible. We could have put all the data onto one line, or separated items with commas instead of spaces, or... The limits to what we could design are just the limits of our ingenuity.

The differences of one versus many lines, and commas versus spaces are just cosmetic, but sometimes quite different approaches can be taken to storing some data. One accessible problem that affords different alternatives is the problem of storing the state of the universe in Conway's Game of Life. You can read about this "game" on [Wikipedia](http://en.wikipedia.org/wiki/Conway's_Game_of_Life) and play it online [here](http://www.bitstorm.org/gameoflife/) (among many others).

The universe in Conway's game of life is a grid of cells each of which can be in one of two states: alive or dead. A natural way to represent it in Python would be as a list of lists of cells (like a very large tic-tac-toe board):

```python
universe = [ [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 1, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]
           ]
```

## Option 1

One way to write this to a text file would be to write lines of space-separated 0s and 1s to the file:

```plaintext
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0
0 0 0 0 1 0 0 0
0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
```

The size of this file would be 136 bytes because we have one byte for the 0 or 1 for each cell, 1 byte for the space to separate them, and 1 byte for the line end marking the end of each row of the universe, i.e. 1 × 8 × 8 + 1 × 8 × 8 + 1 × 8 = 136 bytes. Generalizing this, an _n_ × _n_ universe would require 2 _n_<sup>2</sup> + _n_ bytes.

## Option 2

Using text graphics the universe might be displayed onscreen using blanks to represent dead cells and asterisks to represent live cells like this:

```
   *
    *
  ***
```

This suggests a second approach: we could save the state of the universe by taking a "snapshot" of it and writing that snapshot to the file. Our file would look just like the universe, and would use somewhat less storage because this time we use one byte (to store either a blank character or an asterisk character) for each cell, and one byte for the newline at the end of each row. Thus for an _n_ × _n_ universe we would require _n_<sup>2</sup> + _n_ bytes or roughly half as much storage (for medium and large values of _n_). For our 8 × 8 universe this approach uses 72 bytes.

## Option 3

You will have noticed when playing the online games of life (you did play them didn't you?) that the universe is usually "sparse", that is there are usually relatively few live cells among a great many dead ones. This is a consequence of Conway's rules: cells die easily of overcrowding, so if an area becomes densely populated the cells in it quickly die off keeping overall densities low. This suggests that we may be wasting space storing all those dead cells. Instead we should just store the locations of live cells. Our file format for the universe above would then be:

```
8 8
2 3
3 4
4 2
4 3
4 4
```

where each row after the first one records the location of one live cell in _row col_ form, i.e. the first number gives the row of the cell and the second gives its column. What about the 8s in the first row? With this representation the file does not directly convey the size of the universe as it did in the first two options so we must explicitly state the size of the universe; it's the job of the first line of data to give the height and width of the universe.

The storage requirement of this option depends not on the size of the universe, but on the number of live cells in it. For a universe less than 11 × 11 in size it uses 4 bytes per live cell (1 for row, 1 for separating space, 1 for col and 1 for line end), plus another 4 for the universe size. Generalizing: 4 _n_ + 4 bytes where _n_ gives the number of live cells.

(Note that the memory storage is _affected_ by the size of the universe just not solely determined by it. This is because more bytes are required to represent the row and column coordinates the larger the universe is. In a 1,000 × 1,000 universe most coordinates will be 3 digit numbers, e.g. (148, 763) so most lines will be 8 bytes long and the formula will become 8 _n_ + 8 bytes).

How does this compare with the first two options? For this specific example it uses 24 bytes. As long as the universe is sparse it will be more efficient, but for a crowded universe it will be less efficient. We can calculate the point at which it ceases to become more efficient by finding the number of live cells at which the storage for the two schemes is equal. Assuming a 1,000 × 1,000 universe, Option 1 will require 2,001,000 bytes, Option 2 will require 1,001,000 bytes, and Option 3's requirements will vary with the number of live cells:


| % live cells | Storage in bytes |
| :---: |:--:|
| 0 | 8 |
| 5 | 400,008 |
| 10 | 800,008 |
| 15 | 1,200,008 |
| 20 | 1,600,008 |
| 25 | 2,000,008 |

You can see that for this size of universe the break even point is around 12.5% live cells.

## Option 4

There are numerous other options, but one that often occurs to students is that since cells are either dead or alive their state could be stored using a single bit rather than an entire byte. This would reduce the storage requirements by a factor of 8 in the first two options. It is indeed possible to do this helped along by [Python's binary operators](http://docs.python.org/reference/expressions.html#binary-bitwise-operations) which allow us to manipulate the bits inside bytes, but these are not a focus of the course so we will just nod at this possibility as we move on by. (There are also fussy end conditions to deal with when the universe is not a multiple of 8 in size because then our information does not exactly fill bytes).

## Why no code?

Because it's part of the assignment! 🫣
