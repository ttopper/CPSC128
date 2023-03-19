# How'd we do?

We are going to stop working on our Hunt the Wumpus game at this point,
but this isn't to say it is done. Quite apart from game features we
might add (see the assignment for some ideas), the OO design is not as
polished as it could be.

If you look again at the memory diagram of our objects you will again
see both solid and dotted lines. Generally* a direct reference (solid
line) is preferred to an indirect one (dotted line). There are some
dotted lines here we could replace with solid ones. For example
the `tunnels` attributes could be lists of direct references
to `Room` objects rather than lists of room numbers. This would simplify
the syntax of using them and is semantically more accurate, but it makes
initializing the cave system quite a bit trickier. Likewise, the hazard
and `Player` `location` attributes could contain direct references to
their respective `Room` objects rather than room numbers that have to be
used as indices to indirectly access the rooms, but there are some
initial complications in setting that up too. In sum our design may not
be as OOPy as it could be, but it is as OOPy as we had time and the
skills to make it.

------------------------------------------------------------------------

* The word generally here should signal to you that there are
situations in which the indirect references are preferred as indeed
there are, but you won't go wrong on the kinds of problems you will
encounter in this course preferring direct references.


