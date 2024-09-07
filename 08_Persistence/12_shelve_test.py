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
