# Example: Word Frequencies

Now that we have seen dictionary syntax let's put it to work and solve the problem of counting the frequencies of the words in a string. The input will be a string, and the desired output is a display of each word and the number of times it occurred in the string. We'll use a dictionary for our counters where each key-value pair in the dictionary will consist of a word and the number of times it occurred.

## Pseudocode

The pseudocode description might be,

```
get the string
break the string into a list of words
initialize a dictionary of counters
loop through the list of words
    if the word is in the dictionary
        increment its counter by 1
    otherwise
        set its counter to 1
loop through the entries in the dictionary
    for each entry display the key (the word) and the value (the count)
```

## Python

A straight translation into Python gives,

```
# WordFrequencies.py
# Get the string:
test_string = '''The programmer, who needs clarity, who must talk all day to
    a machine that demands declarations, hunkers down into a low-grade annoyance.
    It is here that the stereotype of the programmer,
    sitting in a dim room, growling from behind Coke cans, has its origins.
    The disorder of the desk, the floor; the yellow Post-It notes everywhere;
    the whiteboards covered with scrawl:
    all this is the outward manifestation of the messiness of human thought.
    The messiness cannot go into the program;
    it piles up around the programmer.
    ~ Ellen Ullman
'''

# Break the string into a list of words:
words = test_string.split()
# Initialize a dictionary of counters:
word_counts = {}

# Loop through the list of words:
for word in words:
    # If the word is in the dictionary:
    if word in word_counts:
        # Increment its counter by 1:
        word_counts[word] = word_counts[word] + 1
    # Otherwise:
    else:
        # Set its counter to 1:
        word_counts[word] = 1

# Loop through the entries in the dictionary:
for word in word_counts:
    # Display the key value pair:
    print(word, ':', word_counts[word])
```

## Refinements

When you run it and examine the output you will see that while this is a
useful core there are some erroneous entries in the output. Among them:

    The : 3
    floor; : 1
    annoyance. : 1
    the : 10
    ~ : 1

The problems here are that,

-   'The' and 'the' are the same word and so their counts should be
    combined.
-   The trailing punctuation on 'floor;' and 'annoyance.' should be
    removed since it is not part of the word, and could mislead counts
    since 'floor;' and 'floor,' would be separate entries.
-   '\~' is not a word at all and so should not be counted.

Application of some string methods can fix some of these problems,

-   We can use the `lower` method to convert strings to all lower case.
-   We can use `strip` to remove trailing (and leading) punctuation
    characters.
-   We can use `isalpha` to test that the string is all letters (and
    thus eliminate '\~').

The body of the loop then becomes,

```
for word in words:
    w = word.lower()
    w = w.strip('.,;:\'"?!()') # Notice the \ to escape the ' inside the string
    if w.isalpha():
        if w in word_counts:
            word_counts[w] = word_counts[w] + 1
        else:
            word_counts[w] = 1
```

Of course `isalpha` is too blunt an instrument since we now lose the
hyphenated words, but we could deal with that too (perhaps by writing
our own little function to check that a string contains only letters and
hyphens!), though it is a matter of details we will not pursue.
