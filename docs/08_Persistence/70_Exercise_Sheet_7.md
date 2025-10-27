# Tutorial 7

1. ### Text file practice

   Write a module containing three functions. When run, the module
   should prompt the user for a filename and a number of lines (let's
   refer to it as `n`) and then call each function in turn with these
   parameters.

   a.  The function `head1` should return a list containing the first
   `n` lines of the file using `read`.

   b.  The function `head2` should return a list containing the first
   `n` lines of the file using `readline`.

   c. The function `head3` should return a list containing the first
   `n` lines of the file using `readlines`.

   Make a test at the bottom to show the output of running the module,
   it might look like this:

   ```plaintext
       Name of file to test with: pooh.txt
       Number of lines to display: 3

       head1 says the first 3 lines are:
       The more it snows
         (Tiddely pom),
       The more it goes

       head2 says the first 3 lines are:
       The more it snows
         (Tiddely pom),
       The more it goes

       head3 says the first 3 lines are:
       The more it snows
         (Tiddely pom),
       The more it goes
   ```

    Here is a short file to test with [pooh.txt](90_pooh.txt)
   

2. ### Making it space efficient

   Since the file could be very long you will **not** want to read
   the whole thing into memory as a list of lines... Modify one of
   your `head` functions from the previous questions so that it
   only loads the number of lines needed (only one of them will
   work).

   Here is a short file to test with [pooh.txt](90_pooh.txt)


3. ### Trilobite data

   Follow along with the instructor to complete the functions
   used to work with the trilobite data. Make sure you have
   working versions of...

   a. `open_trilobite_data()`

   b. `calculate_diversity()`

   c. `write_trilobite_data()`

