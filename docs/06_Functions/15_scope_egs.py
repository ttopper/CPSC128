# scope_egs.py
#
# A program to demonstrate how Python picks between local and global variables.
#
# Kate Chatfield-Reed
# Winter 2023

print('Example 1: Local variable')
def f():
    x = 1
    print('Inside x is', x)
f()
print('Outside x is', x) # Error! Comment this line out once you understand why it is an error.
print()

print('Example 2: Global variable')
x = 1
def f():
    print('Inside x is', x)
f()
print('Outside x is', x)
print()

print('Example 3: Local variable hides global variable inside function')
x = 1
def f():
    x = 2
    print('Inside x is', 2)
f()
print('Outside x is', x)
print()

print('Example 4: Lots of hiding')
x = 1
def outer():
    x = 2
    def inner():
        x = 3
        print('Here in inner x is', x)
    inner()
    print('Here in outer x is', x)
inner() # Error! Comment this line out once you understand why it is an error.
outer()
print('Out here x is', x)

print('Example 5: Hiding the built-in len')
def len():
    print('I am not the real len')
len()