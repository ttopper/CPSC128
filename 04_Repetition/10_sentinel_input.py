# find_the_average.py
#
# This program prints the average of user input numbers.
# 

print("This program computes the average of the numbers entered.")
num_count = -1 # taking out the count from -999 in advance
total = 0
new_value = 0

while new_value != -999:
    total = total + new_value # I'm doing this before we get the number so I don't add -999
    num_count = num_count + 1
    new_value = float(input( "Enter a number to incorporate in the average: " ))
    

average = total/num_count
print(f"The average is {average:.1f}.")
