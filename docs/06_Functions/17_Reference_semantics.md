# Object destruction: Garbage collection* using reference counting

The other thing to note is that the assignment `lst[1] = lst[0]` not
only causes `lst[1]` to refer to `'Tom'` like `lst[0]` does it also
triggers the destruction of the object `'Tim'`. It does so because
Python uses *reference counting* to decide when an object can safely be
destroyed and the memory it is using reclaimed. Reference counting
garbage collection is based on the insight that once the number of
references to an object declines to 0 that object can never be accessed
by a program, therefore it is safe to destroy it. This happens
to `'Tim'` when the last reference to it (`lst[1]`) is removed.

This is also what happens to local variables in functions when the
function ends: as the local names are deleted the reference counts to
the objects drop to 0 and they can be destroyed (unless they are passed
back by a `return` statement which creates a reference to them from a
name in the calling function).

In terms of our diagrams an object's reference count is the number of
arrow heads pointing to it. At the end of the previous code fragment the
reference count of `'Matt'` is 1, and the reference count of `'Tom'` is
3.

With practice these semantics will become second nature, but at first
you may find it necessary to draw diagrams like those above when
debugging your code.

------------------------------------------------------------------------

* Memory management (the creation and deletion of memory structures,
including objects), was the bane of C and C++ programmers' lives. If
you did not carefully destroy objects once they were no longer needed
you created a memory leak, so called because the amount of memory your
program used slowly but steadily increased (since you weren't
reclaiming memory), making it seem like your system was slowly leaking
available memory. Java was the first widely successful language to make
memory management automatic. That meant that programmers could create
objects and that the system would automatically determine when it was
safe to reclaim them. This reclamation process goes by the colourful
name *garbage collection*. There are numerous ways of determining when
given memory can safely be reclaimed; reference counting is just one of
them.
