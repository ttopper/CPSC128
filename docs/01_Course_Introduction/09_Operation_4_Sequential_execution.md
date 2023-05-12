# Operation #4: Sequential Execution

Together our first four commands make a little program and illustrate
the fourth operation: sequential execution.

```python
speed = input()
duration = input()
distance = duration * speed
print(distance)
```

By default the computer executes statements in the order they are
presented, from first to last, top to bottom (the same order in which we
are used to reading). Note that the order can be crucial. Our program
will still work if we swap the first two statements, but most other
reorderings will produce errors. For example swapping the second and
third ones,

```python
speed = input()
distance = duration * speed
duration = input()
print(distance)
```

or the second and fourth ones,

```python
speed = input()
print(distance)
distance = duration * speed
duration = input()
```

or the third and fourth ones,

```python
speed = input()
duration = input()
print(distance)
distance = duration * speed
```

To understand why each of these other orderings results in an error try
stepping through the effects of the statements using a functional
diagram of a computer. If you do so precisely you will soon see the
problem created by each reordering. This ability to step through a
program precisely (or to play computer) is the key skill in debugging
programs.

It is also instructive to try running each of these programs in Python
(you'll see how to do this shortly) to see the error messages they
generate. You'll be seeing a lot of error messages this term, and until
you know what conditions create them they can appear inscrutable. So the
sooner you get to know them the easier it will be for you to debug your
own programs.

With the first three commands, and the default sequential execution
behaviour, we can write programs that gather input, process it, and
output results. But with only sequential execution they must always
process the input in the same way. These programs are calculator like:
You gather the numbers you need, process them and look at the answer. We
will refer to them as SIPO (Sequential Input, Processing, Output)
programs. This is the only type of program you will need to write for
the next module's assignment, but since there are only two more
fundamental operations I want to introduce them to you now. We'll look
at them in depth in Modules 3 and 4.
