# Object Types 1: ints and floats

In which we consider the types of objects for the first, but definitely not the last, time. Python version 3 automatically converts ints to floats if needed. However, in some cases it is still important to know the difference.

5 is not the same as 5.0

## The Issue

Recall our program to convert from Farenheit to Celsius:

    # f2c.py -- converts a temperature in Fahrenheit to its equivalent in Celsius.
    # CPSC 128 Example program
    # Kate Chatfield-Reed, Winter 2023
    #
    print("This program converts temperatures from Fahrenheit to Celsius.")
    print("Enter a temperature in Fahrenheit (e.g. 10) and press Enter.")
    temp_in_f = int(input("Temperature in Fahrenheit: "))
    temp_in_c = (temp_in_f - 32) * 5 / 9
    print temp_in_f, "degrees Fahrenheit =", temp_in_c, "degrees
    Celsius."

In this example I assumed that the input would be an integer (or round number). If you enter the input 2.2, it will give an error because I told the computer to expect only an integer.

    # f2c.py -- converts a temperature in Fahrenheit to its equivalent in Celsius.
    # CPSC 128 Example program
    # Kate Chatfield-Reed, Winter 2023
    #
    print("This program converts temperatures from Fahrenheit to Celsius.")
    print("Enter a temperature in Fahrenheit (e.g. 10.0) and press Enter.")
    temp_in_f = float(input("Temperature in Fahrenheit: "))
    temp_in_c = (temp_in_f - 32) * 5 / 9
    print(temp_in_f, "degrees Fahrenheit =", temp_in_c, "degrees Celsius.")

The necessary changes are shown in red. Try running this version of the program and see how the output changes. Is it what you wanted? If not stay tuned for an update coming soon to a module near you.

The change let the computer know that you could enter any number. It should work if you enter 5, 5.0, or 2.5 as your starting number. Make sure that you pick the number type that is needed for each situation. The key thing to realize here is that 5 and 5.0 are not the same thing.

## Type conversions

You can convert an object of any type to an integer using the class name of integers, int, as a function, e.g. `int(4.3)`. It didn't work in the program above because we were converting a string to a number. Similarly you can convert an object to a floating point number using the class name float as a function, e.g. `float(4)`. Using a class name in this way invokes the class' constructor, a function that tries to build an object of the specified type.

One common occasion where the two types are combined is in finding the average of a set of real numbers. Here the sum will be a floating point value, but the count of the number of values is best represented by an integer. When we divide the sum by the count, we are combining a floating point value with an integer.

## `int` or `float`?

In many problems either `int`s or `float`s can be used depending on the
type of output required. When it is not clear which choice is best the
following insight and guidelines may be helpful. The insight is that
most numbers arise as the result of either measurements (the length,
duration, weight \... of something), or counts (the number of students,
cars, bacteria, problems, \...). The resulting guidelines are to:

-   Prefer floating point values for measurements.
-   Use integers for counts.

Note that the second guideline is stricter than the first.
