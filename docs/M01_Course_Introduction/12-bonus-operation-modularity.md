# Bonus Operation: Modularity

The six commands we have seen so far are logically sufficient to write
any program. But in pragmatic terms another is required. As programs
become large it becomes more and more difficult to work on them, because
there are too many interconnected parts to think about at once. What's
needed is a way to break a large program up into smaller pieces, each of
which can be developed in isolation of the others. These small pieces
are generically called modules. As a rough guide, many programmers
believe that no module should be more than a page long, i.e. about 50
lines. Beyond a page it becomes too hard to think about, and more errors
are made.

(Aside. How large can programs get? Thousands of lines is typical.
Hundreds of thousands and millions is common. Windows 10 for example
consists of around 50,000,000 lines of code, the google chrome browser has 35 million lines, and as of 2020 the
Linux kernel contains around 27,800,000 lines of code.)

In Python, modularization is enabled by using functions (via
the `def` statement), classes (via the `class` statement) and modules
(each Python program file is a module).
