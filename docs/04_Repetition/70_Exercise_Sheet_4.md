# Exercise Sheet 4

0. Write a program that gets two numbers from the user. The user calculates that number to the power of 1, 2, 3, 4, ... and stops when the result is more than the second number. Think about the weird cases like when the second number is smaller than the first number. Below is an example run of the program.

```plaintext
Give me a number to “power” up: 2
Give me a place to stop: 50

2**1 = 2
2**2 = 4
2**3 = 8
2**4 = 16
2**5 = 32
```

1. Write a program that gives the computer a simulated (and untimed) Paced Auditory Serial Addition Test (PASAT). The computer will keep getting positive integer numbers from the user and add the last two values entered before getting the next value. This is actually quite complicated for a person to keep track of but will be easy for the computer. The program will stop when the user enters a negative number. Below is an example run of the program (5+3=8, 3+4=7, 4+6=10,done).

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

2. Use nested `for` loops to write a program that outputs a multiplication table from 1 to a number input by the user. The final output should look something like the example below. You will need to use number formatting to get it to display like a table.

```plaintext
Enter the biggest number in the table: 5
1    2    3    4    5
2    4    6    8   10
3    6    9   12   15
4    8   12   16   20
5   10   15   20   25
```

3. Write a program, using either a `for` loop or `while` loop, that draws different sized triangles depending on the user’s input. You will need to think about how the spaces are related to the total number of rows (0 spaces in the last row, 1 in the second last row...) and how the number of stars is related to the position of the row relative to the top (1 star first row, 3, stars second row...). I’ve included two example runs below to give an idea of what I mean.

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