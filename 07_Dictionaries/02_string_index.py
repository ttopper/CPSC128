# string_index.py

def string_index( s ):
    index = 0
    for i in range(len(s)):
        index = index + (ord(s[-i]) - ord('a') + 1) * 26**i
    return index
        
print(string_index('cat'))
print(string_index('dictionary'))