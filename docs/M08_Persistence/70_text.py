# crud_controller.py
import shelve
fname = input('What file of quotes would you like to work with? ')
db = shelve.open(fname)
over = False
while not over:
    print('''
    Actions
    -------
    c - create a quote to add to the collection
    r - retrieve a quote from the collection and display it
    u - update a quote in the collection
    d - delete a quote from the collection
    l - list all the items in the collection
    q - exit
    Your choice?''')
    choice = input()
    
    if choice == 'c':
        author = input('Who is the author of the quote? ')
        text = input('What did they say or write? ')
        lastname = author[author.rfind(' ')+1:]
        db[lastname] = [author, text]
        
    elif choice == 'r':
        pass
    
    elif choice == 'u':
        pass
    
    elif choice == 'd':
        pass
    
    elif choice == 'l':
        print('Here are the contents of the shelve', fname, ':')
        for key in db:
            print(key, ':', db[key])
            
    elif choice == 'q':
        over = True
        
    else:
        print('Not a valid choice!')
        
db.close()
"""

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
# crud_controller.py
import shelve
fname = input('What file of quotes would you like to work with? ')
db = shelve.open(fname)

# Forever
over = False
while not over:

    # Display the possible actions
    print('''
    Actions
    -------
    c - create a quote to add to the collection
    r - retrieve a quote from the collection and display it
    u - update a quote in the collection
    d - delete a quote from the collection
    l - list all the items in the collection
    q - exit
    Your choice?''')

    # Get the user's choice of action
    choice = input()
    
    # Execute the code corresponding to the chosen action
    if choice == 'c':
        pass       
    elif choice == 'r':
        pass   
    elif choice == 'u':
        pass   
    elif choice == 'd':
        pass  
    elif choice == 'l':
        pass            
    elif choice == 'q':
        over = True       
    else:
        print('Not a valid choice!')
        
db.close()


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


# life.py
universe = [ [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 1, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]
           ]
import pickle
f = open( 'pickled_universe.txt', 'wb')
pickle.dump(universe, f)
f.close()
f = open('pickled_universe.txt', 'rb')
u = pickle.load(f)
f.close()
print(u)

# read_coords.py
coords = []
fname = input('Name of file to read from? ')
f = open(fname, 'r')
for line in f:
    (x_string, y_string) = line.split()
    coords.append([int(x_string),int(y_string)])
f.close()
print('coords =', coords)


# write_coords.py
coords = [[12, 31], [75, 19], [28, 51]]
fname = input('Name of file to create? ')
f = open(fname, 'w')
for coord in coords:
    f.write(str(coord[0])+' '+str(coord[1])+'\n')
f.close()


# ip_extractor.py
fname = input('What file do you want to scan? ')
ip = input('What IP address do you want to scan for? ')
f = open(fname, 'r')
for line in f:
    if line.find(ip) != -1:
        print(line)


# file_read_3.py
f = open('text_file.txt', 'r')
lines = f.readlines()
print(lines)
f.close()


# file_read_2.py
f = open('text_file.txt', 'r')
s = f.read()
print('s is', len(s), 'characters long.')
print(s)
f.close()
"""