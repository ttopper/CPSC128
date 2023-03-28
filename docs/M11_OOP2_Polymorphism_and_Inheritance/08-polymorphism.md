# Polymorphism

Polymorphism allows the same syntax to be used with objects of different
types, or equivalently, polymorphism occurs when the meaning of a method
or operator depends on the type of object(s) it is applied to. For
example the `+` symbol triggers three different operations in the code
below each determined by the objects surrounding it, i.e. by its
context.

    x = y + 5
    salutation = 'Mr.' + last_name
    t = [3, 7] + [6, 2]

From the developer's perspective the question is how we can make our
object types trigger appropriate behaviour. Or to put it another way,
can we give_our_objects the same status and abilities as Python's
built-in objects? The answer is yes. All we need to do is to define some
special methods for our classes. This is all we have to do because when
Python encounters an operator in an expression it looks at the objects
on each side of it (for a binary operator) and then calls a method from
their class definitions *if one is provided*. For example when it
encounters a + sign it checks to see if the object on the left hand side
of the + sign has a method called \_\_add\_\_. If it does, it invokes
it.

Nor is this limited to binary arithmetic operators. We saw earlier that
the print command just looks for an `__str__` method to invoke.
Similarly square brackets for list indexing look for a method
called `__getitem__`.

In all, Python defines dozen of available "hooks" for operations. The
more of them you define for your classes the more they will seem like
built-in classes. To see the full list of possibilities see [section 3.4
of the
documentation](http://docs.python.org/reference/datamodel.html#special-method-names).
What we will do in this module is to work with a small handful of them
to get a feel for the issues involved.
