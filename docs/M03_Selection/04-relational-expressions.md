# Relational Expressions

The test expressions used in Python are relational expressions, and more
specifically Boolean expressions. Relational expressions test the
relation between quantities and produce a Boolean value,
either `True` or `False`*. Python provides the relational operators

    <        <=        ==        !=        >=        >

The two on either end should be easy to interpret. They are,
respectively, less than (`<`), less than or equal to (`<=`), greater
than or equal to (`>=`) and greater than (`>`). The two in the center
are not as easily recognized. The first, `==`, tests for equality. Why
not just use a single equals sign? Because the equals sign, `=`, is
already taken: remember that `=` is the assignment operator. The second
expression, `!=`, is used to test for inequality (or "not equals").
Here are some examples of simple relational expressions.

    x < 27.8
    age >= 65
    temp != max

Try them out in the Python shell.

Python also provides logical operators that can be used to build
compound relational expressions, usually referred to as Boolean
expressions. The logical operators are,

    and
    or
    not

An `and` relation is only `True` if *both* its arguments are `True`.
An `or` relation is `True` as long as *at least one* of its arguments
is `True`. The `not` operator negates its argument. Consider the
following example:

    age >= 20 and age < 30

This expression will only be `True` if the value of the
variable `age` is greater than or equal to 20 **and** it is also less
than 30. Thus the entire expression is `True` when, for example, age is
24, but `False` when it is 12 (because this makes the first
relation `False`), and also when it is 62 (because this makes the second
relation `False`).

    age >= 20 or income < 18.45

This expression is `True` when either the value of `age` is greater than
or equal to 20, or the value of `income` is less than 18.45, or both.

    not tested

This expression is `True` when the value stored in `tested` is `False`,
and `False` when the value stored in tested is `True`.

------------------------------------------------------------------------

* The values `True` and `False` are Boolean constants in Python in the
same way that 1 and -5 are numerical constants. Note however that while
there are an infinite number of numerical constants there
are *exactly* two Boolean constants: `True` and `False`.
