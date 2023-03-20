# Palindrome

## Problem

Write a program that inputs a string and determines if it is a palindrome. A palindrome is a string that reads the same forwards or backwards, e.g. "bob" and "madam". An excellent program would be able to deal with entire phrases by ignoring capitalization, spaces and punctuation in the input, e.g. "A man, a plan, a canal, Panama!" is a palindromic phrase and should be identified as such.

## Solution 1

Ignoring, for the moment, palindromic phrases and focussing instead on words like "madam", the striking thing about a palindrome is that it is the same forwards and backwards. That means that the first letter is the same as the last letter, the second letter is the same as the second last letter, etc. In pseudocode,

```
if first_letter == last_letter and second_letter == second_last_letter and ...
    Then it is a palindrome.
else
    It is NOT a palindrome.
```

Let's move this one step closer to Python by figuring out the indices of those letter positions,

```
if s[0]==s[len(s)-1] and s[1]==s[len(s)-2] and s[2]==s[len(s)-3] and ...
    Then it is a palindrome.
else
    It is NOT a palindrome.
```

We have enough programming experience by now to see that this solution is unworkable exactly as it is since we don't know ahead of time how many test expressions we need (because we don't know ahead of time how long the string is). But the concept is sound and we can make it workable if we replace the `if` statement with a loop that iterates through the font half of the string comparing the characters there to their counterparts in the back half of the string. We'll use the same strategy to detect a palindrome that we did to [detect a flush in a poker hand](09-poker-hands.md): Assume the word is a palindrome and then test to see if we are right. As before we will use a flag variable to keep track.

```
palindrome = True # Our flag variable.
for offset values from 0 to len(s)/2
    if s[offset] != s[len(s)-1-offset]
       palindrome = False
if palindrome
    then it is a palindrome
else
    It is NOT a palindrome
```

Now it's a small step to actual Python (long live stepwise refinement!):

```
s = "madam"

palindrome = True
for offset in range(0, len(s)/2):
    if s[offset] != s[len(s)-1-offset]:
       palindrome = False

if palindrome:
    print("It is a palindrome!")
else:
    print("It is NOT a palindrome.")
```

## Solution 2

Python is often described as a batteries-included language because its built-in libraries are so extensive. We had good luck earlier finding short solutions by leveraging the libraries so let's try that again.

A palindrome is a string that is the same forward and backward. That means it is the same as its reverse. So, another approach would be to build the reverse of a string and compare it to the original. If they are the same then it's a palindrome. Lists have a built-in `reverse` method, but unfortunately strings don't (because they are immutable they can't have a method that changes them). Still, perhaps we can convert our string to a list. Let's try it in the Python shell and see,

```
>>> s = "madam"
>>> slist = list(s)
>>> slist
['m', 'a', 'd', 'a', 'm']
>>>
```

That was easy! Now we can reverse that list,

```
>>> slist.reverse()
>>> slist
['m', 'a', 'd', 'a', 'm']
>>>
```

build a string from it and compare that to the original string. (Note that we can't just compare `slist` and the result of `slist.reverse()` because `reverse` changes the list _in place_, that is it changes `slist` itself rather than creating a new string).

We build a string from a list using a joining string and the string method `join`. Here's a general example:

```
>>> iplist = ['199', '147', '23', '5']
>>> ip = '.'.join(iplist)
>>> ip
'199.147.23.5'
>>>
```

In our case we want to join our characters without anything between them. We can do that by using the empty string '' (that's two single quotes with nothing between them) as our joining string,

```
>>> s_reversed = ''.join(slist)
>>> s_reversed
'madam'
>>>
```

Putting all these pieces together we have,

```
s = "madam"
slist = list(s)
slist.reverse()
s_reversed = ''.join(slist)
if s == s_reversed:
    print("It is a palindrome!")
else:
    print("It is NOT a palindrome.")
```

## Refinements

The original problem statement taunted us by saying that "An excellent program would be able to deal with phrases by ignoring capitalization, spaces and punctuation in the input, e.g. 'A man, a plan, a canal, Panama!' is a palindromic phrase" and it would be nice if our code identified it as such. The trick here is to preprocess the string before letting our code from above at it. What we'll do is take the string and build a new one from it. As we build the new one we will lowercase any capital letters, and exclude any characters that are not alphabetic. The resulting code is,

```
s = "A man, a plan, a canal, panama."
print(s, "becomes...",end='')
s_new = ''
for c in s:
    if c.isalpha():
        if c.isupper():
            s_new = s_new + c.lower()
        else:
            s_new = s_new + c
print(s_new)
```

and the output is,

```
>>>
A man, a plan, a canal, panama. becomes...
```

amanaplanacanalpanama

```
>>>
```

If we place this code before either of our palindrome tests from above we have a complete, and hopefully _excellent_, program.

## Testing

So far we have just used "madam" and been pleased when our code
correctly identified it as a palindrome, but that's not sufficient
testing. What would be good additional tests? Well madam is a palindrome
with an odd number of letters,

-   but we should also test one with an even number of letters.
-   In addition we should test non-palindromes with both odd,
-   and even numbers of letters.
-   We should also test "at the edges". This suggests we test some
    short strings, perhaps one letter
-   and two letter strings. All one letter strings are palindromes but
    we should try both palindromic and non-palindromic two letter
    strings.
-   And of course we should test a string with non-alphabetic characters
    in it.

A good set of test values then would be:

    madam
    maam
    motor
    moor
    a
    oo
    at
    A man, a plan, a canal, Panama!

Running our program multiple times to test all of these would be tiring
so it would be nice if we could automate it. We could do that by putting
our test values into a list and looping through it to run all the tests.
Thus the testing version of our program might look like this,

    TESTS = ['madam', 'maam', 'motor', 'moor', 'a', 'oo', 'at',
             'A man, a plan, a canal, Panama!']
    print('Testing Solution 1:')
    for s in TESTS:
        print(s,end='')
        # Preprocess s to lower case and remove non-alphas.
        s_new = ''
        for c in s:
            if c.isalpha():
                if c.isupper():
                    s_new = s_new + c.lower()
                else:
                    s_new = s_new + c
        s = s_new # Replace s with s_new.
        
        # Test to see if s is a palindrome using Solution 1.
        palindrome = True
        for offset in range(0, len(s)//2):
            if s[offset] != s[len(s)-1-offset]:
               palindrome = False
        if palindrome:
            print("is a palindrome!")
        else:
            print("is NOT a palindrome.")

This is an awkward way to test our code because we need to edit our
original program. Fortunately Python allows us to make our palindrome
testing code a stand alone function, and then to embed it into a module
that does automatic testing when run on its own, but from which we can
import the palindrome function if we need to use it. Creating such
modules and functions is the topic of the next course module.
