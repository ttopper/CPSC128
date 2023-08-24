# Exercise Sheet 1

Here are some exercises to try in the python shell to get an idea of what you can do.

1. Printing things (this is a classic for your first program in every programming language):

```python
print("Hello, world!")
```

2. Storing values.

```python
name = "Kate"
print("Hello", name)
```

Think about why the comma might print in exercise 1, but not in exercise 2.

3. Printing things from input:

```python
name = input()
print("Hello", name)
```

You can enter any name, but that is not very clear.

4. Printing things from input again:

```python
name = input("Enter your name: ") 
print("Hello", name)
```

5. Try some basic math:

```python
speed = int(input())
duration = int(input())
distance = duration * speed print(distance)
```

Look at problems 3 and 4 and see if you can use that to change this code so that it is clear what you are supposed to input in problem 5. Could you make the output clearer as well?

6. You can convert from degrees to radians with the following equation: rad = deg * π/180 Here is that code written in python. Note that we have to import the value of pi from the library math.

```python
import math
print("This program converts degrees to radians. ")
degrees = int(input("Enter the angle in degrees: "))
radians = degrees * math.pi / 180
print("The angle in radians is equal to", radians)
```

7. This code can also be saved in a file. Python files all have the extension `.py`. If you create a new file in IDLE and save it as `deg2rad.py` you can run it from there (using the run drop down menu or by pushing F5). Try that out!

8. The way to convert from kilometers to miles is to divide by 1.6. Try to write a new python program that takes a speed in kilometers and outputs the speed in miles? Make sure it is clear what the user should input and what is being output. Equation: **mi = km / 1.6**

9. You can also run other people’s programs. I downloaded a python program my friend Jonathan from Calgary wrote for his introduction to object-oriented programming class ([TurtleMovingSimple.py](70_turtle_moving_simple.py)). You can download it from the Moodle and run it. It makes a turtle shaped pointer move around a window. When you are reading the program you may notice it has a bunch of writing that doesn’t look like python code after the `#` symbol. All of that information is called the comments and are meant to inform you (or anyone else reading the code) what is happening. Comments are ignored by the computer when the code is compiled. After you have run it try to edit different pieces to change the thickness of the line, the colour of the line, or the shape it draws. Even without knowing too much python you may be able to make a lot of these changes, that is because of the comments and because all the names for the variables and functions are quite clear.

10. If you got this far and still have some time I suggest working on [Assignment 1](90_Assignment_1.md)!
