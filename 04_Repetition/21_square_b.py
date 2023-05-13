# square_b.py
#
# Draw a hollow square on-screen. The size and character to use are chosen by
# the user.
#

print("This program will draw a square on screen.")
print
size = int(input("How large a square would you like? "))
c = input("What character should I use to draw it? ")

if size < 1:
    print("Sorry I need a positive number.")
else:
    for row in range(size):
        for col in range(size):
            if row == 0 or row == size-1 or col == 0 or col == size-1:
                print(c, end = '')
            else:
                print(' ', end = '')
        print()
