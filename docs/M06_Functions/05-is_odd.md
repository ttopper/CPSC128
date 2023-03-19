# is_odd()

Now consider writing a function `is_odd`.

We could do so by basing it *on our approach* in `is_even`,

    def is_even(n):
        if n%2 == 0:
            return True
        else:
            return False

so `is_odd` could be written as,

    def is_odd(n):
        if n%2 != 0:
            return True
        else:
            return False

An alternative would be to base it *on `is_even` itself* (rather than
just reusing the same approach). Taking this tack we would
write `is_odd` as,

    def is_odd(n):
        return not is_even(n)

which just calls `is_even` and negates its return value. Most
programmers would prefer the second version even though in
it `is_odd` is no longer a standalone function, but is instead dependent
on `is_even`. Why? Well the second version involves writing less code
and the result is shorter. More importantly if someday a better way of
determining if a number is even is found only one function needs to be
rewritten (`is_even`) and the other (`is_odd`) automatically benefits
from the improvement. We are unlikely to find a better way of testing
for evenness, but there are many other computationally intensive
processes where better methods are continually being developed and the
fewer places in our code we need to implement the new methods to take
advantage of them the better.
