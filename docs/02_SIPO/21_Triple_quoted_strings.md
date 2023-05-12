# Triple Quoted Strings

Outputting long stretches of text using mulitple print statements is
awkward. To make it easier Python allows you to specify multi-line
output fragments using triple quotes, either single(') or double (").
So instead of,

```python
    print('This program converts a measurement of a tree's circumference into')
    print('an estimate of its diameter (assuming the tree to be circular in')
    print('cross-section).')
    print()
```

we can write,

```python
    print("""This program converts a measurement of a tree's circumference into
    an estimate of its diameter (assuming the tree to be circular in
    cross-section).
    """)
```

or

```python
    print('''This program converts a measurement of a tree's circumference into
    an estimate of its diameter (assuming the tree to be circular in
    cross-section).
    ''')
```

Later we will see that we can use string interpolation to use large
swaths of triple quoted strings as templates into which we insert
variable values to output e.g. entire web pages dynamically.
