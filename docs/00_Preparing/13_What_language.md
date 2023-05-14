# What Language?

## I've read the course description but I still don't know what language we will be using.

Careful readers will have noticed that the particular language the
course will use is not mentioned in the course description. This is by
design, not accident. Like fashions programming languages come and go
but the fundamentals change much more slowly. This course is decidedly
about the fundamentals, and hopefully the course description will
outlast current language fashions.

## No, really, what language will we be using?

We'll be using the language [Python](http://www.python.org).

## Why Python?

Python was designed to be a teaching language. This means that concepts
can be introduced one at a time, and lots of messy details delayed until
they are needed.

Industrial-strength languages like Java and C++ are good for developing
huge software systems, after all that's what they were designed for,
but they are problematic as first languages. For instance in Java to
write a very simple program, one that just displays the message "Hi"
on the screen, the code would look like this:

    class myfirstjavaprog
    {  
            public static void main(String args[])
            {
               System.out.println("Hi!");
            }
    }

and in C++ it would look like this:

    #include <iostream>
    int main()
    {
        std::cout << "Hi!\n";
    }

As you can see in Java and C++ there are a lot of concepts that have to
be explained (e.g. in Java: `class`, `public`, `static`, `void`, `main`,
`String`, `arg[]`, `System.out.println`) before one can write even a
very simple program.

In Python the program is just:

    print( "Hi!" )

which is self-explanatory.

If you're still not convinced think about learning to fly. Your goal
might be to fly 747s or F14s but you don't learn to fly on those planes
because they are too complicated, and too unforgiving of mistakes. You
learn to fly in a small Cessna. Once you have mastered the principles of
flying you move on and upwards. Interestingly the charms of Python are
so seductive that some programmers never leave it (it is for example one
of only three internally supported languages at Google).

(It's also free in both[*](#L107) senses and available across most
platforms.)

## And there's this... 😀

![](13_Xkcd_on_python.png)

------------------------------------------------------------------------

[*]"free as in beer" and "free as in speech" see
[Wikipedia](http://en.wikipedia.org/wiki/Gratis_versus_Libre) or just
Google "free as in beer".
