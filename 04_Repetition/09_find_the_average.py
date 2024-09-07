# find_the_average.py
#
# This program prints the average of user input numbers.
# 

print("This program computes the average of the numbers entered.")
again = 'y'
num_count = 0
total = 0

while again == 'y' or again == 'Y':
    total = total + float(input( "Enter a number to incorporate in the average: " ))
    num_count = num_count + 1
    
    again = input("Do you want to add another value (y/n)? ")

average = total/num_count
print(f"The average is {average:.1f}.")
