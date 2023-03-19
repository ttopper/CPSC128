# Writing functions: Syntax summary

Here is a template for writing Python functions:

    def function-name( parameter-list ):
        ...
        ... function-body
        ...
        return expression
        ...
        return expression

And here are a couple of guidelines:

-   We *prefer* to have a single `return` expression as the last line of
    the function. If this guideline is followed then other programmers
    know where to look to find out what value is returned, and don't
    have to hunt through the function trying to spot all the return
    points. Having said that this is a preference *not a requirement*.
    Some code really is cleaner with multiple `return`s spread
    throughout the function, but this is unusual enough that you should
    do a quick mental check to verify that it is preferable.

-   If you do not include a `return` statement the value returned will
    the special value `None`, but it is better to be explicit that this
    is your intention by placing a blank `return` statement in the
    function than by just not having one (because then other programmers
    will not waste brain cycles wondering if you intended to
    return `None`, or forgot to include a `return`).
