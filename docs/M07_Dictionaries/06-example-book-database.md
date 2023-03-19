# Example: Book Database

In this example we see that the items stored in the dictionary don't have to be numerical (as they were in the previous two examples).

This time we have a small database of book information stored in a dictionary (notice the curly brackets?),

```
books = { "The C Programming Language": ['Brian W. Kernighan',
                                         'Dennis M. Ritchie'],
          "Harry Potter and the Philosopher's Stone" : ['J. K. Rowling'],
          "The AWK programming language" : ['Alfred V. Aho',
                                            'Brian W. Kernighan',
                                            'Peter J. Weinberger'],
          "The practice of programming": ['Brian W. Kernighan', 'Rob Pike'],
          "The cat in the hat": ['Dr. Seuss'],
          "The UNIX Programming Environment": ['Brian W. Kernighan',
                                               'Rob Pike']
        }
```

Hopefully you can tell by looking at it that the keys are book titles, and the values are book authors. Since books can have multiple authors, lists (notice the square brackets?) are used for these values even when there is a single author. Suppose we wish to write a function to list the titles of the books by a given author.

## Pseudocode

```
def search_by_author( database, author ):
    Initialize book_list (the list of books by this author)
    For each key-value pair in the database
        If the value contains author
            Add the key to the book_list
    Return book_list
```

## Translated into Python

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
        

which produces as output,

    >>> 
    J. K. Rowling wrote: ["Harry Potter and the Philosopher's Stone"]
    Brian W. Kernighan wrote: ['The UNIX Programming Environment', 
    'The practice of programming', 'The AWK programming language', 'The C Programming Language']
    Tim Topper wrote: []
    >>> 
