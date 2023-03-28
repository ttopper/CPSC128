# Aside: Iterative Design

Most software design is iterative. This means first that we iterate from
general code to specific code gradually adding more detail on each pass
(iteration). It also means that we iterate or alternate between the
control code in the main routine and the code in the class definitions.

Did you notice the mistakes I made in my first pass at `Cave_System`s'
methods? We are moving back and forth (iterating) between the main
control code and the class definitions just so that we can spot these
misfits as early as possible so correcting them is easy. If we had done
a complete class hierarchy and only then tried to write the main routine
we would have "baked in" and expanded on these errors and they would
be harder to fix. In fact the temptation to write convoluted code to
deal with the shortcomings of our classes might be too hard to resist.
Similarly if we were to write our main routine in detail before
considering what classes we should use we would only end up with well
designed classes by sheer luck since they would not in fact have
been_designed_

So was there a mistake in my original class design? Sure. But the
iterative approach ensured that I caught it early when it was easy to
fix. So let's fix it by turning to the `Room` class.
