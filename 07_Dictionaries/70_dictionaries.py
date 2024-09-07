# ListOfDicts.py
data = [ {'id':4721, 'sex':'F', 'age':31},
         {'id':1828, 'sex':'M', 'age':56},
         {'id':7816, 'sex':'M', 'age':72},
         #. . . lots more records . . .
         {'id':3286, 'sex':'M', 'age':29},
         {'id':5063, 'sex':'F', 'age':22}
       ]

nmales = 0
nfemales = 0
for entry in data:
    if entry['sex'] == 'M':
        nmales = nmales + 1
    elif entry['sex'] == 'F':
        nfemales = nfemales + 1
print('There are', nmales, 'males and', nfemales, 'females.')

oldest = data[0]
for entry in data[1:]:
    if entry['age'] > oldest['age']:
        oldest = entry
print('The oldest person is:', oldest)

"""
# BooksDict.py
def search_by_author(database, author):
    book_list = []
    for key in database:
        if author in database[key]:
            book_list.append( key )
    return book_list

if __name__ == '__main__':
    books = { "Harry Potter and the Philosopher's Stone" : ['J. K. Rowling'],
              "The cat in the hat": ['Dr. Seuss'],
              "The C Programming Language": ['Brian W. Kernighan',
                                             'Dennis M. Ritchie'],
              "The UNIX Programming Environment": ['Brian W. Kernighan',
                                                   'Rob Pike'],
              "The AWK programming language" : ['Alfred V. Aho',
                                                'Brian W. Kernighan',
                                                'Peter J. Weinberger'],
              "The practice of programming": ['Brian W. Kernighan', 'Rob Pike']
            }
    print('J. K. Rowling wrote:', search_by_author(books, 'J. K. Rowling'))
    print('Brian W. Kernighan wrote:',search_by_author(books, 'Brian W. Kernighan'))
    print('Tim Topper wrote', search_by_author(books, 'Tim Topper'))

# ScrabbleScoring.py
LETTER_VALUES = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 'G':2,
                 'H':4, 'I':1, 'J':8, 'K':5, 'L':1, 'M':3, 'N':1,
                 'O':1, 'P':3, 'Q':10, 'R':1, 'S':1, 'T':1, 'U':1,
                 'V':4, 'W':4, 'X':8, 'Y':4, 'Z':1}

def scrabble_value(s):
    total_value = 0
    for letter in s:
        total_value = total_value + LETTER_VALUES[letter]
    return total_value

if __name__ == '__main__':
    print('The value of the word HERE is', scrabble_value('HERE'))


# WordFrequencies.py
# Get the string:
test_string = '''The programmer, who needs clarity, who must talk all day to
    a machine that demands declarations, hunkers down into a low-grade annoyance.
    It is here that the stereotype of the programmer,
    sitting in a dim room, growling from behind Coke cans, has its origins.
    The disorder of the desk, the floor; the yellow Post-It notes everywhere;
    the whiteboards covered with scrawl:
    all this is the outward manifestation of the messiness of human thought.
    The messiness cannot go into the program;
    it piles up around the programmer.
    ~ Ellen Ullman
'''

# Break the string into a list of words:
words = test_string.split()
# Initialize a dictionary of counters:
word_counts = {}

# Loop through the list of words:
for word in words:
    w = word.lower()
    w = w.strip('.,;:'"?!()') # Notice the \ to escape the ' inside the string
    if w.isalpha():
        if w in word_counts:
            word_counts[w] = word_counts[w] + 1
        else:
            word_counts[w] = 1

# Loop through the entries in the dictionary:
for word in word_counts:
    # Display the key value pair:
    print(word, ':', word_counts[word])


d = { 'Tim' : 775, 'Brian' : 869 }

for key in d:
    print(key, ':', d[key])

def string_index( s ):
    index = 0
    for i in range(len(s)):
        index = index + (ord(s[-i]) - ord('a') + 1) * 26**i
    return index
        
print(string_index('cat'))
print(string_index('dictionary'))


test_str ='astringalingding'
counters = 26*[0] # Initialize list of counters to be 26 0s.
for ch in test_str:
    # Calculate index of counter for this letter in counters.
    index = ord(ch) - ord('a')
    # Increment appropriate counter.
    counters[index] = counters[index] + 1
for index in range(26):
    # Display letter corresponding to this index and its count.
    print(chr(ord('a')+index), counters[index])
"""