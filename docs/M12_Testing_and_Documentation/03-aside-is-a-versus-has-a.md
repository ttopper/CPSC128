# Aside: *is-a* versus *has-a*

We have used both is-a and has-a relations already but without drawing
attention to the distinction between them. The is-a relationship
typifies inheritance in which we can say of each subtype or descendant
class that it "is a" superclass. For instance consider the small
hierarchy below,

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

In this case we can say that *a Student **is a** Person* and that *an
Employee **is a** Person*.

Similarly we can say that *an Instructor **is an** Employee* and
that *an Administrator **is an** Employee*.

Now since an Instructor is an Employee and an Employee is a Person it
follows that through inheritance *an Instructor **is a** Person* and
similarly that *an Administrator **is a** Person*.

Let's add some more classes and show some of the attributes.

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

Here we can see some has-a relationships. *A Person **has
a** birthdate* which is presumably of type Date. Thus since all the
classes listed below Person are also Persons they all have birthdates
too and we can say *everyone **has a** Date*.

We can also see that both Students and Instructors have
a `courses` attribute (of type CourseList, take my word for it) so we
can say that *a Student **has a** CourseList* (of the ones s/he takes)
and that *an Instructor **has a** CourseList* (of the ones s/he
teaches).
