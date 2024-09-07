# all_girls.py
#
# A program to simulate how many families with four children will have 4 daughters
#

import random

all_girls = 0

for i in range(1000):
    girls = 0
    for j in range(4):
        girls = girls + random.randint(0,1)
    if girls == 4:
        all_girls = all_girls + 1

percentage = all_girls/1000*100

print("In 1,000 simulated four-child families")
print(f"approximately {percentage:.1f} were made up of four daughters.")
