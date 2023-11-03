# Assignment 12

## Problems

1.  Split into two groups and draw a UML class diagram for Hunt the 
    Wumpus. One group will wirte the UML for the design given in 
    in class and the other group will do a UML for an alternative 
    design (Simon's implementation). You can do this by hand or using 
    software (for example MS Visio or Gliffy), it's up to you. Once 
    both groups have a UML diagram we will compare and discuss the 
    advantages and disadvantages of each design.


2.  Add a docstring containing a sufficient set of doctest tests and 
    a call to run those tests to the module below,

        # ScrabbleScoring.py
        LETTER_VALUES = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 'G':2,
                 'H':4, 'I':1, 'J':8, 'K':5, 'L':1, 'M':3, 'N':1,
                 'O':1, 'P':3, 'Q':10, 'R':1, 'S':1, 'T':1, 'U':1,
                 'V':4, 'W':4, 'X':8, 'Y':4, 'Z':10}
        def scrabble_value(s):
           'Returns the Scrabble score for the letters in the string s.'
            total_value = 0
            for letter in s:
                total_value = total_value + LETTER_VALUES[letter]
            return total_value

3.  Replace the code below that tests the function isStraight with an 
    equivalent set of doctests. Fill in the body of isStraight and 
    run the tests on it.

        # is_straight_doctest.py
        def isStraight(hand):
            pass
        if __name__ == '__main__':
            # TEST_HANDS is a list containing the hands of cards to use in testing
            # the function isStraight, and the correct result for each hand.
            # Note that not all hands have five cards, and some are straights,
            # while some are not.
            TEST_HANDS = [
                [[ 1, 2, 3, 4, 5 ], True],
                [[ 5, 4, 3, 2, 1 ], True],
                [[ 14, 0, 28, 42, 4 ], True],
                [[ 1, 2, 3, 4, 5, 6 ], True],
                [[ 5 ], True],
                [[ 1, 2, 2, 4, 5 ], False],
                [[ 1, 2, 2, 5, 5 ], False],
                [[ 1, 3, 5, 7, 9 ], False]
            ]
            print 'Testing isStraight ... '
            # Loop through the list of TEST_HANDS, to test each sample hand.
            for test in TEST_HANDS:
                # If the function isStraight does not return the correct
                # result...
                if isStraight(test[0]) != test[1]:
                    # ... display an error message
                    print 'isStraight fails on', test[0]


## Logistics

-   Use the following naming scheme for your program files:
    `a`*assignment#*`p`*problem#*yourname`.py` . So your code for the 
    the first problen of this assignment will be named `a11p1bob.py` 
    (adjusted obviously to use your name).

-   Please submit your `.py` file to the Moodle dropbox.
