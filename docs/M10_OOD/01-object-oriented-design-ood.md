# Object-Oriented Design (OOD)

(The last of the long modules!)

The previous module concentrated on the new syntax and programming style required to _write_ object oriented code. A bigger question we will turn to now is how to _design_ OO code. Our simple OO design process* will be to,

1. Analyze the problem domain into a set of objects, and classify the objects by type.
2. Write a class to represent each type of object.
3. Instantiate classes to create individual objects.
4. Write the "main" program that specifies the pattern of communication among the objects.

## Analysis

The critical step here is the first one. While there is considerable craft in completing the remaining steps, decomposing your problem domain into the right set of objects is crucial. In our playing card example it was fairly obvious what the objects would need to be, and there was relatively little communication between them. This is not typical — in most non-trivial problems there are usually several equally plausible decompositions which would each lead to quite different programs.

How then to begin? The easiest case is where the problem domain you are modelling consists of physical objects that you can see. For example looking at one system you might see packages, boxes, pallets, trucks and warehouses while looking at another you might see a gearbox, drive shaft and axle. Next best is when your system does not consist of physical objects but the objects leave physical traces behind, for example bills, purchase orders and invoices, or laws, regulations and policies. Hardest is when it is not clear what the objects are. For example we know the climate is made of gaseous molecules but there are far too many of them for us to model it at that level. That means we must use some abstractions at a higher level that we hope capture what is going on at the molecular level, and often—as in the case of climate modelling—it is not clear what the appropriate abstractions are.

## Classes

Once you have identified the types of objects you need to model you use the Python language features from the last module to write a class for each type of object. This means identifying each object type's attributes (or state) and methods (or behaviour).

Two questions helpful in identifying objects' **attributes** are:

1. What **qualities** does this type of object have? For example does it have a weight? A colour? A size? An owner? A position?
2. What type of information can it **store**? For example a date of receipt? A list of contributors?

Two questions helpful in identifying objects' **methods** are:

1. What can this type of object **do**, i.e. what kinds of messages does it have to respond to? Can it move? Can it cancel? Can it record? Can it trigger?
2. What questions can it **answer** about itself? Can it report its size? Its position? Its colour?

You will notice that the attributes correspond to adjectives and nouns describing the objects, while the methods correspond to verbs. This distinction is often helpful when analyzing system descriptions.

## Instantiation

This simply means creating the objects your program requires and consists of calls to the class constructors. We've already done this, for example in the last module,

```
d = Deck()
 ...
roxx = Hand()
chris = Hand()
```

<br>

## Writing the "main" program

The last step to complete the program is to write the main routine which
specifies the pattern of communication between the objects in the
system.

------------------------------------------------------------------------

* We are just scratching the surface of a large and active area of
programming practice here. Much has been written about methodologies for
object oriented design, and there is a thriving industry of consultants
who ~~preach~~ teach one methodology or another. Through the 1990s these
methodologies became larger and larger until they begat a backlash
movement that argued for smaller more agile processes. An exemplar of
large-scale design is the [Rational Unified
Process](http://en.wikipedia.org/wiki/Rup) (RUP). This methodology
incorporates not only an extensive OO design process, it embeds it in a
complete software development framework. The Silesia page on [Agile
Software
Development](http://en.wikipedia.org/wiki/Agile_software_development) provides
pointers to some of the lighter-weight alternatives.
