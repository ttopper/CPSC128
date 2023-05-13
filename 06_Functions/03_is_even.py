# is_even.py
import random

def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
        
num = random.randint(0,100)

if is_even(num):
    print("Good news your magic number is even! 10 bonus points for you.")
else:
    print("Bad news, your magic number is odd.")