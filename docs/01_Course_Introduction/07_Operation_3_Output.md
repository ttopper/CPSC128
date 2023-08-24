# Operation #3: Output

Our statements so far,

```python
speed = int(input())
duration = int(input())
distance = duration * speed
```

have calculated the quantity `distance` based on the input values
of `speed` and `duration`, but we don't know what it is because that
value exists only inside the memory of our computer. To see it we need
to output it where we can look at it. The most common output command in
Python is the `print` statement. To print the value of `distance` we
would simply use the command,

```python
print(distance)
```

We can also print the values of expressions, e.g.

```python
print(2**8 - 1)
```