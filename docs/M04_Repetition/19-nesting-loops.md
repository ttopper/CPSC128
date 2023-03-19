# Nesting loops

This code is an example of nested loops:

![Nested print loops in Python.](19_nested_loops.png)

The general pattern here is,

    while test1:
        while test2:
            statement

The key thing to be aware of is that the inner while loop (the one
with *test2*) does **all** of its iterations for **each** of the
iterations of the outer while loop (the one with *test1*).

Note that there is no limitation that stops us at two while loops. For
example it is quite common in image processing operations to have four
nested loops. An outer pair that is responsible for considering each
pixel in the image, and an inner pair that processes that pixel in the
context of its neighbouring pixels.
