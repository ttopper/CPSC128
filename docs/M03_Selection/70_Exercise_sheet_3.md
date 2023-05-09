# Exercise Sheet 3

0. Write a program that takes a number from the user and prints the absolute value of that number (so if it is a negative number, it will switch it to a positive number before it prints).

1. Write a program that gets an integer from the user and identifies it as an even or odd number. The output should be either ‘it’s even’ or ‘it’s odd’. What math operator should you use?

2. Fill in the rest of the truth table for the following logical expression `((A or B) and not C)`. I’ve made some extra columns so that you can work through it step by step.


    | A | B | C | not C | A or B | ((A or B) and not C) |
    |:-:|:-:|:-:|:-:|:-:|:-:|
    | T | T | T |  F |    T |              F| 
    | T | T | F |  T |    T 
    | T | F | T |   F 
    | T | F | F   
    | F | T | T 
    | F | T | F 
    | F | F | T 
    | F | F | F


3. Write a program that takes a numerical grade out of 100 as input. It should return the students letter grade based on the table below. There are three solutions to this problem in the Moodle. I encourage you to solve it on your own and then compare your answer to the options in the Moodle. Is there a more efficient or elegant way to solve the problem than what you chose?

    | Grade | Letter |
    |------|:-:|
    | 95-100 | A+ | 
    | 86-94 | A |
    | 80-85 | A- |
    | 75-79 | B+ |
    | 70-74 | B |
    | 65-69 | B- |
    | 62-64 | C+ |
    | 58-61 | C |
    | 55-57 | C- | |
    | 50-54 | D |
    | <50 | F |
                                                  

4. Write a program that takes a total annual salary in dollars and returns how much federal income tax that individual will have to pay. There is a good example about heating bills in the Moodle that may help you figure out how to solve this problem.

    **Bonus**: Try and make it display the result with only 2 numbers after the decimal place. There are some examples and instructions near the end of this week’s Moodle to help start playing with print formatting.

    | 2022 FEDERAL INCOME TAX BRACKET | 2022 FEDERAL INCOME TAX RATE |
    |:-------------------------------:|:----------------------------:|
    |   $50,197 or less               | 15% |
    |   $50,198 to $100,392           | 20.5% |
    |    $100,393 to $155,625         | 26% |
    |    $155,626 to $221,708         | 29% |
    |    $221,709 and above           | 33% |


5. Write a program that gets an integer from the user. It should then print the number with the appropriate suffix. For example if the user entered the number 1, you would print 1st. You can use the modulo operator to figure out the appropriate suffix for each number. Remember that numbers that end in 11th, 12th, and 13th are special cases because they don’t use 1st, 2nd, and 3rd. An example run is shown below.

    ```
    Enter a whole number: 552
    That is the 552nd number.
    ```