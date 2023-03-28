# A small example: A dice class

Before considering an extended example let's consider a small one to
see what the syntactical elements are that support OOP in Python. In
Python as in most OOP languages (including C++ and
Java—but_not_Javascript) the key OOP construct is the class. A class
specifies the characteristics of an object type and provides a rubber
stamp or template for creating objects of a particular type. Consider
for example a die (as in one dice, not death!). A die is quite a simple
object. It has a single attribute, its number of sides, and just one
method, `roll`, i.e. the only message you can really send a die is to
roll itself and report the result. Like I said it's a simple object.
Here is a complete `import`able module that defines a `Die` class and
some code to test it (minimally). First the code alone (I have left out
the docstrings to avoid obscuring the functional code):

    # die_class_0.py
    import random

    class Die:
        def __init__(self, n):
            self.nsides = n
            
        def roll(self):
            spots = random.randint(1,self.nsides)
            return spots

    if __name__ == '__main__':
        d1 = Die(6)
        red = Die(20)
        
        print('Rolling d1 ...',)
        result = d1.roll()
        print('result =', result)
        
        print('Rolling red and d1 together gets you:', d1.roll() + red.roll())
        print('The die d1 has %d sides' % (d1.nsides))

and then the code with (hopefully helpful) annotations,

![Annotated image of die class in Python
3.](06_Annotated_die_class.png)
