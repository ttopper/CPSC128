# smallest_largest.py
#
# Find the smallest and largest values in a sequence entered by the user.
#
# Kate Chatfield-Reed
# Winter 2023

print("This program will display the largest and smallest values you enter.")
print()
print("You have to choose a special number to indicate the end of your input.")
sentinel = float(input("What number will indicate that you have entered all your values?"))
print()

print("Begin entering your values now.")
print("Press Enter after each one, and type your special number when you are done.")
num = float(input("> "))
smallest = num
largest = num
while num != sentinel:
    if num < smallest:
        smallest = num
    elif num > largest:
        largest = num
    num = float(input("> "))

if smallest == largest == sentinel:
    print("You only entered the special number you chose.")
else:
    print("The smallest value in your list is:", smallest)
    print("The largest value in your list is:", largest)
