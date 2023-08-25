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
