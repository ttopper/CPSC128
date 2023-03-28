#!/usr/bin/python
# https://gist.github.com/zamber/af5086cb9c097be5c002
import os
import re
from titlecase import titlecase  # pip install titlecase

# Config
root = 'src'

os.chdir(root)

dictionary = {}

for node in os.walk('.'):
    path = node[0].strip('./')
    # i[1] are directories, ignore. This does not have to be recursive (yet)
    filelist = node[2]
    dictionary[path] = filelist

# http://blog.codinghorror.com/sorting-for-humans-natural-sort-order/


def sorted_nicely(l):
    """ Sort the given iterable in the way that humans expect.
        Modified to ignore case sensitivity in sorting. """
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [
        convert(c) for c in re.split('([0-9]+)', key.lower())]
    return sorted(l, key=alphanum_key)


def full_caps(word, **kwargs):
    """ Callback for title case, retains full caps words. """
    if (word.upper() == word):
        return word


def prettify(title):
    """ Convert a filename to a title cased, numbered title. """
    title = re.split('-', re.sub('_', '-', title))
    if (any(title) == False):
        return ''
    elif (title[0].isdigit()):
        title[0] += '.'
    return titlecase(re.sub('\.md$', '', ' '.join(title)), callback=full_caps)

for path in sorted_nicely(dictionary):
    print("- " + prettify(path) + ":")
    counter = 1
    for filename in sorted_nicely(dictionary[path]):
        title = filename
        # add an index number if the filename does not have one
        if (not(title[:1].isdigit())):
            title = str(counter) + '-' + title
        title = prettify(title)
        # files
        print("    - '" + title + "': '" + path + "/" + filename + "'")
        counter += 1