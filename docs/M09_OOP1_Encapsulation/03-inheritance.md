# Inheritance

Experience creating objects soon showed programmers that many objects
shared features, e.g. several might have text blocks, or creation dates,
or screen positions, and they realized that they could further reduce
the amount of new code they had to write if they could reuse existing
code by having one type of object _inherit_ behaviour and properties
from another. Then if the ancestor's behaviour or properties were
updated the descendant would instantly inherit the improvements. This
can lead to large hierarchies of object types; some define thousands of
object types. To give you a flavour of a type hierarchy here is a
medium-sized inheritance hierarchy for a Python-based internet
application development platform:

![A class
hierarchy.](03_UIClassHierarchy.png)

Inheritance hierarchies are easiest to read bottom up. For example, if
we begin at the lower right the chart above tells us that
a `FlexTable` is a kind of `HTMLTable` which is in turn a kind
of `Panel` which is a kind of `Widget` which is a kind of `UIObject`.
What this means is that if we improve our code for `Panel`s, then `Widget`s
and `UIObject`s will instantly and transparently inherit these
improvements as well without us having to modify their code at all.
