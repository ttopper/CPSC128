# Summary: Selection using `if`

We have seen three ways of using the `if` statement
to_select_statements to execute.

One possibility is that we have a statement (simple or compound) to
execute conditionally. The construct to use is:

    if test-expression:
        true-statement

A second possibility is that we want to select one of two statements to
execute. In this case the construct is:

    if test-expression:
        true-statement
    else:
        false-statement

The third possibility is that we want to select one of a number of
mutually exclusive statements to execute. In this case the construct is:

    if test-expression:
        true-statement
    elif test-expression:
        true-statement
    ...
    else:
        false-statement

with as many `elif` statements as required to cover all the
possibilities, and the `else` statement usually reserved for catching
errors (specifically invalid values).
