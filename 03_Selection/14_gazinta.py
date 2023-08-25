# pGazinta.py
# Kate Chatfield-Reed

print('''Wondering if one number "goes into: another?
Give me the numbers (big one first) and I'll tell you.
''')

a = int(input('First number = '))
b = int(input('Second number = '))
print()

if b == 0:
    print('Sorry division by 0 is undefined!')
elif a%b == 0:
    print(b, 'does go into', a, 'exactly.')
else:
    print(b, 'does NOT go into', a, 'exactly.')
