# pTreeCircumference.py
#
# Kate Chatfield-Reed
# January 2023
import math

print('''This program converts a measurement of a tree's circumference into an
estimate of its diameter (assuming the tree to be circular in 
cross-section).
''')

circumference = float(input('Enter the circumference of the tree in centimetres: '))
print()

diameter = circumference/math.pi

print("The tree's diameter is {:.2f} centimetres.".format(diameter))
print()

done = input("Press Enter to exit.")
