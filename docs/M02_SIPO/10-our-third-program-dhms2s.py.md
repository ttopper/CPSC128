# Our third program (dhms2s.py)

We'll finish by writing another program; one that takes several input
values instead of just one.

The problem is to convert a time given in days, hours, minutes, and
seconds to the equivalent number of seconds.

For example 1 day, 8 hours, 23 minutes and 11 seconds is (doing it by
hand) 1 × 24 × 60 × 60 + 8 × 60 × 60 + 23 × 60 + 11 = 116,591 seconds.
The calculation is based on the fact that each day has 24 hours, each
hour has 60 minutes, and each minute has 60 seconds.

The **input** is the number of days, hours, minutes, and seconds.

The **processing** is the calculation above.

And the **output** is the equivalent number of seconds.

The core (I say core because I am leaving out the documentation and some
interactive elements so you can better focus on what matters) of a
Python program to do this calculation might look like this,

    print("Enter your values now,")
    days = int(input("Enter days: "))
    hours = int(input("Enter hours: "))
    minutes = int(input("Enter minutes: "))
    seconds = int(input("Enter seconds: "))
    tot_seconds = days*24*60*60 + hours*60*60 + minutes*60 + seconds
    print("Total seconds is", tot_seconds)

It seems to work but there is one improvement that can be made. The
small improvement is that we can rewrite the processing statement so it
does fewer calculations. As it stands the statement,

    tot_seconds = days*24*60*60 + hours*60*60 + minutes*60 + seconds;

does 3 additions and 6 multiplications. If we factor the expression and
rewrite it as,

    tot_seconds = ((days*24 + hours)*60 + minutes)*60 + seconds;

we reduce the count of multiplications from 6 to 3: a significant
reduction.
