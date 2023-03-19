# shelves.py
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
if 'Kernighan' in quotefile:
    print("yes")
quotefile.close()
