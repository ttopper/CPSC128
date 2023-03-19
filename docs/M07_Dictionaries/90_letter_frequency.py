# letter_frequency.py
# CPSC 128
# Winter 2013
# Tim Topper

def letter_frequencyA( text ):
    pass

def letter_frequencyB( text ):
    pass

def letter_frequencyC( text ):
    pass

if __name__ == '__main__':

    test_string = '''The most important single aspect of software development
        is to be clear about what you are trying to build.
        ~ Bjarne Stroustrup (creator of C++)

        As soon as we started programming, we found to our surprise that
        it wasn't as easy to get programs right as we had thought.
        Debugging had to be discovered. I can remember the exact instant
        when I realized that a large part of my life from then on
        was going to be spent in finding mistakes in my own programs.
        ~ Maurice Wilkes discovers debugging, 1949

        The programmer, who needs clarity, who must talk all day to a machine
        that demands declarations, hunkers down into a low-grade annoyance.
        It is here that the stereotype of the programmer,
        sitting in a dim room, growling from behind Coke cans, has its origins.
        The disorder of the desk, the floor; the yellow Post-It notes everywhere;
        the whiteboards covered with scrawl:
        all this is the outward manifestation of the messiness of human thought.
        The messiness cannot go into the program;
        it piles up around the programmer.
        ~ Ellen Ullman
    '''

    #########################
    # Test letter_frequencyA:
    #########################
    correct_result = [65, 11, 18, 29, 91, 15, 30, 41, 54, 1, 6, 26, 32, 52,
                      69, 18, 0, 61, 58, 82, 20, 5, 21, 1, 11, 1]
    # Note that the continued statement above does NOT need a \
    # at the end of the first line.
    result = letter_frequencyA( test_string )
    print 'letter_frequencyA says:'
    print result
    if result == correct_result:
        print 'and it\'s right!'
    else:
        print 'but it isn\'t right though.'
        # Note the escaped embedded quote here.
        # Alternatively the outer quotes could be double quotes, and the inner
        # quote not escaped. (see e.g. letter_frequencyC code below)
    print

    #########################
    # Test letter_frequencyB:
    #########################
    correct_result = [['a', 65], ['b', 11], ['c', 18], ['d', 29], ['e', 91],
                      ['f', 15], ['g', 30], ['h', 41], ['i', 54], ['j', 1],
                      ['k', 6], ['l', 26], ['m', 32], ['n', 52], ['o', 69],
                      ['p', 18], ['q', 0], ['r', 61], ['s', 58], ['t', 82],
                      ['u', 20], ['v', 5], ['w', 21], ['x', 1], ['y', 11],
                      ['z', 1]]
    result = letter_frequencyB( test_string )
    print 'letter_frequencyB says:'
    print result
    if result == correct_result:
        print 'and it\'s right!'
    else:
        print 'but it isn\'t right though.'
    print

    #########################
    # Test letter_frequencyC:
    #########################
    correct_result = {'a': 65, 'c': 18, 'b': 11, 'e': 91, 'd': 29, 'g': 30,
                      'f': 15, 'i': 54, 'h': 41, 'k': 6, 'j': 1, 'm': 32,
                      'l': 26, 'o': 69, 'n': 52, 'p': 18, 's': 58, 'r': 61,
                      'u': 20, 't': 82, 'w': 21, 'v': 5, 'y': 11, 'x': 1, 'z': 1}
    result = letter_frequencyC( test_string )
    print 'letter_frequencyC says:'
    print result
    if result == correct_result:
        print 'and it\'s right!'
    else:
        print 'but it isn\'t right though.'
    print
