# pPythagoras-a.py
# Kate Chatfield-Reed

print('''
===========================
Right-angle triangle tester
---------------------------

Enter the lengths of the sides of your triangle and I will tell you
if it has a right angle or not.
''')

a = int(input('Length of first side = '))
b = int(input('Length of second side = '))
c = int(input('Length of third side = '))
print()

if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print('That is a right-angled trangle.')
else:
    print('That is not a right-angle trangle.')
