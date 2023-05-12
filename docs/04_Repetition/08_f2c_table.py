# f2c_table.py
#
# This program can convert a temperature from Fahrenheit to Celsius.
# It creates a table of conversions from 0 to 100 F in increments of 10.
# 

temp_in_f = 0

print("Fahrenheit  Celsius")
while temp_in_f <= 100:
    
    temp_in_c = (temp_in_f - 32) * 5 / 9
    print("{:8.1f}{:10.1f}".format(temp_in_f,temp_in_c))

    temp_in_f = temp_in_f + 10
