# Exercise Sheet 2

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

2. Fill in the rest of the truth table for the following logical expression `((A or B) and not C)`. I’ve made some extra columns so that you can work through it step by step.


    | A | B | C | not C | A or B | ((A or B) and not C) |
    |:-:|:-:|:-:|:-:|:-:|:-:|
    | T | T | T |  F |    T |              F| 
    | T | T | F |  T |    T 
    | T | F | T |  F 
    | T | F | F   
    | F | T | T 
    | F | T | F 
    | F | F | T 
    | F | F | F


3. Write a program that takes a number from the user and prints the absolute value of that number (so if it is a negative number, it will switch it to a positive number before it prints).                              

4. Write a program that gets an integer from the user. It should then print the number with the appropriate suffix (i.e. 552 would be **552nd**. For example if the user entered the number 1, you would print 1st. You can use the modulo operator to figure out the appropriate suffix for each number. `num % 10 == 1` will return `True` if the last digit is 1. For your first try ignore numbers that end in 11th, 12th, and 13th which are weird cases because they don’t use 1st, 2nd, and 3rd. Below is the pseudocode.


        Get the number as input from the user
        Check to see if the number ends in a 1
            print the number with 'st' at the end
        Otherwise check to see if the number ends in a 2
            print the number with 'nd' at the end
        Otherwise check to see if the number ends in a 3
            print the number with 'rd' at the end
        Otherwise
            print the number with 'th' at the end
