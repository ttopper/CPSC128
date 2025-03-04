# a8_2.py
#
# A group of functions claiming to return the largest of
# the three values they are passed.
#
# Tim Topper
# CPSC 128
# Fall 2012

def biggest_a(a, b, c):
    '''returns the largest of the three values passed.'''
    big_one = a
    if b>a:
        big_one = b
    else:
        big_one = c
    return big_one

def biggest_b(a, b, c):
    '''returns the largest of the three values passed.'''
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c

def biggest_c(a, b, c):
    '''returns the largest of the three values passed.'''
    m = a
    if b>m:
        m = b
    if c>m:
        m = c
    return m

def biggest_d(a, b, c):
    '''returns the largest of the three values passed.'''
    def max(i, j):
        if i>j:
            return i
        else:
            return j
    return max(a, max(b, c))

def biggest_e(a, b, c):
    '''returns the largest of the three values passed.'''
    if a>b:
        temp = a
    elif b>a:
        temp = b
    else:
        temp = c
    return temp

def biggest_f(a, b, c):
    '''returns the largest of the three values passed.'''
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c

# You should use the following code to help you test
# the functions above.
# FNS is a list of lists. Each interior
# list contains a function and the name of the function.
FNS = [[biggest_a, 'biggest_a'], [biggest_b, 'biggest_b'],
       [biggest_c, 'biggest_c'], [biggest_d, 'biggest_d'],
       [biggest_e, 'biggest_e'], [biggest_f, 'biggest_f']
      ]

# Loop through the list FNS
# assigning the function to fn and its name to name.
for (fn, name) in FNS:
    print('Testing', name)
    # Put your tests here.
    # Form: print fn(a, b, c), 'Right answer'
    # Here's an example:
    print(fn(2, 1, 3), '=> Should be 3')
    print(fn(-5, 0, 5), '=> Should be 5')
