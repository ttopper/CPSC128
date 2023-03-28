# `if` Syntax, in Detail

The syntax of the `if` statement is,

    if test-expression1:
        true-statement1
    [elif test-expression2:
        true-statement2]
    ...
    [else:
        false-statement]

Or in words, the `if` statement consists of the
keyword **`if`** followed by a *test expression*, followed by a
statement that will be executed if the test expression is `True`,
optionally followed by the keyword `elif` followed by a second test
expression and a second statement which will be executed if the second
text expression is `True`, and so on until an optional `else` is reached
the statements following which will be executed only if_all_the
test-expressions above it were `False`. Note that the statements
following `if`, `elif` and `else` statements **must** be indented.
