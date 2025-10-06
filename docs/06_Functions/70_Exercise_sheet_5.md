# Tutorial 5

0.  ### Make the code run
    Insert the necessary function definitions into the code below so
    that it will work properly (i.e. as shown in the sample runs below
    it).

    Notes:

    -   0 is a one-digit, even, unsigned number.
    -   You may not make any changes to the code below, i.e. your
        functions have to fit the code, you are not allowed to modify
        the code to fit your functions.

``` python
# t5p0name.py
# Just some practice writing little functions.
# Insert the necessary functions here.

line(60, '=')
print('Function practice')
line(60, '-')
num = int(input('Give me an integer value: '))
print('Your number contains', ndigits(num), end = ' ')
print('digits, is', even_or_odd(num), end = '')
if ispos(num):
    print(', and is positive.')
else:
    print(', but is not positive.')
line(60, '-')
```

```plaintext
============================================================
Function practice
------------------------------------------------------------
Give me an integer value: 78931
Your number contains 5 digits, is odd and is positive.
------------------------------------------------------------

============================================================
Function practice
------------------------------------------------------------
Give me an integer value: -122
Your number contains 3 digits, is even but is not positive.
------------------------------------------------------------
```
**Hint**: There are several ways of tackling the `ndigits` function.

-   You can find the number of digits by counting how many times you
    can divide a number by 10 before you get 0, e.g. 7 can be
    divided by 10 once, while 732 can be divided 3 times.
-   You can use the logarithm of the number to the base 10.
-   You can convert the number to a string and then use **len()** to
    see how long the string is.


1.  ### Poker Flush Function

    Write a function that decides if a list of card numbers is a flush.
    A flush is a hand in which all 5 cards share one suit. For example
    the list `[6, 0, 11, 2, 5]` is a flush because all the cards are 
    clubs.

    The function should take a list as its argument and return a Boolean.

    Do not remove your test values from the program so I can see how
    thoroughly you tested your code. You can show me your tests and 
    explain why you chose them when you show me your code.

2.  ### Dedup Function (must use either del or remove)

    Write a function that removes duplicate values from a list, i.e. if
    the list starts out as `[4, 2, 5, 2, 4]`, then after your code
    fragment runs it should be `[4, 2, 5]`.

    Think about what the arguments and return should be.

3.  ### Drawing Diamonds Function
    Fix the function that displays a diamond on the screen, e.g.

          *
         ***
        *****
         ***
          *

    Your function should get a number to indicate the size of the diamond
    to draw and a string to indicate what character to use to draw it.
    (The size of a diamond is specified by the lengths of its sides, i.e. 
    3 in the case above). The function should return None.

``` python

def diamond(size, char):
    char_count = 1
    space_count = size - 1

    for i in range(size):
        print(space_count*' ' + char_count*'*')
        char_count = char_count + 2
        space_count = space_count - 1

    char_count = char_count - 1
    space_count = space_count + 1
    
    for i in range(size,1,-1):
        print(space_count*' ' + char_count*'*')
        char_count = char_count + 2
        space_count = space_count - 1
        

diamond(3,'+')

``` 