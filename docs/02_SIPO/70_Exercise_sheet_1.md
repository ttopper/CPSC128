# Tutorial 1

1. Look at the following code fragments. Each one has one small problem that will cause an error or give the wrong output. Using what you know about python math operations and SIPO programming to identify an correct the problems.

a)
```python
distance_km = int(input('Enter a distance in kilometers: ')
distance_km * 1.6 = distance_miles
print(distance_km,'kilometers is the same as', distance_miles, 'miles')
```

b)
```python
distance = duration * speed
speed = int(input('Enter the speed in km: '))
duration = int(input('Enter the duration of time in hours: '))
print(distance)
```

c)

```python
name = input('Enter your name: ') 
print('Hello name')
```

2. Look at the following and think about how well the code is written. The program works correctly, so I want you to focus on the clarity of the variable names and the comments included. Look at the [marking guide](https://ttopper.github.io/CPSC128/00_Preparing/14_Marking_scheme/) and think about what grade you would give to this code. Make some notes on the feedback you would give to this student to help them improve their grade.

```python
# annual_income.py
# This program calculates how mush someone maeks


w = float(input('Enter how much you make: '))
h = float(input('Enter your hours: '))

total = w * h * 52

print('You make',total, 'dollars.')
```

3.  ### Trivialities

    We only know enough Python commands to write simple programs so far,
    but we do need to practice using what we've got so ... write a
    program that produces sessions like this one:

```plaintext
    Useless Trivia Generator v0.01
    ==============================
    How old are you? 28
    And how many pounds do you weigh? 165
    Did you know that you're 196 in dog years!
    But you're also over 883008000 seconds old.
    Did you know that on the moon you would weigh only 27.5 pounds?
    But on the sun, you'd weigh 4471.5 pounds (but not for long!).
```

Some facts that might be helpful to you in writing your program:

-   There are seven dog years in each calendar year.
-   There are 60 seconds in a minute, 60 minutes in an hour, 24
    hours in a day, and (at least) 365 days in a year.
-   Things weigh 1/6th as much on the moon as they do on the surface
    of the earth.
-   Things weigh 27.1 times as much on the surface of the sun as
    they do on the surface of the earth.


