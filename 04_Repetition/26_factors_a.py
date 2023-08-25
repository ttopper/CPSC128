# factors.py
#
# Display all the input number's factors.
# Version a: Simple, and somewhat fragile, but not inefficient.
# Two implementations.

import math

print("This program will display all the factors of the number you enter.")
num = int(input("Number: "))

print("{:d}'s factors are:".format(num))
divisor = 1
while divisor*divisor <= num:
    if num%divisor == 0:
        print(divisor, num//divisor)
    divisor = divisor + 1
