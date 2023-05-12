# Version 2

If you emulated Version 1 precisely you will have noticed that you did a
lot of unnecessary work when the mark was 96. Your simulation should
have revealed that the grade passed the test in the first `if` statement
and output "A+". So far so good. Next though it went on to evaluate
the second `if` test, and the third, and the fourth and so on, all the
way down the list. But, once we determined that the grade was an A+ we
didn't have to do any of the other tests, because if the grade is
between 95 and 100, it can't be in any of the other ranges.

The way to avoid the unnecessary tests is to perform the tests following
the first one with `elif` statements. The structure of the code is:

    # Version 2.
    print(" ... ") # Instructions to user
    grade = float(input( " ... " ))
    if grade >= 95 and grade <= 100:
        print("A+")
    elif grade >= 86 and grade <= 94:
        print("A")
    elif grade >= 80 and grade <= 85:
        print("A-")
    # ...
    # and so on down to
    # ...
    elif grade >= 50 and grade <= 54:
        print("D")
    elif grade >= 0 and grade <= 50:
        print("F")
    else:
        print("Error: The grade must be between 0 and 100.")

Before we analyze this code, again verify that it works by simulating
its execution for a couple of sample numerical grades, e.g. 65 and 93.

This is an improvement over the original code. For one thing we have
eliminated the final error condition test completely: if the mark
doesn't fall in any of the specified ranges then it must be out of
range. But it also, on average does fewer tests. Consider, if the grade
is an A+, e.g. 96, it does only the first `if` and skips the rest. Of
course if the grade is an F it still does all the tests as it bumps its
way down the list. So it never does more tests and often does fewer. On
average (if the average grade is in the middle of the list) it will do
half as many if tests as the first version, making it twice as fast.

However, careful examination reveals that we still have more tests than
are required, and those unnecessary tests waste processor time and slow
down the program. What are the unnecessary tests? This time it's not
unnecessary tests being evaluated, it's unnecessary comparisons being
performed inside the tests.

    print(" ... ") # Instructions to user
    grade = float(input("..."))
    if grade > 100 or grade < 0:
        print("Error: The grade must be between 0 and 100.")
    elif grade >= 95:
        print("A+")
    elif grade >= 86:
        print("A")
    elif grade >= 80:
        print("A-")
    # ...
    # and so on down to
    # ...
    elif grade >= 50:
        print("D")
    elif grade >= 0:
        print("F")

(Again verify that the code works by "running it' in your mind with a
couple of typical values.)

This code represents a significant improvement over the second version
on two counts: it is more efficient, and it is easier to read. It is
easier to read because the relational expressions are shorter. It is
more efficient because where the previous version had 33 relational
operators (3 for each of 11 letter grades) this one has 3 + 10 = 13 (2
for the initial range check followed by one for each possible letter
grade except the last). This is less than half as many, a significant
improvement in any field (imagine a runner completing a race in half the
previous time, or a car whose mileage suddenly doubled!).
