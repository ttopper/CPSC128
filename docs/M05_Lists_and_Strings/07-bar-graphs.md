## The Problem

What we have is a list of numbers, say [3, 7, 8, 10, 14, 14, 11, 11, 9, 6, 2] and we would like to draw a bar graph of them like this,

```
***
*******
********
**********
**************
**************
***********
***********
*********
******
**
```

## Version 1

The pseudocode to do so might look like this,

```plaintext
for each value in the list
    draw a bar of value asterisks
```

which could be translated into the following Python,

```python
data = [3, 7, 8, 10, 14, 14, 11, 11, 9, 6, 2]
for datum in data:
    print(datum * '*')
```

Note:

* The use of `*` as a string repetition operator.
* The difference between the two asterisks in the second line: the first is an operator; the second is a string literal.

## Version 2

The graph doesn't look like much, even for a text graphics chart. Let's dress it up one step at a time. First we'll display the data value in front of the bar:

```python
data = [3, 7, 8, 10, 14, 14, 11, 11, 9, 6, 2]
for datum in data:
    print(datum, datum * '*')
```

To produce,

```plaintext
3 ***
7 *******
8 ********
10 **********
14 **************
14 **************
11 ***********
11 ***********
9 *********
6 ******
2 **
```

## Version 3

This is a little better, but the bars don't all start in the same place. We need to place our data values in fixed length fields. For this data we could do this,

```python
data = [3, 7, 8, 10, 14, 14, 11, 11, 9, 6, 2]
for datum in data:
    print("{:2d}".format(datum), datum * '*')
```

and get this,

```
3 ***
 7 *******
 8 ********
10 **********
14 **************
14 **************
11 ***********
11 ***********
 9 *********
 6 ******
 2 **
```

but a width of 2 wouldn't work well for larger values. It would be better to find the largest value in the list and then use the length of that value as the field width. We can do that using the built-in function `max` to find the field width and then converting that value to a string[^*] and using the `len` function to get the length of the string. We can then use that output field width to build an appropriate format string. The resuting code,

```python
data = [3, 7, 8, 10, 14, 14, 11, 11, 9, 6, 2]
OFW = len(str(max(data))) # Output Field Width.
FORMAT = "{:" + str(OFW) + "d}" # Format string.
for datum in data:
    print(FORMAT.format(datum), datum * '*')
```

produces this graph,

```plaintext
 3 ***
 7 *******
 8 ********
10 **********
14 **************
14 **************
11 ***********
11 ***********
 9 *********
 6 ******
 2 **
```

## Version 4

But now we have added a potential confusion: are those the values of the bars or the labels of the data? Let's add data labels, and put the values into parentheses so our output will look like this,

```plaintext
 2s ( 3) ***
 3s ( 7) *******
 4s ( 8) ********
 5s (10) **********
 6s (14) **************
 7s (14) **************
 8s (11) ***********
 9s (11) ***********
10s ( 9) *********
11s ( 6) ******
12s ( 2) **
```

Here's the Python code to do it,.

```python
data = [3, 7, 8, 10, 14, 14, 11, 11, 9, 6, 2]
labels = ['2s', '3s', '4s', '5s', '6s', '7s',
          '8s','9s', '10s', '11s', '12s']
OFW = len(str(max(data))) # Output Field Width.
DFORMAT = "({:" + str(OFW) + "d})" # Data format string.
label_lens = map(len, labels) # List of label lengths.
LFW = max(label_lens) # Label Field Width.
LFORMAT = "{:" + str(LFW) + "s}" # Label format string.
for i in range(len(data)):
    print(LFORMAT.format(labels[i]), DFORMAT.format(data[i]), data[i] * '*')
```

Notes:

* For more on the `map` function in line 8 see [The `map` function](14-the-map-function.md).
* The loop discipline is now index-based because we need to loop through the two lists (data and labels) at the same time picking one item from each list.

## Reading Code

It may surprise you to learn that working programmers spend more time reading code than writing it. There's reading their own code of course, but they almost always work on large systems made up of code from many programmers, and since their code needs to work with the existing code, they need to be able to read that existing code. When you work in a production environment you have the use of intelligent editors and debuggers that help you trace through code to see what it is doing, and we will indeed use IDLE's debugger later. For now though we can use the original poor man's debugger: `print` statements. To understand the code above, paste it into a file and then place an appropriate `print` statement after each line so you can see the values that are being calculated, e.g.

```python
data = [3, 7, 8, 10, 14, 14, 11, 11, 9, 6, 2]
labels = ['2s', '3s', '4s', '5s', '6s', '7s', '8s',
          '9s', '10s', '11s', '12s']

OFW = len(str(max(data))) # Output Field Width.
print('OFW = ', OFW)

DFORMAT = "({:" + str(OFW) + "d})" # Data format string.
print('DFORMAT = ', DFORMAT)

label_lens = map(len, labels) # List of label lengths.
print('label_lens = ', label_lens)

LFW = max(label_lens) # Label Field Width.
print('LFW = ', LFW)

LFORMAT = "{:" + str(LFW) + "s}" # Label format string.
print('LFORMAT = ', LFORMAT)

for i in range(len(data)):
    print(LFORMAT.format(labels[i]), DFORMAT.format(data[i]), data[i] * '*')
```

This will produce the output,

```plaintext
OFW =  2
DFORMAT =  ({:2d})
label_lens =  [2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3]
LFW =  3
LFORMAT =  {:3s}
 2s ( 3) ***
 3s ( 7) *******
 4s ( 8) ********
 5s (10) **********
 6s (14) **************
 7s (14) **************
 8s (11) ***********
 9s (11) ***********
10s ( 9) *********
11s ( 6) ******
12s ( 2) **
```

enabling you to see what the calculated values are.

## Version 5

There is one last refinement worth working on. We were fortunate that all the values in our data set were relatively small, because if any of them had been very large the bars would have wrapped across multiple lines on our screens. The final refinement is to scale the data values if they are larger than the screen is wide so that there will be no wrapped lines. Here's the code to do that. Take the time to understand what it is doing (add in `print` statements if necessary!).

```python
SCREEN_WIDTH = 60
data = [300, 700, 800, 1000, 1400, 1400, 1100, 1100, 900, 600, 200]
labels = ['2s', '3s', '4s', '5s', '6s', '7s', '8s',
          '9s', '10s', '11s', '12s']

OFW = len(str(max(data))) # Output Field Width.
DFORMAT = "({:" + str(OFW) + "d})" # Data format string.

label_lens = map(len, labels) # List of label lengths.
LFW = max(label_lens) # Label Field Width.
LFORMAT = "{:" + str(LFW) + "s}" # Label format string.

MAX_BAR = SCREEN_WIDTH - (OFW+2) - LFW - 2

max_datum = max(data)
if max_datum > MAX_BAR:
    scaled_data = []
    for datum in data:
        scaled_data.append(datum * MAX_BAR // max_datum)

for i in range(len(data)):
    print(LFORMAT.format(labels[i]), DFORMAT.format(data[i]), scaled_data[i] * '*')
```

Notes:

* Note the new `SCREEN_WIDTH` constant at the top. This is the total width available for the graphic display.
* `MAX_BAR` is the width of the screen leftover after accounting for the space used by the labels and data values.
* 2 is added to `OFW` in the calculation of `MAX_BAR` to account for the ()s around the data value.
* The final 2 is subtracted to account for the spaces Python automatically inserts into the output after each argument.
* `max_datum` is used to avoid multiple calls to the `max` function each of which would have to traverse the list looking for the maximum value.
* `scaled_data` contains the data scaled into the range `0` `...` `MAX_BAR`

The corresponding output is,

```
 2s ( 300) **********
 3s ( 700) *************************
 4s ( 800) *****************************
 5s (1000) ************************************
 6s (1400) ***************************************************
 7s (1400) ***************************************************
 8s (1100) ****************************************
 9s (1100) ****************************************
10s ( 900) ********************************
11s ( 600) *********************
12s ( 200) *******
```

<br>

## Summary

While our final output isn't fancy it is a helpful visualization of the
original tabular data and it allowed us to experience several common
programming issues.

More important is the approach demonstrated through the 5 versions of
this program: The method of _successive refinement_. It is much easier
to start with a simple program that works and gradually refine it, than
to try and design the ideal system at the outset. Later in this course,
and even more so in its successor, we will discuss when it is appropriate
to use big up front design, and when it is appropriate to use agile
design[^*].

---

[^*]: See [Type Conversions](13-built-in-type-conversions.md) for more on this.

[^*]: To read more about this Google "agile software development".
