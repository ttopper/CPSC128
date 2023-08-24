# Output Formatting

To get output like this,

![.](24_output_formatting_0.gif)

instead of this,

![.](24_output_formatting_1.gif)

Build a `print` statement with the
string,

![print formatting example in
python](24_print_format.png)

[Below is the output of each print
statement.]{style="font-size: 0.9375rem;"}\

1.  ![.](24_output_formatting_1.gif)

2.  ![.](24_output_formatting_0.gif)

3.  ![.](24_output_formatting_0.gif)

4.  ![.](24_output_formatting_0.gif)

The formatting codes used in the second print statement are derived from
those originally used by the language C and now also used by the
languages C++, AWK, Perl, and PHP among others. Each format placeholder
has the form,

```plaintext
%[optional arguments]letter
```

The % sign indicates the beginning of a placeholder.

Although all of these options are valid in Python 3 we will be using option 
4, the f-string, because that is currently considered best practice. I also 
think it the easist to read!

The letter indicates the desired format:

  Letter  | Format
  :------:|------------------------------
  d       | decimal integer
  o       | unsigned octal integer
  x       | unsigned hexadecimal integer
  f       | floating point
  s       | string
  
All these take an optional argument specifying the width of the field in
which the value should be displayed, e.g.

![.](24_output_formatting_5.gif)

The floating point code takes an additional argument specifying the
number of digits to display to the right of the decimal point, e.g.

![.](24_output_formatting_6.gif)

Note that if a field width is narrower than the value to be displayed
the field is enlarged to fit the value, e.g.

![.](24_output_formatting_7.gif)

this can be helpful when you want to insert numerical values into
sentences (rather than some tabular format), e.g.

![.](24_output_formatting_8.gif)

If you need to display multiple values enclose the interpolating
variables in parentheses, e.g.

![.](24_output_formatting_9.gif)


There is much more to string formatting than is shown here. For the
details start with the Python Library Reference [Section
7](https://docs.python.org/3/tutorial/inputoutput.html).
More details can be found in the Gnu AWK manual [Section
5.2](https://www.gnu.org/software/gawk/manual/html_node/Print-Examples.html)
