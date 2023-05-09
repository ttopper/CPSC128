# Finding the Standard Library Modules

Python is often referred to as a “batteries included” language because
its standard library offers so much functionality you rarely have to
download other, separate, tools. The standard library modules also offer
the student programmer a rich resource of high quality code to study and
learn from. Sometimes though it is not obvious where to find the
standard library files on your computer. Fortunately you can ask Python
to tell you where they are. First `import` the `sys` module, then look
at its `path` attribute. This attribute is a list of all the directories
Python will search in the order they will be searched when you look for
a module. For example,

    >>> import sys
    >>> sys.path
    ['//home/Profiles/kchatfieldreed/Documents/CPSC128_Intro_OO/Programs',
     'C:\\Program Files\\Python311\\Lib\\idlelib',
     'C:\\Program Files\\Python311\\python311.zip',
     'C:\\Program Files\\Python311\\Lib',
     'C:\\Program Files\\Python311\\DLLs',
     'C:\\Program Files\\Python311',
     'C:\\Program Files\\Python311\\Lib\\site-packages']
    >>>

Here we can see that it will begin by looking in my current
directory `//home/Profiles/kchatfieldreed/Documents/CPSC128_Intro_OO/Programs` and
then work through the remainder of the list. The search stops when the
first match is found.

Note: The bulk of the libraries are found in the `lib` directory and its
descendants, on this machine that means the fourth
entry `C:\\Program Files\\Python311\\Lib`.

Note that since this path is available through introspection it can be
changed dynamically by a running program — a useful trick in some
situations.


