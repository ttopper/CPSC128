
"""

# pBeaufortScale-c.py
# Kate Chatfield-Reed

print('''.:!Beaufort Wind Scale!:.
''')

wind_speed = float(input("Enter the wind speed in miles per hour (ideally measure 10 m off the ground): "))
print()

if wind_speed < 0:
    print("Check your anemometer, it shouldn't generate negative values.")
elif wind_speed > 83:
    print('A wind speed of', wind_speed, 'is off the Beaufort scale, so there is no classification')
    print('for it (but I suggest you take shelter).')
else:
    if wind_speed <= 1:
        force = 0
        specification = "Calm"
    elif wind_speed <= 3:
        force = 1
        specification = "Light Air"
    elif wind_speed <= 7:
        force = 2
        specification = "Light Breeze"
    elif wind_speed <= 12:
        force = 3
        specification = "Gentle Breeze"
    elif wind_speed <= 18:
        force = 4
        specification = "Moderate Breeze"
    elif wind_speed <= 24:
        force = 5
        specification = "Fresh Breeze"
    elif wind_speed <= 31:
        force = 6
        specification = "Strong Breeze"
    elif wind_speed <= 38:
        force = 7
        specification = "Near Gale"
    elif wind_speed <= 46:
        force = 8
        specification = "Gale"
    elif wind_speed <= 54:
        force = 9
        specification = "Severe Gale"
    elif wind_speed <= 63:
        force = 10
        specification = "Storm"
    elif wind_speed <= 72:
        force = 11
        specification = "Violent Storm"
    else:
        force = 12
        specification = "Hurricane"

msg = 'A wind speed of {:.1f} mph corresponds to Force {} or {}'.format(wind_speed,force,specification)

print('''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/1999/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns=http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
    <meta http-equiv="content-type" content="text/html; charset=iso-8859-1" />
    <title>Beaufort Wind Scale</title>
</head>
<body>
    <p>{}</p>
</body>
</html>
'''.format(msg))


# pBeaufortScale-b.py
# Kate Chatfield-Reed

print('''.:!Beaufort Wind Scale!:.
''')

wind_speed = float(input("Enter the wind speed in miles per hour (ideally measure 10 m off the ground): "))
print()

if wind_speed < 0:
    print("Check your anemometer, it shouldn't generate negative values.")
elif wind_speed > 83:
    print('A wind speed of', wind_speed, 'is off the Beaufort scale, so there is no classification')
    print('for it (but I suggest you take shelter).')
else:
    if wind_speed <= 1:
        force = 0
        specification = "Calm"
    elif wind_speed <= 3:
        force = 1
        specification = "Light Air"
    elif wind_speed <= 7:
        force = 2
        specification = "Light Breeze"
    elif wind_speed <= 12:
        force = 3
        specification = "Gentle Breeze"
    elif wind_speed <= 18:
        force = 4
        specification = "Moderate Breeze"
    elif wind_speed <= 24:
        force = 5
        specification = "Fresh Breeze"
    elif wind_speed <= 31:
        force = 6
        specification = "Strong Breeze"
    elif wind_speed <= 38:
        force = 7
        specification = "Near Gale"
    elif wind_speed <= 46:
        force = 8
        specification = "Gale"
    elif wind_speed <= 54:
        force = 9
        specification = "Severe Gale"
    elif wind_speed <= 63:
        force = 10
        specification = "Storm"
    elif wind_speed <= 72:
        force = 11
        specification = "Violent Storm"
    else:
        force = 12
        specification = "Hurricane"

print('A wind speed of {:.1f} mph corresponds to Force {} or {}'.format(wind_speed,force,specification))
print()


# pBeaufortScale-a.py
# Kate Chatfield-Reed

print('''.:!Beaufort Wind Scale!:.
''')

wind_speed = float(input("Enter the wind speed in miles per hour (ideally measure 10 m off the ground): "))
print()

if wind_speed < 0:
    print("Check your anemometer, it shouldn't generate negative values.")
elif wind_speed <= 1:
    print('A wind speed of', wind_speed, 'mph corresponds to Force 0 or "Calm"')
elif wind_speed <= 3:
    print('A wind speed of', wind_speed, 'mph corresponds to Force 1 or "Light Air"')
elif wind_speed <= 7:
    print('A wind speed of', wind_speed, 'mph corresponds to Force 2 or "Light Breeze"')
elif wind_speed <= 12:
    print('A wind speed of', wind_speed, 'mph corrsponds to Force 3 or "Gentle Breeze"')
elif wind_speed <= 18:
    print('A wind speed of', wind_speed, 'mph corresponds to Force 4 or "Moderate Breeze"')
elif wind_speed <= 24:
    print('A wind speed of', wind_speed, 'mph corresponds to Force 5 or "Fresh Breeze"')
elif wind_speed <= 31:
    print('A wind speed of', wind_speed, 'mph corresponds to Force 6 or "Strong Breeze"')
elif wind_speed <= 38:
    print('A wind speed of', wind_speed, 'mph corresponds to Force 7 or "Near Gale"')
elif wind_speed <= 46:
    print('A wind speed of', wind_speed, 'mph corresponds to Force 8 or "Gale"')
elif wind_speed <= 54:
    print('A wind speed of', wind_speed, 'mph corresponds to Force 9 or "Severe Gale"')
elif wind_speed <= 63:
    print('A wind speed of', wind_speed, 'mph corresponds to Force 10 or "Storm"')
elif wind_speed <= 72:
    print('A wind speed of', wind_speed, 'mph corresponds to Force 11 or "Violent Storm"')
elif wind_speed <= 83:
    print('A wind speed of', wind_speed, 'mph corresponds to Force 12 or "Hurricane"')
else:
    print('A wind speed of', wind_speed, 'is off the Beaufort scale, so there is no classification')
    print('for it (but I suggest you take shelter).')



# pUtilityBills.py
# Kate Chatfield-Reed

print('''
=======================
    Bill Calculator
-----------------------''')
kwh = float(input('Enter kilowatt-hours used: '))
if kwh < 0:
    print('\nRecheck input value!')
    print("It was egative, and the meters\ndon't run backward.")
else:
    if kwh <= 500.0:
        amount = 20.0
    elif kwh <= 1000.0:
        amount = 20.0 + 0.03*(kwh-500)
    else:
        amount = 35.0 + 0.02*(kwh-1000)
print('Bill amount = ${:.2f}.'.format(amount))




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



###########################################################
## tmpcnvrt.py -- allows the user to convert a temperature
##        in Fahrenheit to Celsius or vice versa.
##
## CPSC 128 Demonstration Program
##
## Kate Chatfield-Reed, Winter 2023
###########################################################
print("This program converts temperatures from Fahrenheit to Celsius,")
print("or from Celsius to Fahrenheit.")
print("Choose")
print("1 to convert Fahrenheit to Celsius")
print("2 to convert Celsius to Fahrenheit")

choice = int(input( "Your choice? " ))

if choice == 1:
    print("This program converts temperatures from Fahrenheit to Celsius.")
    temp_in_f = int(input( "Enter a temperature in Fahrenheit (e.g. 10) and press Enter: " ))
    temp_in_c = (temp_in_f - 32) * 5 / 9
    print(temp_in_f, " degrees Fahrenheit = ", temp_in_c, " degrees Celsius.")

elif choice == 2:
    print("This program converts temperatures from Celsius to Fahrenheit .")
    temp_in_c= int(input( "Enter a temperature in Celsius (e.g. 10) and press Enter: " ))
    temp_in_f = temp_in_c * 9 / 5 + 32
    print(temp_in_c, " degrees Celsius = ", temp_in_f, " degrees Fahrenheit.")

else:
    print("Error: Your choice not recognized!")



# pOilSpill.py
#
# Kate Chatfield-Reed
# January 2023
import math

print('''This program estimates the current size of an oil spill
based on how long ago the spill began.
''')
duration = int(input("How long ago in minutes did the oil spill start? "))
print()

area = 6000*math.sqrt(duration)

print("The area of the spill after", duration, "minutes is")
print("approximately {:.2f} sqare metres.".format(area))
print()

done = input("Press Enter to exit.")




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

twonies = change // 200
change = change % 200
loonies = change // 100
change = change % 100
quarters = change // 25
change = change % 25
dimes = change // 10
change = change % 10
nickels = change // 5

print("{:d} twonies,".format(twonies))
print("{:d} loonies,".format(loonies))
print("{:d} quarters,".format(quarters))
print("{:d} dimes,".format(dimes))
print("{:d} nickels,".format(nickels))
print()

done = input("Press Enter to exit.")



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



# pTreeCircumference.py
#
# Kate Chatfield-Reed
# January 2023
import math

print('''This program converts a measurement of a tree's circumference into an
estimate of its diameter (assuming the tree to be circular in 
cross-section).
''')

circumference = float(input('Enter the circumference of the tree in centimetres: '))
print()

diameter = circumference/math.pi

print("The tree's diameter is {:.2f} centimetres.".format(diameter))
print()

done = input("Press Enter to exit.")
"""
