# The map() function

The `map` function (seen in [Bar Graph](07-bar-graphs.md))
can simplify some list processing. The command,

```python
map(fn, seq)
```

builds a new list from an existing one by applying the function `fn` to
every member of the sequence `seq`. For example if you have the list of
strings, `names = ['Tim', 'Mary', 'Stephanie', 'Bob']`, and want a list
of the lengths of those strings `map` is just the ticket. It creates a
`map` object that can be cast to a list:

```plaintext
>>> names = ['Tim', 'Mary', 'Stephanie', 'Bob']
>>> len_list = map(len, names)
>>> list(len_list)
[3, 4, 9, 3]
>>> 
```

`map` doesn't do anything magical it just replaces the loop
construction,

    len_list = []
    for item in names:
        len_list.append(len(item))

with a more compact, and less error-prone notation.

Some languages don't provide a `map` function in which case you may
want to write your own[^*]] since it's so handy.

---

[^*]: No you don't know how quite yet, but you'll see how in the very
next module!
