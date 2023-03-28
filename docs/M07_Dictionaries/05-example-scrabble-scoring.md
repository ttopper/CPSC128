# Example: Scrabble Scoring

Dictionaries aren't only useful for counting. In fact they are more frequently used to look up information by key value. We'll consider a couple of examples of this starting with a small one.

Players in the board game Scrabble score points by building words out of letters. The value of a word depends on the letters it is built from. (It also depends on where they are placed on the board, but we'll ignore that issue — at least for now!). The value of each letter is shown below. Write a function that is passed a word and returns the total Scrabble-value of the word.

```
A=1 B=3 C=3 D=2  E=1 F=4 G=2 H=4 I=1 J=8 K=5 L=1 M=3
N=1 O=1 P=3 Q=10 R=1 S=1 T=1 U=1 V=4 W=4 X=8 Y=4 Z=1
```

## Pseudocode

```
def ScrabbleValue( s ):
    Initialize the total value to 0
    Loop through the word a letter at a time
        Look up the letter's value
        Increment the total value by this letter's value
    Return the total value
```


## Python code

```python
    # ScrabbleScoring.py
    LETTER_VALUES = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 'G':2,
                     'H':4, 'I':1, 'J':8, 'K':5, 'L':1, 'M':3, 'N':1,
                     'O':1, 'P':3, 'Q':10, 'R':1, 'S':1, 'T':1, 'U':1,
                     'V':4, 'W':4, 'X':8, 'Y':4, 'Z':1}

    def scrabble_value(s):
        total_value = 0
        for letter in s:
            total_value = total_value + LETTER_VALUES[letter]
        return total_value

    if __name__ == '__main__':
        print('The value of the word HERE is', scrabble_value('HERE'))
```

Note: The documentation and testing are both minimal. I included what I
did as placeholders to remind you that they are part of complete
programs.
