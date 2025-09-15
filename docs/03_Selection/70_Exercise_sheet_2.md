# Tutorial 2

1. Figure out what each program will print if the input is the number `-5`.

a)
```python
num = int(input('Enter a number: '))
if num > 0:
    print(num)
```

b)
```python
num = int(input('Enter a number: '))
if num % 2 == 0:
    print(num*2)
else:
    print(num**2)
```

c)
```python
num = int(input('Enter a number: '))
if num > 0 and num % 2 == 0:
    print("I'm positive it's even!")
elif num > 0:
    print("I'm positive it's odd!")
elif num == 0:
    print("Zip zero nada!")
elif num < 0 and num % 2 == 0:
    print("Even if it's negative?")
else:
    print("Even if it's odd?")
    
```

2. Write a program that takes a number from the user and prints the absolute value of that number (so if it is a negative number, it will switch it to a positive number before it prints).                              


3.  ### Is it a triangle?

    Write a program that accepts three numerical values and outputs a
    message indicating whether they could represent the lengths of the
    sides of a triangle or not. Look up the **triangle inequality theorem** 
    to help you design your program.

    A sample run might look like this,

        =================
        Is it a triangle?
        -----------------
        Enter your first value: 4
        Enter the second value: 9
        Enter the third value: 3
        I'm afraid those three numbers could NOT represent the lengths of the sides of a triangle.


**Optional**. Write a program that gets an integer from the user. It should then print the number with the appropriate suffix (i.e. 552 would be **552nd**. For example if the user entered the number 1, you would print 1st. You can use the modulo operator to figure out the appropriate suffix for each number. `num % 10 == 1` will return `True` if the last digit is 1. For your first try ignore numbers that end in 11th, 12th, and 13th which are weird cases because they don’t use 1st, 2nd, and 3rd. Below is the pseudocode.


        Get the number as input from the user
        Check to see if the number ends in a 1
            print the number with 'st' at the end
        Otherwise check to see if the number ends in a 2
            print the number with 'nd' at the end
        Otherwise check to see if the number ends in a 3
            print the number with 'rd' at the end
        Otherwise
            print the number with 'th' at the end
