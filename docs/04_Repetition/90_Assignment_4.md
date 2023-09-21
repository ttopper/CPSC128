# Assignment 4

## Problems

1.  ### More weird numbers

    "Take a four-digit number. Add the number formed by the first two
    digits to the number formed by the last two digits, and square the
    resulting sum. Surprise! You've got the original number back."

    Write a program to find all the four-digit numbers that have this
    property.

    For example, here's a number that fails the test: 1430. Add 14 to
    30 to get 44, square 44 to get 1936, but this is not what we started
    with (i.e. 1430) so this number fails the test.

2.  ### Drawing Diamonds

    Write a program that displays a diamond on the screen, e.g.

          *
         ***
        *****
         ***
          *

    Your program should ask the user how large a diamond to draw and
    what character to use to draw it. (The size of a diamond is
    specified by the lengths of its sides, i.e. 3 in the case above).

3.  ### DONALD + GERALD = ROBERT

    Write a program that displays the solution(s) to the cryptarithm:

          DONALD
        + GERALD
        --------
          ROBERT

    Each letter represents one digit. No two letters represent the same
    digit. The numbers represented by DONALD, GERALD and ROBERT are
    well-formed, e.g. do not begin with 0. How fast can you make your
    program? The faster the better (but since someone once tried it let
    me say that presolving it and just the printing the solution is
    definitely a cheat!).

    Include [timing code](30_Timing_programs.md) in your program so I can
    compare its speed to others on my computer.

4.  ### Craps

    Write a program that outputs the probability of winning at the game
    of craps. The rules for the game of craps are:

    > A player rolls two dice. Each die has six faces. These faces
    contain 1, 2, 3, 4, 5 and 6 spots. After the dice have come to
    rest, the sum of the spots on the two upward faces is calculated.
    If the sum is 7 or 11 on the first throw, the player wins. If the
    sum is 2, 3 or 12 on the first throw (called “craps”), the
    player loses (i.e. the “house” wins). If the sum is 4, 5, 6, 8,
    9 or 10 on the first throw, then that sum becomes the player's
    “point”. To win, you must continue rolling the dice until you
    “make your point”. The player loses if they roll a 7 before making
    their point.

## Logistics

-   Use the following naming scheme for your program files:
    `a`*assignment#*`p`*problem#*name`.py` . So your solution for problem 1 on this assignment will be named `a4p1bob.py` .

-   Submit your assignment through the Moodle page. There will be a Dropbox for the assignment for you to upload your `.py` files.
