# Translate the Algorithm into Python

The next step in developing our program is to look at what we did by
hand and identify the corresponding computer commands. Here are the
numbered steps we identified:

1.  I began by writing down the amount to be converted, 40.

2.  Next I subtracted 32 from it.

3.  Then I multiplied the difference by 5/9.

4.  The result was 4, meaning that 40 degrees Fahrenheit is equivalent
    to 4 degrees Celsius.

Now we'll translate these English commands into their Python
equivalents.

Step 1 above, getting the amount to be converted, is equivalent to the
input operation,

```python
    temp_in_f = int(input())
```
The next two operations (steps 2 and 3) can be combined into one
processing (or assignment) statement as follows,

```python
temp_in_c = (temp_in_f - 32) * 5 / 9
```
Finally the last step (4) is equivalent to an output statement,

```python
print(temp_in_c)
```
If we write these three statements down in sequence we have the core of
a very small Python program.

```python
temp_in_f = int(input())
temp_in_c = (temp_in_f - 32) * 5 / 9
print(temp_in_c)
```
To check that this seems reasonable let's mentally trace its
step-by-step operation on our functional computer model.

1.  The first statement instructs the processor to watch the input
    channel for a value, store it and label it `temp_in_F`. As users we
    place the value into the input stream by typing it on the keyboard
    and then pressing the Enter key.

2.  The second statement has the processor fetch the value
    named `temp_in_F`, subtract 32 from it, multiply the result by 5 and
    divide that result by 9. The final value is stored and
    labelled `temp_in_C`.

3.  The final statement instructs the processor to fetch the value
    named `temp_in_C` and send it to the output stream. This makes it
    appear on our screen.

The final step is to enter, run and test our program.
