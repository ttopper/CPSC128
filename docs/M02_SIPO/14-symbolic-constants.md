# Symbolic Constants 

A second improvement is possible. Looking at our program we see that several calculations are performed more than once, i.e. (24 * 60 * 60) and (60 * 60). There should be a way to avoid the unnecessary recalculation, and there is. All we have to do is to calculate the quantities and store them so we can reuse the pre-calculated quantity. We could store them in a variable, but the quantity shouldn't change, so it would be wise to prevent it from changing if we can.

A second small concern is that it may not be clear to a someone reading our program (say someone maintaining it, or even ourselves rereading it a few months later) what the quantity 60 * 60 is.

Python has a convention we will adhere to to help deal with these issues. We will calculate our reused values once near the top of the program and give them names in all caps to indicate that these values are intended to remain unchanged.

    SECS_PER_DAY = 24 * 60 * 60
    SECS_PER_HOUR = 60 * 60
    SECS_PER_MINUTE = 60

    days = tot_seconds // SECS_PER_DAY
    remainder = tot_seconds % SECS_PER_DAY
    hours = remainder // SECS_PER_HOUR
    remainder = remainder % SECS_PER_HOUR
    minutes = remainder // SECS_PER_MIN
    remainder = remainder % SECS_PER_MIN

Notes:

- By convention constants are given capitalized names. This makes them stand out, and serves as a cue for people reading the program to the fixed nature of the quantity.

- These quantities are called symbolic constants, because we get to label them symbolically, i.e. we get to name them. The advantage of naming them is increased readability. Readers may not know what 24*60*60 is but SECS_PER_DAY will be meaningful to most.

Putting all these changes together and adding the declarations, overhead, and some instructions gives us the following complete program.

    # s2dhms.py -- converts a time in seconds to
    # its equivalent in days, hours, minutes and seconds.
    #
    # CPSC 128 Demonstration Program
    #
    # Kate Chatfield-Reed, Winter 2023

    SECS_PER_DAY = 24 * 60 * 60
    SECS_PER_HOUR = 60 * 60
    SECS_PER_MINUTE = 60

    # Input.
    print("=====================================================")
    print("     Seconds to Days, Hours, Minutes and Seconds")
    print("-----------------------------------------------------")
    print()
    print("This program converts a number of seconds to its")
    print("equivalent in days, hours, minutes and seconds.";)
    tot_seconds = int(input("Enter the number of seconds now (e.g. 116529): "))
    print()

    # Processing.
    days = tot_seconds // SECS_PER_DAY
    remainder = tot_seconds % SECS_PER_DAY
    hours = remainder // SECS_PER_HOUR
    remainder = remainder % SECS_PER_HOUR
    minutes = remainder // SECS_PER_MINUTE
    remainder = remainder % SECS_PER_MINUTE

    # Output.
    print(tot_seconds, "seconds =", days, "days,", hours, "hours,",)
    print(minutes, "minutes and", remainder, "seconds")

Notes:

- Note the effect of the trailing comma in the second last line. Try removing it and see how the output changes. How would you describe what this comma does?

- Note the blank print() statements, i.e. print() statements with no items in the brackets, used to output blank lines.

## Summary

Symbolic constants can be used to avoid repeating calculations
unnecessarily and to increase readability. They are identified by being
given names in ALLCAPS.
