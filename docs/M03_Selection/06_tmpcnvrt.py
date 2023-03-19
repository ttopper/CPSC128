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
