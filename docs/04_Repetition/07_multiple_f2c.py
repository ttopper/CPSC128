# multiple_f2c.py
#
# This program can convert a temperature from Fahrenheit to Celsius.
# It will do it multiple times if the user indicates the want to do another conversion.
# 

print("This program converts temperatures from Fahrenheit to Celsius.")
again = 'y'

while again == 'y' or again == 'Y':
    temp_in_f = float(input( "Enter a temperature in Fahrenheit (e.g. 10) and press Enter: " ))
    temp_in_c = (temp_in_f - 32) * 5 / 9
    print("{:.1f} degrees Fahrenheit = {:.1f} degrees Celsius.".format(temp_in_f,temp_in_c))

    again = input("Do you want to convert another value (y/n)? ")

print("Bye now.")
