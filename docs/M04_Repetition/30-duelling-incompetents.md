# Duelling Incompetents

## The problem

Write a program to model the following peculiar duel (the names have been changed to protect the parties involved). A and B have quarelled and are going to settle their differences by duelling with pistols. Not only are A and B touchy, neither is a very good shot. A hits what he shoots at on average once every two tries. B is even worse, hitting what he shoots at once every three tries. Being a gentleman A allows B to fire first. The duel continues until one of them is hit.

Your program should determine who is most likely to win the duel, by simulating many duels between A and B. It should output the percentage of duels won by A and the percentage won by B.

## Getting to the Solution

Approach: We'll write this program from the inside out. Starting from the most specific event and working outward to a full program.

## B Shoots

The duel begins with B taking a shot at A. He can either hit or miss A. The chances that he hits A are 1 in 3. The chances that he misses are 2 in 3.

```python
import random

# B shoots at A
if random.randint(0, 2) == 2:
    print("B hits A. The duel's over.")
else:
    print("B misses A. The duel continues.")
```

## A Shoots

If B hits A then the duel ends, but if he misses the duel will continue. The duel continues by A taking a shot at B. This code is similar to B taking a shot at A, but the odds are different because A is a better shot. We put the code for A's shot into the else branch of the if above, since A only gets to shoot if B misses.

```python
import random

# B shoots at A
if random.randint(0, 2) == 2:
    print("B hits A. The duel's over.")
else:
    print("B misses A. The duel continues.")
if random.randint(0, 1) == 1:
    print("A hits B. The duel's over.")
else:
    print("A misses B. The duel continues.")
```
## One Complete Duel

Now if A hits B the duel is over, but if A misses the duel continues with B taking a shot. We could copy our B shooting code and add it in the second else branch above, but we could have to do that a lot, since the duel could, in principle, take an infinite number of rounds to complete. A simpler approach is to place the code above inside a `while` loop:

```python
import random
 
while ?:
        # B shoots at A
    if random.randint(0, 2) == 2:
        print("B hits A. The duel's over.")
    else:
        print("B misses A. The duel continues.") 
        if random.randint(0, 1) == 1:
            print("A hits B. The duel's over.")
        else:
            print("A misses B. The duel continues.")
```      
The question is what the `while` condition should be. We want to say, “while the duel is not over, they keep shooting at each other” and Python lets us come very close to writing this:

```python
import random

over = False
while not over:
# B shoots at A
if random.randint(0, 2) == 2:
    print("B hits A. The duel's over.")
    over = True
else:
    print("B misses A. The duel continues.") 
    if random.randint(0, 1) == 1:
        print("A hits B. The duel's over.")
        over = True
    else:
        print("A misses B. The duel continues.")
```
We declare a variable called `over` to hold the state of the duel. It's value is `False` when the duel is not over, and `True` when the duel is over. We initialize it to be `False` (since before they have shot at each other the duel can't be over). We update its value to `True` when one antagonist hits the other. The loop lets them keep taking turns shooting at each other until one finally hits the other.

This code successfully models a duel: run it and see.

## Many Duels

We are making progress but we are not done because the original problem wanted us to simulate many duels and display the percentage of duels won by each antagonist. To simulate many duels we pack all the code above (except for the `import`) into a `for` loop, and record, using counters, the number of duels each antagonist wins.

```python
import random

awins = 0
bwins = 0

for duel in range(0, 100): # See Pythonic Details for an explanation of range.
    over = False
    while not over:
        # B shoots at A
        if random.randint( 0, 2 ) == 2:
            print("B hit A. The duel's over.")
            bwins = bwins + 1
            over = True
        else:
            print("B missed A. The duel continues.")
            if random.randint( 0, 1 ) == 1:
                print("A hit B. The duel's over.")
                awins = awins + 1
                over = True
            else:
                print("A missed B. The duel continues.")
    print(6*'-')

print("A won", awins, "duels.")
print("B won", bwins, "duels.")
```

Note that we are careful to initialize our counters **above** the `for` loop, but to reset `over` to `False` **inside** the `for` loop.

## Remaining Work

We haven't quite met the question's requirements:

-   We need to display the percentage of wins by A and B (not just the
    absolute numbers of wins).
-   We shouldn't really hardwire the number of duels to be simulated
    (100 in the code above) into the program. It would be better to make
    it be a constant, and better yet to allow the user to specify the
    value.
-   And of course the appearance of the program onscreen could be
    improved.
