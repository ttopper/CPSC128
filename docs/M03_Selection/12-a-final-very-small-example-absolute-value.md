# A Final (Very Small) Example: Absolute value

For completeness we should consider the case where there is only one
action to be performed, but it only needs to be performed some of the
time. This arises, for example, when we need to make sure a value is
positive. Suppose, for example, that we have a value in a program that
should not be negative. If it is negative we want to make it positive.
There are two possibilities, but only one of them requires any action:

1.  If the number is already positive, we don't have to do anything.
2.  But if the number is negative we have to negate it to remove the
    negative sign.

The code to do this might look like:

    if value < 0:
        value = -value

This code simply demonstrates that the `else` statement is optional and
not a required element of selection.
