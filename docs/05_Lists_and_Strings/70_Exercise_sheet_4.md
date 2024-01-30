# Exercise Sheet 5

0. Write a list of lists that represents a library of books. Each book in the list should have a title, author, and number of pages stored as part of each book ["The Giver", "Lois Lowry", 240]. Try making your own library of books. Then see what you can do with your library. Here are my suggestions:

   a. Write some code asking for input to add a new book to the library.

   b. Write some code that prints all the titles in the library.

1. Write a program the gets a word from the user and replaces the middle of the word with random special characters chosen from a set (as if it were censoring a swear word). It will help to know the length of each word (we don’t want to do it if the length is less than 3) and where the middle sub-string starts and ends (you can use slice). You will also want a way to pick some special characters (maybe something similar to the boggle game). Remember string are immutable. I’ve shown an example below.

```plaintext
Enter a word for me to censor: talk
Here is the censored version: t@$k
```