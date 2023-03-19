# Documentation

The final step in producing a complete program is to document our
program. For a large project documentation includes in-program comments
explaining the code, various charts showing the program structure, a
user manual, etc. However for now we will constrain ourselves to
in-program comments.

Two types of comments are usually included: meta-comments, and internal
comments. Meta-comments document who created the program, and when and
why they did so. Internal comments on the other hand are used to
document the internal workings of the program. As a rule of thumb you
should comment any statements that you had to puzzle over to figure out,
on the assumption that when you reencounter them in six months you will
again have to puzzle them out.

Both types of comments are produced by the same simple mechanism: the
computer ignores any text on a line that follows a hash mark outside of
a string literal, i.e. a `#`. Thus a `#` at the start of a line
instructs the computer to ignore the entire line, and a `#` part way
along a line instructs the computer to ignore the remainder of the line.
(Fine print: unless the `#` is enclosed in a string literal.)

Our first program is short and straightforward enough to get by without
internal comments (the variable names are descriptive, and the output
statements make clear what the program is intended to do). So we will
simply add a small banner of meta-information at the top. The result is
our first complete Python program.

    # f2c.py -- converts a temperature in Fahrenheit to its equivalent in Celsius.
    # CPSC 128 Example program
    # Kate Chatfield-Reed, Winter 2023

    print("This program converts temperatures from Fahrenheit to Celsius.")
    print("Enter a temperature in Fahrenheit (e.g. 10) and press Enter.")
    temp_in_f = int(input("Temperature in Fahrenheit: "))
    temp_in_c = (temp_in_f - 32) * 5 / 9
    print(temp_in_f, "degrees Fahrenheit =", temp_in_c, "degrees Celsius.")
