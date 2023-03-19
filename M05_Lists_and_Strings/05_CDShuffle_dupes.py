# CDShuffle_dupes.py
TESTS = ['madam', 'maam', 'motor', 'moor', 'a', 'oo', 'at',
         'A man, a plan, a canal, Panama!']
print('Testing Solution 1:')
for s in TESTS:
    print(s,end='')
    # Preprocess s to lower case and remove non-alphas.
    s_new = ''
    for c in s:
        if c.isalpha():
            if c.isupper():
                s_new = s_new + c.lower()
            else:
                s_new = s_new + c
    s = s_new # Replace s with s_new.
    
    # Test to see if s is a palindrome using Solution 1.
    palindrome = True
    for offset in range(0, len(s)//2):
        if s[offset] != s[len(s)-1-offset]:
           palindrome = False
    if palindrome:
        print("is a palindrome!")
    else:
        print("is NOT a palindrome.")
