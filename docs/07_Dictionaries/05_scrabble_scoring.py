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
