# Dictionary "derivation"

## Think back

Earlier we saw that we could use a list as an array of counters, e.g. to calculate dice odds. The trick there was to map the outcomes of rolling a pair of fair dice, i.e. 2, 3, 4, ..., 11, 12, onto the entries in a list. Since lists are numbered from 0, we did that by subtracting 2 from each dice outcome. This mapped outcomes to counters as follows,

| Dice outcome |  | Counter |
| ---: | :-: | :---|
| 2 |  → | counters[0] |
| 3 |  → | counters[1] |
| 4 |  → | counters[2] |
| ... | ... | ... |
| 11 |  → | counters[9] |
| 12 |  → | counters[10] |

This is a nice little trick and programmers used similar ones to map all sorts of types onto list indexes so they could count them (or store information associated with them).

## Counting letters

For example if you want to count letters you need to map the letters of the alphabet onto counters like this,

| Letter |  | Counter |
| :---: |:-:|:---|
|  'a' |  → | counters[0] |
|  'b' |  → | counters[1] |
|  'c' |  → | counters[2] |
| ... | ... | ... |
|  'y' |  → | counters[24] |
|  'z' |  → | counters[25] |

This was done by taking advantage of the properties by which characters are stored in memory.

Since the days of teletypes characters had to be represented digitally and so there was an encoding for them. The most common for a long time was ASCII*. This specified the binary encoding for the common keyboard characters and control codes as shown e.g. [in this table](http://www.asciitable.com/). You can see the control codes teletypes required in the first 32 positions, followed by some special characters and digits, the capital letters, some more special characters, the lower case alphabet, and finally a few more special characters. Thankfully for the tricks below the letters were kept in sequence without intervening special characters. Most languages provide functions to get the ASCII value of a character. In Python this function is `ord`, (for **ord**inal position)

```
>>> ord('a')
97
>>>
```

Its inverse which returns a character corresponding to an ASCII code is `chr`,

```
>>> chr(97)
'a'
>>>
```

Using `ord` we can implement the mapping above by subtracting 97 (or more readably `ord('a')`) from the ordinal values of the characters,

```
test_str ='astringalingding'
counters = 26*[0] # Initialize list of counters to be 26 0s.
for ch in test_str:
    # Calculate index of counter for this letter in counters.
    index = ord(ch) - ord('a')
    # Increment appropriate counter.
    counters[index] = counters[index] + 1
for index in range(26):
    # Display letter corresponding to this index and its count.
    print(chr(ord('a')+index), counters[index])
```

Try it, and examine the output. Note how fragile the code is, e.g. insert a space into `test_str`, or a capital letter. (Don't worry you'll get to make it more robust on the assignment.)

## The limits of ingenuity...

Both these tricks we have seen for mapping sequences onto lists are ingenious but programmers' ingenuity hit a temporary stumbling block when they wanted to count the occurrences of words. At first it seems straightforward. We just need to map words onto counters something like this,


| word |  | Counter |
| ---: |:-:|:---|
|  'cat' |  → | counters[0] |
|  'dog' |  → | counters[1] |
|  'pie' |  → | counters[2] |
| ... | ... | ... |

But there are problems.

First our mappings from dice outcomes and letters to counters were based on the fact that they were both short sequences. The list of possible words is not short: the English language alone boasts roughly a million words and this is without counting proper names like the names of people and places. We can hardly initialize a list of a million counters each time we need to count the occurrences of words in some paragraph.

Second, it's not easy to see how to map 'cat' onto 0 and 'pie' onto 2. In our first two examples we were able to do so using simple arithmetic to deal with an offset between the two sequences first by subtracting 2 and then by subtracting 97. Here simple arithmetic will not suffice.

## ... call for greater ingenuity ...

Programmers tried numerous arithmetic tricks to map words onto indices. For example we could try adding together the ASCII codes for the letters in the words so 'cat' becomes ord('c') + ord('a') + ord('t') = 99 + 97 + 116 = 312 while 'dog' becomes ord('d') + ord('o') + ord('g') = 100 + 111 + 103 = 314. This works nicely for 'cat' and 'dog', but 'dog' and 'god' end up having the same code (as do all acronyms) which won't do.

To distinguish 'dog' and 'god' we have to take account of the order of the letters. One way to do this draws its inspiration from numbers. After all 574 and 475 are made from the same digits but we don't confuse them because the position of the numbers matters: 574 means "5 hundreds, 7 tens, and 4 ones" whereas 475 means "4 hundreds, 7 tens and 5 ones". We can adapt this positional scheme to code our strings. If 574 means (5 × 100) + (7 × 10) + (4 × 1) or (5 × 102) + (7 × 101) + (4 × 100) then by analogy cat should mean (3 × 262) + (1 × 261) + (20 × 260) — because c, a and t are the 3rd, 1st and 20th letters of the alphabet. Here's a function that calculates this kind of a string index,

```
def string_index( s ):
    index = 0
    for i in range(len(s)):
        index = index + (ord(s[-i]) - ord('a') + 1) * 26**i
    return index

print(string_index('cat'))
print(string_index('dictionary'))
```

(Note the use of the negative index in `s[-i]` to access the letters of the word from the back to the front, and `- ord('a') + 1` to get the letter's position in the alphabet).

This gives us unique numbers for words, but they get large quickly. 'cat's index is a modest 1199, but 'dictionary's is 49,655,615,398,718 which makes us long to deal with a mere million counters (that's 49 **trillion**).

## ... which calls for even greater ingenuity

Ingenuity knows few bounds so there are fixes of course. We can reduce large numbers to small ones by, for example, using modulo, %. If we want to limit ourselves to a list with 1,000 counters we can just use %1000 and our numbers will all be scaled into the range 0-999. Of course we may have collisions between indices whose last three digits are the same if we do that, but we can watch for that situation and handle it. We might also run out of counters if we have more than 1,000 unique words, but we can watch for that too and enlarge the list of counters if and when it happens. Are there risks of errors? Yes. Are there performance costs? Yes again (testing for collisions takes time; resizing a list takes more time). In all it took programmers a couple of decades of sustained development effort to iron out the major problems. In fact it remains an ongoing area of development in which no best solution is known. But the libraries of major languages contain robust efficient code for doing just this, and that code lies behind the implementation of dictionaries/hash tables/collections/mappings.

The `string_index` function above is called a _hashing_ function. A _hash_ is a unique identifier. In Python most objects can be hashed, not just strings. In fact you can see the internal hash for an object just by calling the built-in `hash` function,

```
>>> hash('cat')
-7283039196165750486
>>> hash('dicitonary')
-2899658674586044407
```

<br>

## Summary

A dictionary works by using a hashing function to get a unique numerical
identifier (hash) for an object, and then using that hash to locate the
data associated with the object (typically in a list). As long as the
hashing function can be computed quickly, and is unique, dictionaries
can be almost as fast as lists and yet allow for readable, meaningful
indexes.

------------------------------------------------------------------------

* ASCII is being slowly superseded by Unicode because the latter can
handle all the characters in all human languages rather than just the
few that appear on North American keyboards. Python 3 for example uses
Unicode exclusively for its strings. Most other languages are still some
ways from providing robust Unicode processing.
