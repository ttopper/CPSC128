# Reusing Functions

Now that we've written some reusable functions dealing with playing
cards the question arises as to just how we go about reusing them.

One way to reuse them would be to open the program file containing them
and copy and paste the functions (and the
constants `SUITS` and `FACE_VALUES`) into our working program file. But
what if we later improve these functions? Then we'd have to recopy and
repaste them. The same would apply if (God forbid!) we found a bug that
we had to fix in one of these functions. Then we'd have to remember all
the programs into which we'd copied and pasted them and replace the
buggy versions with the new ones. It would be nice if that copying and
pasting could be automated somehow so that code always benefited
automatically from improvements to our functions.

Well it turns out that automatically copying and pasting code is tricky
and thus unreliable. Instead programmers have found the best way to
reuse code is to have a way to include the contents (all or just some)
of one file in another. Python does this using modules and
the `import` command. We have already used `import` to get at functions
in the `math` and `random` modules. Now we will see how to use it to get
at functions we have written in our own programs.
