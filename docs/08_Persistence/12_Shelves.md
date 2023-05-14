# Shelves

A `shelve` ([Official documentation](http://docs.python.org/library/shelve.html)) is like a dictionary that is stored on disk. (The name continues the canning theme begun with `pickle`). The dictionary values can be any object that can be pickled. Retrieval is fast because the dictionary keys are hashed for fast retrieval.

Here is an example that stores quotations into a `shelve` on disk. The comments should make it self-explanatory.

```python
# shelve_test.py
import shelve
# First here are a couple of quotes to work with.
b = ['Kent Beck', 'Optimism is an occupational hazard of programming: testing is the treatment.']
k = ['Brian Kernighan', 'Controlling complexity is the essence of computer programming.']
# Now let's create an in-RAM dictionary with the quotes in it.
quotes = {}
# Add the quotes to the dictionary keyed by last name.
quotes['Kernighan'] = k
quotes['Beck'] = b
# Now let's display what we have:
print('Here's the dictionary:')
print(quotes)
print()
print('Here it is again by looping through it:')
for person in quotes.keys():
print(quotes[person])
print()
# Now let's create a shelve and put the quotes in it.
# Like a file we open it, but unlike with a file
# opening a shelve is non-destructive so you can reopen it as often
# as you want.
quotefile = shelve.open('quotes')
# Notice how the access syntax mirrors the dictionary syntax above.
quotefile['Kernighan'] = k
quotefile['Beck'] = b
quotefile.close()
# The quotes should be stored on-disk now.
# Let's reopen the shelve and display the quotes.
quotefile = shelve.open('quotes')
print('Here's the content of the shelve:')
# Notice how similar this is to working with the in-memory dictionary above.
for key in quotefile:
print(key, ':', quotefile[key])
quotefile.close()
```

The example shows how to store and retrieve data with the shelve, but what about deleting a stored item? Just use `del dictionary[key]` or in the specific example above we could use `del quotefile['Beck']` to remove the Kent Beck quote.

## A small gotcha

Brian Kernighan is a very smart guy and has said many memorable things. What if we add a second quote by him to the shelve? Well if we use the same key, i.e. his last name `Kernighan`, it will replace the existing quote. What to do? One view is that last name was not a good choice for the key because it is not unique to the items being stored, i.e. two items can have the same key. Another is that it is a fine key, but the values in the dictionary should be a list of the quotes by Brian Kernighan not a single list element giving one quote, i.e. the entry should be a list of lists. In either case we probably want to be able to tell if we already have any quotes by him already and we can do that using the shelve's `in` method,

```python
if 'Kernighan' in quotefile:
   # deal with it...
```


## A bigger Gotcha: Shelves update on assignment not mutation<br>

> **WTH!?**"_Shelves update on assignment not mutation._"

Shelves are mostly very easy to use, but there is one common gotcha to be aware of when you use them and that is that <q>shelves update on assignment not mutation</q>. There have I said it enough times? Now I'll explain it.

## The problem: Surprise!

Consider the following transcript carefully,

```plaintext
>>> s = shelve.open('test_shelve')
>>> s['bob'] = 42
>>> s['liz']=[31]
>>> s.close()
>>> s = shelve.open('test_shelve')
>>> for key in s:
print(key, ':', s[key])

bob : 42
liz : [31]
>>> s['bob'] = 43
>>> s['liz'][0] = 30
>>> s.close()
>>> s = shelve.open('test_shelve')
>>> for key in s:
print(key, ':', s[key])

bob : 43
liz : [31]
```

The thing to notice here is that `s['bob']` was changed (from `42` to `43`), but that `s['liz']` was **not** (it's still just `[31]`). **WTH?** The reason is that `s['bob']` was _assigned to_, but `s['liz']` was only _mutated_, that is the contents of the list `s['liz']` were changed, but `s['liz']` itself still refers to the same list object. That object's contents may have changed but Python has no (easy and efficient) way of noticing that. So `s['bob']` was assigned to and therefore updated but `s['liz']` was only mutated and so was not updated, just like the phrase says: "Shelves update on assignment not mutation".

How can we force `s['liz']` to be updated?

## Solution 1

Open the shelve with the option `writeback=True`,

```plaintext
>>> s = shelve.open('test_shelve', writeback=True)
>>> s['liz'][0] = 1
>>> s.close()
>>> s = shelve.open('test_shelve')
>>> for key in s:
print(key, ':', s[key])

bob : 43
liz : [1]
```

_But_ listen to the official documentation:

> If the optional writeback parameter is set to True, all entries accessed are cached in memory, and written back at close time; this can make it handier to mutate mutable entries in the persistent dictionary, but, if many entries are accessed, **it can consume vast amounts of memory**for the cache, and it can make the close operation **very slow**since all accessed entries are written back (there is no way to determine which accessed entries are mutable, nor which ones were actually mutated). [*](http://docs.python.org/lib/module-shelve.html)

## Solution 2

Mutate the object via a temporary name assigned to it and then reassign the temporary name to the shelve (i.e. keyed) name. In other words use a temporary name to force an assignment to the keyed name happen:

```plaintext
>>> s = shelve.open('test_shelve', writeback=True)
>>> tmp = s['liz']
>>> tmp[0] = 2
>>> s['liz'] = tmp
>>> s.close()
>>> s = shelve.open('test_shelve')
>>> for key in s:
print(key, ':', s[key])

bob : 43
liz : [2]
```

<br>

## Summary

**Fact**: _Shelves update on assignment, not mutation_.

**Implication**: This means that changes to shelve members that contain
mutable types, e.g. lists and dictionaries, are not automatically
updated to disk.

**Solution 1**: Open the shelve with the option `writeback` set
to `True`.

**Drawback**: If the shelve is open for long a large number of cached
shelve objects will accumulate and need to be written to the shelve file
when it is closed.

**Solution 2**: Mutate the shelve object via a temporary name assigned
to it and then reassign the temporary name to the shelve (i.e. keyed)
name.

**Drawback**: It takes some care to do this consistently.

**Conclusion: Use Solution 2.**
