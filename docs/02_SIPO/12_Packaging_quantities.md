# Packaging Quantities

## The problem

We want to write a program that does the opposite of our last program,
i.e. instead of taking a time in days, hours, minutes and seconds and
calculating the equivalent number of seconds, we want to take a large
number of seconds and find the equivalent number of days, hours,
minutes, and seconds.

For example, we would like to divide 200,000 seconds into the equivalent
number of days, hours, minutes, and seconds.

## Packaging Quantities: Do it by hand

Our first step is to figure out how many days worth of seconds this is.
So we divide 200,000 by `(24*60*60)`:

```plaintext
days = 200,000 / (24 * 60 * 60) = 2
```

Note that the result is two because we do an integer (not "decimal")
division; what we want to know is how many whole days worth of seconds
will go into 200,000.

Now we calculate how many seconds are left over after taking out two
days worth of seconds.

```plaintext
remainder = 200,000 - 2 * (24 * 60 * 60) = 27,200
```

Next we want to calculate how many hours worth of seconds this is. We do
this similarly to the days calculation above.

```plaintext
hours = 27,200 / (60 * 60) = 7
```

And find the remainder,

```plaintext
remainder = 27,200 - 7 * (60 * 60) = 2,000
```

Finally we calculate the number of minutes,

```plaintext
minutes = 2,000 / 60 = 33
```

and the remainder of that is the leftover seconds,

```plaintext
seconds = 2,000 - 33 * 60 = 20
```

So 200,000 seconds is equivalent to 2 days, 7 hours, 33 minutes and 20
seconds.

In terms of input, processing and output:

- the **input** is the number of seconds (200,000),

- the **processing** consists of several steps to find the number of days,
hours, minutes and seconds, including intermediate steps to find the
remainders along the way, and

- the **output** is the number of days, hours, minutes and seconds.

## Translate into Python

A literal translation of our manual steps,

```plaintext
days = 200,000 / (24*60*60) = 2
remainder = 200,000 - 2*(24*60*60) = 27,200
hours = 27,200 / (60*60) = 7
remainder = 27,200 - 7*(60*60) = 2,000
minutes = 2,000 / 60 = 33
seconds = 2,000 - 33*60 = 20
```

into Python might look like this (we used the // symbol to tell python
to use integer division):

```python
tot_seconds = int(input("Enter the number of seconds: "))
days = tot_seconds // (24*60*60)
remainder = tot_seconds - days * (24*60*60)
hours = remainder // (60*60)
remainder = remainder - hours * (60*60)
minutes = remainder // 60
remainder = remainder - minutes*60
print(tot_seconds, "seconds is", days, "days,")
print(hours, "hours,", minutes, "minutes and")
print(remainder, " seconds.")
```

Notes:

-   This is just the core of the program and the instructions are
    minimal, for now ...
-   Note that the final value output is `remainder`, do you understand
    why?

As written (with the addition of — you already know this right? —
interface and documentation) this program would run and calculate the
answer correctly, but a couple of improvements are possible.
