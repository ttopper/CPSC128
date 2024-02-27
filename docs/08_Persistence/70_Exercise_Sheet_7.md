# Exercise

1.  ### Text file practice

    Write a module containing two functions. When run, the module
    should prompt the user for a filename and a number of lines (let's
    refer to it as `n`) and then call each function in turn with these
    parameters.

    a.  The function `head` should return a list containing the first
        `n` lines of the file.

    b.  The function `tail` should return a list containing the last `n`
        lines of the file.

    Make a test at the bottom to show the output of running the module, 
    it might look like this:

```plaintext
    Name of file to test with: pooh.txt
    Number of lines to display: 3

    head says the first 3 lines are:
    The more it snows
      (Tiddely pom),
    The more it goes

    tail says the last 3 lines are:
     How cold my toes
      (Tiddely pom),
     Are growing.
```

Since the file could be very long you will **not** want to read the
whole thing into memory as a list of lines... Here is a short file to
test with [pooh.txt](90_pooh.txt)