# Tutorial 6

1.  ### Every letter counts

    First up a problem to give you a little practice working with the
    collection types (lists and dictionaries). Write the following
    implementations of the function `letter_frequency` that takes a
    string and returns a collection type showing how often each letter
    of the alphabet occurs in the string.

    a.  The first version (`letter_frequencyA`) should return a list
        with 26 integer elements representing the frequency of
        occurrence of each letter of the alphabet in order from a to z.

    b.  The second version (`letter_frequencyB`) should return a list of
        26 lists, each of which contains a letter and its associated
        count.

    c.  The third version (`letter_frequencyC`) should return a
        dictionary that uses the letters as keys and whose values are
        the letters' counts. Make sure to use a dictionary specific solution!

    The program that will call these functions is
    [`letter_frequency.py`](90_letter_frequency.py). Your job is to replace
    the `pass` statements with function bodies that implement the
    functionality specified above. Studying the embedded tests should
    answer any other questions you have about the functions'
    operations.