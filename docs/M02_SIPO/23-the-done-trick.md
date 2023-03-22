# The `done` trick

If you run your Python program by double-clicking its program icon then
after it displays its output it immediately closes the terminal window,
probably before you could actually see what the output was. One way to
prevent this rapid closure is to add a statement like this one at the
end of your program,

```python
    done = input("Press Enter to exit.")
```

This works because it instructs the computer to await input from the
user, so the program freezes (halts execution) while it waits.
