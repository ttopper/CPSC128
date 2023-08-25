
# pChange_ValueOf.py
#
# Kate Chatfield-Reed
# January 2023

print('''Tell me about the change in your pocket and I'll add it up for you.

How many of each type do you have?''')
toonies = int(input("Toonies: "))
loonies = int(input("Loonies: "))
quarters = int(input("Quarters: "))
dimes = int(input("Dimes: "))
nickels = int(input("Nickels: "))
print()

total = toonies * 2 + loonies * 1 + quarters * 0.25 + dimes * 0.1 \
        + nickels * 0.05

print(f"The change in your pocket is worth {total:.2f}.")
print("Don't blow it all in one place!")
print()

done = input("Press Enter to exit.")

