# square_a.py
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
elif size == 1:
    print(c)
else:
    print(size*c + "\n" + (size-2)*(c+(size-2)*" " + c + "\n") + size*c + "\n")
