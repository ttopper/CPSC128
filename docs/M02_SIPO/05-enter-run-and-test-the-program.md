# Enter, run and test the program

The last step in writing our program is also the first where we actually
use the computer.

1.  Within IDLE choose File → New Window and type in our three statement
    wonder.

```python
    temp_in_f = int(input())
    temp_in_c = (temp_in_f - 32) * 5 / 9
    print(temp_in_c)
```
2.  Save the result (File → Save) into a file called `f2c.py`. Note how
    IDLE colourizes the program once it knows the file extension.

3.  Press <kbd>F5</kbd> to run your program. This will bring the Python shell
    window to the front where you will interact with your program.

4.  Type <kbd>4</kbd><kbd>0</kbd> and then watch what number appears. If it isn't spproximately 4 you've
    got a problem.

Step 4 is a test of our program but it isn't sufficient testing to be
confident our program will work correctly with all possible values. We
should try a couple of other known-correct values to be sure it works
correctly. In later programs I'll have much more to say about choosing
test values and testing procedures.

This is the core of our first Python program, but just the core. Now we
have to attend to several other important issues:

-   Naming values
-   What will we see on the screen when we run the program?
-   Documentation
