# Object-Oriented Programming

So far we have been doing **procedural, object-based programming**.

In **procedural programming** the programmer specifies
the _procedure_ to follow to solve a problem. As you have discovered,
this procedure consists of a series of step-by-step instructions and
must be specified quite precisely. Although some large programs are
procedural, e.g. the Linux kernel and the Apache web server, the larger
they become the more difficult they are to compose. Large procedural
programs tend to become fragile, and it can be difficult to reuse the
code in them.

Our programming became **object-based** when our procedures began to
operate on objects. Object operations came with their own jargon of
objects, methods and messages. For example when we write

```python
    a_list.append('Tom')
```

we are invoking the `append` _method_ of the list _object_ `a_list`. We
might also say we are sending the
object `a_list` the _message_ `append`. Objects package data (e.g. the
data inside `a_list` above) and the code to operate on it (e.g.
the `append` method) together into convenient units that are easy to
use, and to **reuse**.

In **Object-oriented programming** (OOP) we go beyond using pre-existing
classes and learn how to create new classes of our own. This gives us
the ability to extend the basic types Python provides. Wish Python
provided `dice` and `playing_cards` in addition to numbers and strings? Just
add them to the language by defining new classes for each. Along with
this ability comes a new perspective on program building. Rather than
focussing on the procedural specification of what has to be done, OOP
views the execution of a program as an interaction between objects that
send messages to each other. In response to these messages the objects
carry out (internal) processing and retain state (store results). The
emphasis in object-oriented programming is on the design and coding of
these objects.

OOP comes with even more impressive jargon than object-based
programming. The three key aspects of OOP
are _encapsulation_, _inheritance_, and _polymorphism_. The ideas are not
as difficult as their forbidding names suggest and this module and the
next two are essentially long explanations with examples of these three
concepts. To get started though, here are brief explanations of these
concepts to introduce them to you and give you a general idea of what
they are about.
