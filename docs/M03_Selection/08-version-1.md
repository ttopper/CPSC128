# Version 1

We would like to write a program that accepts a numerical grade and
outputs a letter grade. Clearly the program will use one or
more `print` statements to display instructions to the user, and
an `input` statement to get the numerical grade to be converted. Then it
will need to output one of the 11 possible letter grades depending on
the numerical grade. That is obviously a selection step, because we are
selecting one of 11 possible output statements. The question is how to
structure `if` statements to implement that step.

If someone asked us what the table says we might reply, "It says if the
numerical grade is between 95 and 100, then the letter grade is an A+.
If the numerical grade is between 86 and 94, then the letter grade is an
A." and so on. A literal translation of this into Python would result
in the following code.

    # Version 1.
    print(" ... ") # Instructions to user
    grade = float(input("..."))
    if grade >= 95 and grade <= 100:
        print("A+")
    if grade >= 86 and grade <= 94:
        print("A")
    if grade >= 80 and grade <= 85:
        print("A-")
    # ...
    # and so on down to
    # ...
    if grade >= 50 and grade <= 54:
        print("D")
    if grade >= 0 and grade <= 50:
        print("F")
    if grade < 0 or grade > 100:
        print "Error: The grade must be between 0 and 100."

This code would work. Play computer and try it yourself starting with
numerical grades of, say, 65 and 96. But although it works, it performs
unnecessary tests and so is slower than it could be.
