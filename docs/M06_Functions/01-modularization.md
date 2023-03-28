# Modularization

The first module in this course introduced the six essential imperative
programming operations. There were three simple statements,

_input_
:   gets a value from the input stream and stores it in memory.

_processing_
:   processes/combines/manipulates values stored in memory and stores
    the result in memory

_output_
:   sends a value to the output stream

and three control structures,

_sequential processing_
:   in which statements are executed one at a time in sequence

_selection_
:   in which one group of statements or another, but not both, are
    executed

_repetition_
:   in which a group of statements is executed repeatedly

I also introduced one “bonus” structure: _modularity_. Many modern
computer scientists would take issue with the _bonus_ characterization
and argue that modularization is perhaps the most fundamental structure
provided by modern programming languages.

I do not disagree with their assessment. I refer to the other control
structures as _essential_ because it is logically impossible to write
all programs without each and every one of them. It is possible to write
a program without modularization, but extremely difficult, and the
resulting program if it was ever successfully written and tested would
be very difficult to modify or maintain.

Why is modularization so important? Because it enables us to

1.  **reduce the complexity** of our programs, while at the same time
    allowing us to
2.  **create reusable chunks of code**.

We reduce complexity by using a divide and conquer strategy, i.e. taking
a large program and dividing it into smaller, more manageable, pieces.
If we choose our pieces carefully, we can accumulate a collection of
modules that are reusable. This saves us time on future projects by
allowing us to avoid reinventing the wheel.

Reducing complexity is important because there is a (small) limit to the
number of things the human brain can think about at once. Cognitive
psychologists often peg the capacity of short term memory at 7 plus or
minus two items, because people can on average only recall between 5 and
9 items from a sequence they are given to remember. This biological
limitation makes it very difficult to think about problems involving a
dozen units, much less ones involving hundreds of disparate parts. One
way of organizing the complexity of a large system is to divide it into
hierarchies that only have a handful of items on any given level. This
division is modularization. Dividing a problem well, i.e. in a way that
makes the problem simpler to solve, is a skill that is developed through
practice and by studying examples.

As we tackle different programming problems and projects we will build
up a storehouse of modules. If we modularize our problems well we will
develop a toolkit of reusable modules that we can use in the future to
avoid rewriting code we have written before. Choosing modules for
reusability is more objective than choosing them to reduce complexity:
the main rule is to make each module do one thing, and only one thing,
well, and to avoid side effects. We avoid side effects by having each
module restrict its actions to as narrow a domain as possible.

Python enables modularization through the use of

1.  **functions**,
2.  **classes**, and
3.  **modules**.

In this module of the course we will consider the first and third of
these, i.e. functions and modules. The second item, classes, is the
subject of the entire third part of the course.
