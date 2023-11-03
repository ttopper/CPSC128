# Assignment 11

## Problems

1.  Using a `class` does not necessarily make a program object oriented. 
    Consider the code below. The first warning bells are that the 
    class has no methods and the functions in the module are stand 
    alone functions not class methods. The code uses a `class`, but if 
    you look carefully you will see that the class is used to represent 
    not one type of object but several types of objects. The give-away 
    is the attribute kind and the way it is tested by the remaining 
    functions in the module to decide what to do. *YOU DO NOT ACTUALLY 
    HAVE TO DRAW OR MANIPULATE SHAPES!* This is just an example of how 
    to implement good object oriented design.

        # Suppose we need to support circles, equilateral triangles and squares.
        (CIRCLE, TRIANGLE, SQUARE) = range(3)
        class Shape:
            def __init__(self, k, c, s):
                self.kind = k
                self.centre = c
                self.size = s
        ...
        def draw(shape):
            if shape.kind == CIRCLE:
                # code to draw a circle
                ...
            elif shape.kind == TRIANGLE:
                # code to draw a triangle
                ...
            else:
                # code to draw a square
                ...
        def fill(shape, colour):
        # Fills the shape with colour.
            if shape.kind == CIRCLE:
                # code to fill in a circle
                ...
            elif shape.kind == TRIANGLE:
                # code to fill in a triangle
                ...
            else:
                # code to fill in a square
                ...
        def rotate(shape, angle):
            # Rotates the shape about its centre by angle.
            if shape.kind == CIRCLE:
                # code to rotate a circle
                ...
            elif shape.kind == TRIANGLE:
                # code to rotate a triangle
                ...
            else:
                # code to rotate a square
                ...
 
        def groovy(shape_list):
            for shape in shape_list:
                draw(shape)
                rotate(shape, math.pi/2)
                fill(shape, random.randint(0,15))


    a. Suppose you are given this code and told you must add support 
       for an additional shape, pentagons. What changes would you 
       have to make to the module? Call this version a11_1_1a.py.

    b. Now refactor this code so it uses three classes Circle, 
       Triangle and Square instead of one where each class has its 
       own draw, fill, etc. methods. Call this version a11_1_1b.py.

    c. Finally, what changes have to be made to version a11_1_1b.py 
       to support a new pentagon shape type? Call this version 
       a11_1_1c.py

    d. Compare the changes you made in a. and c. above. In each case 
       how much existing code did you have to modify? Which approach 
       is most likely to result in breaking existing code? You can 
       put your answers to these questions in your submission comment.


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
    the first problen of this assignment will be named `a11p1bob.py` 
    (adjusted obviously to use your name).

-   Please submit your `.py` file to the Moodle dropbox.
