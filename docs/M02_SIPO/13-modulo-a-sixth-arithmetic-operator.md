# Modulo: A Sixth Arithmetic Operator

The first improvement we can make to our program is to take advantage of an operator Python (and most programming languges) provides to calculate remainders. Everyday arithmetic gets by with addition, +, subtraction, -, multiplication, *, division /, and integer division // but remainders occur in a host of common algorithms so programming languages provide a fifth arithmetic operator in addition to the common four. The fifth operation is named modulo and is denoted in Python by the symbol %. It returns the remainder of a division. For example `17 // 5` is 3 because 5 goes into 17 three times, but what if we need to know how much was "left over"? We use the modulo operator like this: `17 % 5` to get 2, the remainder when 17 is divided by 5.

We wrote instructions of our own to calculate the remainder above but using modulo will be more compact, i.e. make our program shorter, and may well be more efficient (because the language writers will have implemented it as efficiently as possible), and will at any rate not be less efficient.

Using modulo we can rewrite the processing portion of our program like this:

    days = tot_seconds // (24*60*60)
    remainder = tot_seconds % (24*60*60)
    hours = remainder // (60*60)
    remainder = remainder % (60*60)
    minutes = remainder // 60
    remainder = remainder % 60

## Summary

The remainder of a division can be found using the modulo
operator `%`. This operation is useful for packaging a large
quantity into smaller packages, e.g. a large number of seconds into
packages of days, hours, minutes and seconds. This sort of packaging
turns out to be a common operation in many kinds of problems.
