# SIPO Summary

Using input, processing (via assignment), and output statements we can
write sequential or SIPO programs. These programs have a standard
structure containing three parts:

1.  A block of statements to get the necessary input values from the
    user,

2.  A block of statements to process these values (typically to
    calculate new values based on them),

3.  And a block of statements to output the calculated values.

The number of statements in each block will vary, as will the particular
processing operations, but those three fundamental parts will always be
present. This program structure can be represented using a flowchart as
follows:

<!-- ![.](11_IPO_flowchart.gif) -->

```mermaid
flowchart TD
    A(Begin Execution)
    B[/<b>Input</b> necessary values/]
    C[<b>Process</b> stored values,<br>i.e. perform calculations]
    D[\<b>Output</b> calculated values\]
    E(End execution)
    A --> B --> C --> D --> E
```