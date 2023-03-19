# pOilSpill.py
#
# Kate Chatfield-Reed
# January 2023
import math

print('''This program estimates the current size of an oil spill
based on how long ago the spill began.
''')
duration = int(input("How long ago in minutes did the oil spill start? "))
print()

area = 6000*math.sqrt(duration)

print("The area of the spill after", duration, "minutes is")
print("approximately {:.2f} sqare metres.".format(area))
print()

done = input("Press Enter to exit.")