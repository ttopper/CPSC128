# pPythagoras-b.py
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

hypoteneuse = a
if b>hypoteneuse:
    hypoteneuse = b
if c>hypoteneuse:
    hypoteneuse = c

if a**2 + b**2 + c**2 == 2*hypoteneuse**2:
    print('That is a right-angled trangle.')
else:
    print('That is not a right-angle trangle.')
