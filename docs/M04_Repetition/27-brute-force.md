# Brute Force

> *When in doubt, use brute force.* ~ Ken Thompson, Bell Labs

Thompson's advice has two aspects. The first is that some problems that
are difficult for humans to solve because we are not quick at processing
and are unreliable when doing repetitive operations are easy for
computers to solve because those weaknesses of ours are their strengths.
In this sense he is advising us to play to the computer's strengths.

The second sense is that often we try to be too clever when solving
problems and to overthink our solutions when simple brute force could
get the job done.

We'll look at a few types of problems in this module that lend
themselves to brute force solutions.

-   The first are simulations where we have the computer painstakingly
    model some process step-by-step, and do so not just once but many
    times so that we can estimate the likelihood of various outcomes.
-   The second are in some sense purely computational problems that
    arise in numerical processing, e.g. in cryptography. We will begin
    just by searching for certain kinds of numbers. Since there may be a
    lot of numbers to consider and each one requires some computation
    this is well suited to repetitive computer processing.
-   Long before sudoku, newspapers featured various mental puzzles, one
    type of which were known as cryptarithms. These can be solved by
    brute force, but there can be so many possible solutions to consider
    that refining our brute force approach is necessary.
