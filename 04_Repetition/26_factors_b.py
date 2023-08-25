# factors_b.py
#
# Display all the input number's factors.
# Version b: Simple, and somewhat fragile, but not inefficient.
# Two implementations.

import math

print("This program will display all the factors of the number you enter.")
num = int(input("Number: "))

print("{:d}'s factors are:".format(num))
print(1,num)
if num%2 == 0:
    divisor = 2
    increment = 1
else:
    divisor = 3
    increment = 2
while divisor*divisor <= num:
    if num%divisor == 0:
        print(divisor, num//divisor)
    divisor = divisor + increment
