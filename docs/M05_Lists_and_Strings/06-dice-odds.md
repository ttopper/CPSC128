# Dice Odds

Imagine that before we go on vacation to Vegas we want to bone up on some of the relevant odds. Let's start with the frequency of various outcomes when rolling a pair of dice. We could do this by rolling a pair of fair dice many times and recording (counting!) how many times each outcome occurs. There are 11 possible outcomes because we can observe anywhere from 2 to 12 spots on the pair of dice. This means we need to record how many twos occur, how many threes occur, how many fours occur, and so on up to how many twelves occur.

## Solution 1: Without lists

Without using lists we could do it like this:

```
import random
ROLLS = 1000
# Initialize counters to 0.
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0
sevens = 0
eights = 0
nines = 0
tens = 0
elevens = 0
twelves = 0
# Roll dice many times and record frequency of outcomes.
for roll in range(ROLLS):
    outcome = random.randint(1, 6) + random.randint(1, 6)
    if outcome == 2:
        twos = twos + 1
    elif outcome == 3:
        threes = threes + 1
    elif outcome == 4:
        fours = fours + 1
    elif outcome == 5:
        fives = fives + 1
    elif outcome == 6:
        sixes = sixes + 1
    elif outcome == 7:
        sevens = sevens + 1
    elif outcome == 8:
        eights = eights + 1
    elif outcome == 9:
        nines = nines + 1
    elif outcome == 10:
        tens = tens + 1
    elif outcome == 11:
        elevens = elevens + 1
    else:
        twelves = twelves + 1

# Display results.
print("  =====================")
print("  Outcome | Occurrences")
print("  --------+------------")
print("      2   |{:8d}".format(twos))
print("      3   |{:8d}".format(threes))
print("      4   |{:8d}".format(fours))
print("      5   |{:8d}".format(fives))
print("      6   |{:8d}".format(sixes))
print("      7   |{:8d}".format(sevens))
print("      8   |{:8d}".format(eights))
print("      9   |{:8d}".format(nines))
print("     10   |{:8d}".format(tens))
print("     11   |{:8d}".format(elevens))
print("     12   |{:8d}".format(twelves))
print("  ---------------------")
```

which produces output like this,

```
>>>
  =====================
  Outcome | Occurrences
  --------+------------
      2   |      29
      3   |      66
      4   |      71
      5   |     100
      6   |     137
      7   |     173
      8   |     132
      9   |     122
     10   |      78
     11   |      59
     12   |      33
  ---------------------
>>>
```

The code is straightforward but lengthy, and relatively slow, because of the cascade of `if`s. On average it will take 5 and a half comparisons before finding the correct counter to increment. (We could do somewhat better if we reordered the tests in decreasing order of frequency, but if we knew their frequencies, we probably wouldn't be writing the code in the first place!).

## Solution 2: Using lists

These operations can be done more compactly and quickly using _a list of counters_. We'll let each item in the list count one of the outcomes so we'll need eleven entries in the list all initialized to 0. Then instead of using logic tests to identify the counter to increment we can use the `outcome` value as an index to directly access the appropriate counter.

```
import random

ROLLS = 1000

# Initialize counters to 0.
counters = [0] * 11

# Roll dice many times and record frequency of outcomes.
for roll in range(ROLLS):
    outcome = random.randint(1, 6) + random.randint(1, 6)
    # Now increment the appropriate counter.
    # Notice that no testing is needed because we can calculate the index of the matching entry.
    counters[outcome-2] = counters[outcome-2] + 1

# Display results.
print("  =====================")
print("  Outcome | Occurrences")
print("  --------+------------")
for posn in range(11):
    print("{:7d}   |{:8d}".format(posn+2, counters[posn]))
print("  ---------------------")
```

Notes:

* Notice the syntax used to initialize the list to contain 11 values of 0.
* The index of counters inside the loop is `outcome-2` because lists are indexed from 0, but our first outcome value is 2 (not 0), so we need to subtract 2 from the outcome to get the matching entry in the list. This way we'll map outcome 2 to counter 0, outcome 3 to counter 1, and so on up to outcome 12 mapping onto counter 10.
* Notice how the body of the output table can also be generated compactly thanks to the list.

## The verdict

  --------------------------------------------------- ---------------------------------------------------------
  Without list                                        Using list
  52 lines of code                                    12 lines of code
  Average 5.5 tests to select counter to increment.   Exactly one calculation to select counter to increment.
  --------------------------------------------------- ---------------------------------------------------------

 
