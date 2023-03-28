# Compound Statements and Indentation

The syntax for `if` offered previously says that
the `if`, `elif` and `else` statements can be followed by a single
statement. But what if a single statement isn't enough to get the job
done? What if several statements will be required? Python's solution to
this is simple: just indent all the statements the same amount beneath
the `if`/`elif`/`else` statement. The result is a single *compound
statement*. The word compound simply indicates that the statement
contains several individual sub-statements. As long as the group of
statements are all indented the same amount they will be treated as a
single block or chunk and all be executed. Indentation is encouraged in
almost all modern programming languages to enhance readability, but
Python goes a step further and_requires_it. The next program we
consider illustrates compound statements.
