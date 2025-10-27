# Assignment 7

## Problems


1.  ### Small mammal data

    At Yukon University we have researchers tracking wildlife around 
    Yukon since 2005. They have collected data about mice from a site near 
    Whitehorse. They used live trapping techniques to record details of 
    various small mammal they caught during each trapping session. Dr. Scott 
    Gilbert shared some of his research data in a tab delimited text file 
    **small_mammal_data.txt**. The file is available on the Moodle. We are 
    particularly interested in the reproductive health of the female 
    Clethrionomys sp. There are many columns in the data that represent 
    different characteristics of the mice that were tracked at different time 
    points over the summer.

    a. Write a function called `load_mouse_data` that has two arguments: a string 
       representing the name of the datafile and a string representing the mouse 
       `Species` that we are interested in. The function should return the data 
       from the file as a list of lists with only the rows for that mouse species. 
       Keep the first row that has the column names. Try to solve this without 
       loading the whole file.

    b. Write a function called `save_mouse_data` that has two arguments: the data as 
       a list of lists and a string called filename that indicates where to save 
       the modified data. The function should create a new data file of the mouse 
       data with filename specified. The function should return None.

    c. Write function called `sexed_weight` that has two arguments: the data from 
       the file as a list of lists and an integer indicating the `Sex` you are 
       interested in (1 for male and 2 for female). The function returns a float 
       that represents the mean weight of the mice of that sex in that dataset.

    d. Write a function called `lactation_status` that takes the data from the file 
       as a list of lists and returns a dictionary where the keys are the `Lactation` 
       status and the values are the counts of the females with that lactation status. 
       A lactation status of 1 means not lactating, 2 means just starting or finishing 
       lactating, and 3 indicates that they are lactating for sure.


2.  ### Testing `biggest()`

    The last few assignments have provided you with examples of testing
    harnesses to ensure programs are working correctly. Now it is time
    for you to design some tests of your own. The file
    [a7p2kate.py](90_a7p2kate.py) contains six versions of a function named
    `biggest` that all claim to return the largest of three values they
    are passed. Add test cases to the program to determine which ones
    (if any) work correctly. Based on your test cases identify the
    situations (if any) in which each version fails, and the reason for
    the failure, i.e. what the problem is with the code. Enter your
    answers into the docstrings for each function.


## Logistics

-   Use the following naming scheme for your program files:
    `a`*assignment#*`p`*problem#yourname*`.py` . So your solution
    to problem 1 on this assignment will be named `a7p1bob.py`
    and your solution for problem 2 will be named `a7p2bob.py` (adjusted obviously to use your name).

-   Please submit all your `.py` files to the Moodle dropbox.
