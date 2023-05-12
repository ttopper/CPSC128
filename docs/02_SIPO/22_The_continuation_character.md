# The Continuation Character

The lines in your Python programs should normally be kept "short"
where short means less than 80 characters long. This is usually
straightforward, but sometimes long expressions can be difficult to
format clearly and still fit on one line. In this case you can place a
continuation character at the end of the line to indicate to the Python
interpreter that it continues on the next line. Python uses the
backslash as its continuation character, e.g.

```python
    total = twonies * 2.0 + loonies*1.0 + quarters*0.25 + dimes*0.10 \
            + nickels*0.05 + pennies*0.01
```