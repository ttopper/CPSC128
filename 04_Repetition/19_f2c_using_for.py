# f2c_using_for.py
#
# This program can convert a temperature from Fahrenheit to Celsius.
# It creates a table of conversions from 0 to 100 F in increments of 10.
# 

print("Fahrenheit  Celsius")
for temp_in_f in range(0, 101,10):
    temp_in_c = (temp_in_f - 32) * 5 / 9
    print("{:6d}{:12.1f}".format(temp_in_f,temp_in_c))
