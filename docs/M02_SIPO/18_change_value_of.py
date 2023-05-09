# pChange_ValueOf.py
#
# Kate Chatfield-Reed
# January 2023
print('''Tell me about the change in your pocket and I'll add it up for you.

How many of each type of coin do you have?''')
twonies = int(input("Twonies: "))
loonies = int(input("Loonies: "))
quarters = int(input("Quarters: "))
dimes = int(input("Dimes: "))
nickels = int(input("Nickels: "))
print()

total = twonies * 2 + loonies * 1 + quarters * 0.25 + dimes * 0.1 \
        + nickels * 0.05

print("The change in your pocket is worth ${:.2f}.".format(total))
print("Don't blow it all in one place!")
print()

done = input("Press Enter to exit.")
