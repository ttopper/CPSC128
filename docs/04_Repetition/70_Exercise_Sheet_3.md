# Tutorial 3

1. Write a program that gets two numbers from the user. The user calculates that number to the power of 1, 2, 3, 4, ... while the result is less than the second number. Below is an example run of the program.

```plaintext
Give me a number to “power” up: 2
Give me a place to stop: 50

2**1 = 2
2**2 = 4
2**3 = 8
2**4 = 16
2**5 = 32
```

2. Write a program that gives the computer a simulated (and untimed) Paced Auditory Serial Addition Test (PASAT). The computer will keep getting positive integer numbers from the user and add the last two values entered before getting the next value. This is actually quite complicated for a person to keep track of but will be easy for the computer. The program will stop when the user enters a negative number. Below is an example run of the program (5+3=8, 3+4=7, 4+6=10,done).

```plaintext
Give me a PASAT by giving me positive integers
to add. When you are ready to stop enter -1.

Start giving me numbers:
>5
>3
8
>4
7
>6
10
>-1
Done my PASAT! How did I do?
```

3.  Use nested a loop to write a program that outputs a multiplication table for each number from 1 to a number input by the user. The final output should look something like the example below.

```plaintext
Enter the biggest number in the table: 5
1    2    3    4    5
2    4    6    8   10
3    6    9   12   15
4    8   12   16   20
5   10   15   20   25
```

4. Drawing Diamonds
Write a program that displays a diamond on the screen, e.g.

          *
         ***
        *****
         ***
          *

Your program should ask the user how large a diamond to draw and
what character to use to draw it. (The size of a diamond is
specified by the lengths of its sides, i.e. 3 in the case above).