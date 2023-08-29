# Aside: *is-a* versus *has-a*

We have used both is-a and has-a relations already but without drawing
attention to the distinction between them. The is-a relationship
typifies inheritance, in which we can say of each subtype or descendant
class that it "is a" superclass. For instance consider the small
hierarchy below,

```python
class Person:
    ...
class Student(Person):
    ...
class Employee(Person):
    ...
class Instructor(Employee):
    ...
class Administrator(Employee):
    ...
```

In this case we can say that _a `Student` **is a** `Person`_ and that _an
`Employee` **is a** `Person`_.

Similarly we can say that _an `Instructor` **is an** `Employee`_ and
that _an `Administrator` **is an** `Employee`_.

Now since an Instructor is an Employee and an Employee is a Person it
follows that through inheritance _an `Instructor` **is a** `Person`_ and
similarly that _an `Administrator` **is a** `Person`_.

Let's add some more classes and show some of the attributes.

```python
class Date:
    ...
class CourseList:
    ...
class Person:
    def __init__(...):
        self.birthdate = ...
    ...
class Student(Person):
    def __init__(...):
        self.courses = ...
    ...
class Employee(Person):
    ...
class Instructor(Employee):
    def __init__(...):
        self.courses = ...
    ...
class Administrator(Employee):
    ...
```

Here we can see some has-a relationships. _A `Person` **has
a** `birthdate`_ which is presumably of type `Date`. Thus since all the
classes listed below `Person` are also `Person`s they all have `birthdate`s
too and we can say _everyone **has a** `Date`_.

We can also see that both Students and Instructors have
a `courses` attribute (of type `CourseList`, take my word for it) so we
can say that _a `Student` **has a** `CourseList`_ (of the ones s/he takes)
and that _an `Instructor` **has a** `CourseList`_ (of the ones s/he
teaches).
