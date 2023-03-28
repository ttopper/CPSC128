# Encapsulation

The first benefit of OOP is that it allows for_encapsulation_ This
just means that an object encapsulates (or hides) how it operates from
the code that invokes it. We have benefitted, for example, by being able
to use Python's lists and dictionaries without having to worry about
how they are implemented internally. That's because they_abstract_the
behaviour to encapsulate their functionality and hide the implementation
details from us.

Encapsulation is necessary in OOP so objects can interact with each
other without needing to know the details of how each other operates. In
fact complete encapsulation allows for an object type to be rewritten
and dropped into a working program without any of the other program
components needing to be aware of the change.

This is not as magical as it might sound. If the next version of Python
changes the internal storage of dictionaries we will never know as long
as it behaves the same as the current implementation and our programs
keep working. As programmers got used to this their attention was drawn
to the importance of object interfaces, since as long as the interface,
or behaviour, is maintained, the implementation can be changed at will.
Some languages, including Python, have features or practices that allow
class interfaces to be formally specified. The programmer's focus then
is on "programming to the interface".
