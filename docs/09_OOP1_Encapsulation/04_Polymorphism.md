# Polymorphism

Programmers noticed another regularity among their objects: often many
of them needed to be able to respond to the same message, but by doing
somewhat different things. For example we _add_ items to a list, and to
a dictionary, and to a menu, etc. In this case we want all these object
types to be able to respond to an `add` message, i.e. to provide
an `add` method. Of course in Python we don't always know what type of
object a name refers to, `list[3]` could be another list, or a menu, or
a string, etc. The ability to be able to say `list[3].add(thing)` and
have the language interpreter figure out what to do is _polymorphism_
More technically it is the ability for an operation to trigger different
behaviours in different contexts. A concrete example we have seen of
this is the behaviour of the `+` operator: it _adds_ numbers,

```python
x = y + 5
```

*appends* strings,

```python
salutation = 'Mr.' + last_name
```

and_extends_lists,

```python
t = [3, 7] + [6, 2]
```

In each case the semantics of the `+` operator is different because the
operation performed depends on the types of the objects it is working
with.

When fully utilized, polymorphism allows us to add new object types to
the Python language. For example if we need to work a lot with invoices
we can define an invoice type that can be printed, added to, subtracted
from, multiplied by, iterated over etc. This ability to extend the
language allows it to be customized to suit any given problem domain and
has been a powerful driver for the adoption of object-oriented
programming.
