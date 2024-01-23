# Exercise Sheet 3

For the following problem descriptions decide whether it would be best to use an **if** statement (with or without elifs and else), a **while** loop, or a **for** loop. You don't have to write code for all of these. **Pick one to solve and show me.**

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

2. Write a guessing game program where the user has to guess a number between 1 and 100. The computer will let the user know if they are too high or too low after each guess and stop when the user the guesses correctly. Then it will tell the user about their glorious victory!

3. Get the length and width of a rectangle and tell the user if it is a square or not.

4. Use nested a loop to write a program that outputs a multiplication table for each number from 1 to a number input by the user. The final output should look something like the example below.

```plaintext
Enter the biggest number in the table: 5
1    2    3    4    5
2    4    6    8   10
3    6    9   12   15
4    8   12   16   20
5   10   15   20   25
```

5. Write a program that gets the users salary and tells them how much income tax they will pay based on the table below.

    | 2022 FEDERAL INCOME TAX BRACKET | 2022 FEDERAL INCOME TAX RATE |
    |:-------------------------------:|:----------------------------:|
    |   $50,197 or less               | 15% |
    |   $50,198 to $100,392           | 20.5% |
    |    $100,393 to $155,625         | 26% |
    |    $155,626 to $221,708         | 29% |
    |    $221,709 and above           | 33% |


6. Write a program that gives the computer a simulated (and untimed) Paced Auditory Serial Addition Test (PASAT). The computer will keep getting positive integer numbers from the user and add the last two values entered before getting the next value. This is actually quite complicated for a person to keep track of but will be easy for the computer. The program will stop when the user enters a negative number. Below is an example run of the program (5+3=8, 3+4=7, 4+6=10,done).

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

7. Write a program that converts a number from a decimal number to a number in binary using the following pseudocode.

```plaintext
1. Divide the decimal number by the value of the new base (i.e. 2 for binary)
2. Get the remainder and make it the right most digit of the new number.
3. Divide the quotient of the last step by the new base.
4. Get the remainder and make it the 2nd right most digit.
5. Repeat steps 3 and 4 until the quotient is zero.
```

8. Write a program that draws different sized triangles depending on the user’s input. You will need to think about how the spaces are related to the total number of rows (0 spaces in the last row, 1 in the second last row...) and how the number of stars is related to the position of the row relative to the top (1 star first row, 3, stars second row...). I’ve included two example runs below to give an idea of what I mean.

```plaintext
Enter the size of the triangle: 3
  *
 *** 
*****

Enter the size of the triangle: 6
     *
    ***
   *****
  *******
 *********
***********
```