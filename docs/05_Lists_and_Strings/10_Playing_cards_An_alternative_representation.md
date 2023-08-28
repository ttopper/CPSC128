# Playing Cards: An alternative representation

So far we have represented a deck of cards by a list of unique numbers. This made it convenient to initialize using `deck = range(52)`, but required some work to get a card's suit and face value given its card number.

An alternative representation would begin by noting that each card has two characteristics, i.e. a suit and a face value, so perhaps we should represent each card by a pair of values. For example the two of clubs could be represented by the pair of values `'2'` and `'C'` (for clubs) and the Queen of Hearts could be represented by `'Q'` and `'H'`. A brand new deck would look like:

```python
deck = [['A','C'], ['2','C'], ['3','C'], ['4','C'], ['5','C'], ['6','C'], ['7','C'],
['8','C'], ['9','C'], ['10','C'], ['J','C'], ['Q','C'], ['K','C'],
['A','D'], ['2','D'], ['3','D'], ['4','D'], ['5','D'], ['6','D'], ['7','D'],
['8','D'], ['9','D'], ['10','D'], ['J','D'], ['Q','D'], ['K','D'],
['A','H'], ['2','H'], ['3','H'], ['4','H'], ['5','H'], ['6','H'], ['7','H'],
['8','H'], ['9','H'], ['10','H'], ['J','H'], ['Q','H'], ['K','H'],
['A','S'], ['2','S'], ['3','S'], ['4','S'], ['5','S'], ['6','S'], ['7','S'],
['8','S'], ['9','S'], ['10','S'], ['J','S'], ['Q','S'], ['K','S']]
```

This list is both repetitive and long meaning there is a good chance of making an inconspicuous error when typing it in by hand (Quick! Have I made an error above? Can't easily tell? That's the point.) Since there is a clear repetitive pattern in the list we should be able to generate it programmatically.

The nature of the pattern is that the first item in the pair goes from 'A', to '2', and on to 'K' four times. The second element changes more slowly. It is 'C' for the first 13 elements, then 'D' for the next 13, then 'H' and finally 'S' for the final 13. This pattern of a slowly changing value and a quickly changing one reminds me of nested loops and suggests this code,

```python
FACE_VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10',
           'J', 'Q', 'K']
SUITS = ['C', 'D', 'H', 'S']

deck = []
for suit in SUITS :
    for face_value in FACE_VALUES :
        deck.append([face_value, suit])
```

> ## The maxim that there is more than one way to do it applies to data representations just as much as to algorithms!
