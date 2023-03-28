# Exercise Sheet 5

0. Write a list of lists that represents a library of books. Each book in the list should have a title, author, and number of pages stored as part of each book ["The Giver", "Lois Lowry", 240]. Try making your own library of books. Then see what you can do with your library. Here are my suggestions:

   a. Write some code asking for input to add a new book to the library.

   b. Write some code that prints all the titles in the library.

   c. Write some code that prints all the authors (and remove duplicates if you have more
   than one book by the same author).

   d. Write some code that will tell you the title of the longest book.

1. Modify the program `boggle.py` using lists so that instead of choosing the letters randomly from a string it uses a list representing 16 different dice, each with 6 possible letters to choose from. These will represent the dice that are used in the physical version of the game. If the game format is unclear check out the [Wikipedia page for Boggle](https://en.wikipedia.org/wiki/Boggle). Below are the letters found on each of the 16 dice.

```plaintext
"AAEEGN", "ABBJOO", "ACHOPS", "AFFKPS",
"AOOTTW", "CIMOTU", "DEILRX", "DELRVY",
"DISTTY", "EEGHNW", "EEINSU", "EHRTVW",
"EIOSST", "ELRTTY", "HIMNQU", "HLNNRZ"
```

2. Write a program the gets a word from the user and replaces the middle of the word with random special characters chosen from a set (as if it were censoring a swear word). It will help to know the length of each word (we don’t want to do it if the length is less than 3) and where the middle sub-string starts and ends (you can use slice). You will also want a way to pick some special characters (maybe something similar to the boggle game). Remember string are immutable. I’ve shown an example below.

```plaintext
Enter a word for me to censor: talk
Here is the censored version: t@$k
```

3. Write a version of the code above that will work on a whole sentence. It will help to split the list up into the individual words first.

```plaintext
Enter a sentence for me to censor:
I do not talk to foxes.

Here is the censored version:
I do n&t t#&k to f&@$s.
```