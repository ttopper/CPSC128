# Naming Values

What names _can_ you choose for the values you store? The names must
begin with a letter, but can be followed by any sequence of letters,
numbers, and the underscore character `_`.

A more important question is what names _should_ you choose for your
values? The names you choose should be,

-   descriptive of the values they refer to, to enhance program
    readability,
-   short, for convenience,
-   all lowercase, to adhere to Python convention.

The computer doesn't care what you call them. For example our program
would run as well if we changed the variable names to be,

```python
x = int(input())
y = (x - 32) * 5 / 9
print(y)
```

or even,

```python
fish_guts = int(input())
corn_flakes = (fish_guts - 32) * 5 / 9
print(corn_flakes)
```

I, however, care very much what you call them, as will the other
programmers you work with, and even you when you come back to modify
your code in six months, or six years. The two versions above are
respectively, obscure, and downright misleading, and would be graded
accordingly!
