# What will it look like onscreen?

> Our first consideration of user interface and user interaction.

As you've seen when you ran the program, the disappointing answer is
that not much appears on-screen. When we run the program it will watch
the input channel and wait for a value to appear there. Specifically, it
will wait for the Enter key on the keyboard to be pressed, and then look
in the keyboard buffer to see what keys were pressed before the Enter
key. From these keypresses it will attempt to construct an integer value
which it will store in `temp_in_f`. It will not instruct us to type
anything; we must just remember to do so. When we do type, we will see
the characters we type appear on-screen, and have until we press the
Enter key to Backspace over the line making changes. Pressing the Enter
key forwards the line we have typed to the processor.

If we have typed 40, then after it has calculated the equivalent
temperature on the Celsius scale it will display 4 beneath our 40 on the
screen. So the screen might look something like this:

```plaintext
    40
    4.444444444444445
```

Hardly inspiring, and no casual user would realize they were supposed to
type anything, nor, on the off chance they did type a number, would they
realize what the output was.

(This is a good chance to experience another error message. Press <kbd>F5</kbd>
again to run your program and instead of typing a number type the
word `help` and then press the Enter key.)

To make our program more useful we need to provide instructions to the
user, and explain the output. We do this by inserting extra print
statements into the program. For example:

```python
print("This program converts temperatures from Fahrenheit to Celsius.")
print("Enter a temperature in Fahrenheit (e.g. 10) and press Enter.")
temp_in_f = int(input("Temperature in Fahrenheit: "))
temp_in_c = (temp_in_f - 32) * 5 / 9
print(temp_in_f, "degrees Fahrenheit =", temp_in_c, "degrees Celsius.")
```

Now the screen will look like this:

```plaintext
This program converts temperatures from Fahrenheit to Celsius.
Enter a temperature in Fahrenheit (e.g. 10) and press Enter.
Temperature in Fahrenheit: 40
40  degrees Fahrenheit =  4.444444444444445  degrees Celsius.
```
Still not earth-shattering, but a marked improvement.

There are quite a few things to note in this small example:

-   `print` statements aren't limited to printing values that are in
    memory, they can also print messages (formally: string literals). To
    do so just enclose the string of characters you would like to
    display on-screen in quotes. This means the
    statements `print("rate")` and `print(rate)` do very different
    things. The first one prints the letters `r`, `a`, `t`,
    and `e` on-screen. The second one looks for a value named `rate` and
    displays the value (and if it can't find one displays an error
    message!). Try adding and removing some of the quotes in the sample
    program above and see what happens.

-   You can combine values and string literals in one print statement,
    as the last line of the program does, to produce more meaningful
    output. To do so just separate successive items with commas. The
    commas are required.

-   An input statement can include a string literal that acts as a
    prompt to the user, in which case the string will be displayed
    and_then_the computer will watch for input from the user. This
    gives you a way to instruct the user. Note that the string must be
    enclosed in quotes. If your prompt is too long to fit inside the
    parentheses just put some of it into print statements preceding the
    input statement.

-   To get a sense of how precision matters in programming try removing
    the space after the colon (:) in the input prompt and re-running
    your program. Do you notice how the on-screen appearance is
    different? You should, and you should prefer it with the space.

-   I've added some blank lines into the program to visually separate
    the I, P and O blocks of the program to make it easier to see the
    program's structure. I do this for me and for you; Python could
    care less.

Using string literals judiciously it is possible to create clear input
instructions, and clearly (if modestly) formatted output.
