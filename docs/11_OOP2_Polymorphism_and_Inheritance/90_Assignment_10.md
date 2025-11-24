# Assignment 10

## Problems

1.  Think about how you would redesign the three hazard types from
    last week to use inheritance. What would the parent class be?
    How would the code in the three hazards change? How would the
    code change when you initiate the hazards or in the main loop?
    Write the parent class and modify the hazards from the game 
    to inherit from it. Show the places if any that would need
    to change when you create or interact with hazards. In the 
    comment at the top tell me if your design changed as you 
    implemented the refactoring, and tell me if you think there is an
    advantage to the new implementation. If you did not complete the
    assignment you can work with the code provided in the slides or
    on the website.


2.  The class `CoinJar` represents a jar of Canadian coins. Write the 
    necessary code so this program will run correctly.

        tims = CoinJar(pennies=3, quarters=2, loonies=1,toonies=0)
        mollys = CoinJar(pennies=48, nickels=12, dimes=7, quarters=14)
        print(tims.value()) # Displays 1.53
        print(mollys.value()) # Displays 5.28
        print(tims.dimes) # Displays 0.
        print(tims[0]) # Displays 0.
        print(mollys.quarters) # Displays 14.
        print(mollys[3]) # Displays 7.
        if tims > mollys:
            print('Tim is richer than Molly.')
        else:
            print('Molly is at least as rich as Tim.')
        # ^ Displays: Molly is at least as rich as Tim.
        tims = tims + mollys
        print(tims) # Fancy display of your design.

    Hint: Since the order of the parameters varies between the two 
    constructor calls in lines 1 and 2 we can tell that named parameters 
    are being used.

3.  The file [`WumpusAdjMatrixMap.py`](90_WumpusAdjMatrixMap.py) contains 
    an alternative representation of a wumpus cave system (one based on an 
    adjacency matrix* rather than the list of lists of tunnels we have been 
    using) and stubs for two functions: tunnels_from and tunnels_to. Write 
    the bodies of these functions so they will work as the docstrings 
    describe. The docstrings contain one test of each function, but these 
    are meant to be illustrative rather than exhaustive.

    Note that you don't have to integrate this representation into your 
    earlier Hunt the Wumpus program. This is a stand alone problem.

    Hint: You might want to peek ahead at Module 12 to see how to activate 
    the tests in the docstrings.

## Logistics

-   Use the following naming scheme for your program files:
    `a`*assignment#*`p`*problem#*yourname`.py` . So your code for the 
    the first problen of this assignment will be named `a10p1bob.py` 
    (adjusted obviously to use your name).

-   Please submit your `.py` file to the Moodle dropbox.
