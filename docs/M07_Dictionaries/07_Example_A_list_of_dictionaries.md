# Example: A list of dictionaries

Hopefully the last example reminded you that the values in a dictionary can be of any Python type. In the same way that other types can occur inside dictionaries, dictionaries can occur inside other Python data structures. In fact much of the power of programming comes from the freedom with which we can combine its elements. In Part I of the course we saw the many ways that control structures can be combined. Similarly here in Part II we will see that the same applies to data structures. Accordingly our next exhibit is a list of dictionaries. _List_ because the outermost brackets are square, _of dictionaries_ because the inner brackets are curly.

```
data = [ {'id':4721, 'sex':'F', 'age':31},
         {'id':1828, 'sex':'M', 'age':56},
         {'id':7816, 'sex':'M', 'age':72},
         #. . . lots more records . . .
         {'id':3286, 'sex':'M', 'age':29},
         {'id':5063, 'sex':'F', 'age':22}
       ]
```

## Problem 1

How could we display the entry of the oldest individual?

## Pseudocode

```
We have to start somewhere so let's begin with the first entry
and set it to be the oldest record (after all it's the oldest
we have seen so far!)
Consider each item in the database from the second to the end
    If the age of this entry is older than our current oldest
        Update our oldest record
Display the oldest record
```

## Python code

```
# 70_list_of_dicts.py
data = [ {'id':4721, 'sex':'F', 'age':31},
         {'id':1828, 'sex':'M', 'age':56},
         {'id':7816, 'sex':'M', 'age':72},
         #. . . lots more records . . .
         {'id':3286, 'sex':'M', 'age':29},
         {'id':5063, 'sex':'F', 'age':22}
       ]

oldest = data[0]
for entry in data[1:]:
    if entry['age'] > oldest['age']:
        oldest = entry
print('The oldest person is:', oldest)
```

The output of this is,

```
>>>
The oldest person is: {'age': 72, 'id': 7816, 'sex': 'M'}
>>>
```

Notice that the order of the key-value pairs in the output does not match that in the input. This is generally the case with dictionaries. The output order matches the internal storage order of the pairs, not the input order.

(For thought: what should the output be when there are two equally old people, e.g. in this case what if there were two 72 year olds?)

## Problem 2

How could we output the number of male and female records?

## Pseudocode

```
Set counter of males to 0
Set counter of females to 0
Consider each item in the database
    If the value for the key 'sex' is 'M'
        Increment the counter of males
    Elif the value of the key 'sex' is 'F'
        Increment the counter of females
Display the male and female counters
```

<br>

## Python Code

    nmales = 0
    nfemales = 0
    for entry in data:
        if entry['sex'] == 'M':
            nmales = nmales + 1
        elif entry['sex'] == 'F':
            nfemales = nfemales + 1
    print('There are', nmales, 'males and', nfemales, 'females.')

Notes:

-   You may be wondering why I used `elif` and another test rather than
    just an `else`. This makes the code easy to modify for people who
    don't identify as either gender.
-   The `n` prefix on the counts is a common (but optional) naming
    practice. It indicates the name represents a count. Why `n` and
    not `c` for count? Probably because `n` is commonly used for counts
    in math courses.


