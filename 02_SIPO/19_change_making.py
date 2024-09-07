
# pChange_Making.py
#
# Kate Chatfield-Reed
# January 2023
#
print("This program tells you how to 'make change' using the fewest coins.")
print()
change = int(input("How much change do you have to make (in cents)? "))
print()
change = round(change/5) * 5
print(change, "cents change can be given using:")

toonies = change // 200
change = change % 200
loonies = change // 100
change = change % 100
quarters = change // 25
change = change % 25
dimes = change // 10
change = change % 10
nickels = change // 5

print(f"{toonies:d} toonies,")
print(f"{loonies:d} loonies,")
print(f"{quarters:d} quarters,")
print(f"{dimes:d} dimes,")
print(f"{nickels:d} nickels,")
print()

done = input("Press Enter to exit.")

