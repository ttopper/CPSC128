"""

import time
import math
start = time.time()

sum = 0
for num in range(1,1000000):
    sum = sum + math.sqrt(num)

end = time.time()
print('That took',end-start,'seconds.')
print('Oh, and the sum is', sum)



print("Table of squares for 1-10")
print("    x    x**2")
for x in range(1,11):
    print("{:5d}{:8d}".format(x, x**2))



for s in range(1,10):
    for e in range(0,10):
        for n in range(0,10):
            for d in range(0,10):
                for m in range(1,10):
                    for o in range(0,10):
                        for r in range(0,10):
                            for y in range(0,10):
                                send = s*1000+e*100+n*10+d
                                more = m*1000+o*100+r*10+e
                                money = m*10000+o*1000+n*100+e*10+y
                                if send + more == money:
                                    if s!=e and s!=n and s!=d and s!=m and s!=o and s!=r  and s!=y and \
                                       e!=n and e!=d and e!=m and e!=o and e!=r and e!=y and \
                                       n!=d and n!=m and n!=o and n!=r and n!=y and \
                                       d!=m and d!=o and d!=r and d!=y and \
                                       m!=o and m!=r and m!=y and \
                                       o!=r and o!=y and \
                                       r!=y:
                                        print("  {:d}{:d}{:d}{:d}".format(s,e,n,d))
                                        print(" +{:d}{:d}{:d}{:d}".format(m,o,r,e))
                                        print("——")
                                        print(" {:d}{:d}{:d}{:d}{:d}".format(m,o,n,e,y))


# Display all the input number's factors.
# Version a: Simple, and somewhat fragile, but not inefficient.
# Two implementations.

import math

print("This program will display all the factors of the number you enter.")
num = int(input("Number: "))

print("{:d}'s factors are:".format(num))
divisor = 1
while divisor*divisor <= num:
    if num%divisor == 0:
        print(divisor, num//divisor)
    divisor = divisor + 1

# Display all the input number's factors.
# Version b: Simple, and somewhat fragile, but not inefficient.
# Two implementations.

import math

print("This program will display all the factors of the number you enter.")
num = int(input("Number: "))

print("{:d}'s factors are:".format(num))
print(1,num)
if num%2 == 0:
    divisor = 2
    increment = 1
else:
    divisor = 3
    increment = 2
while divisor*divisor <= num:
    if num%divisor == 0:
        print(divisor, num//divisor)
    divisor = divisor + increment




#
# A program to simulate how many families with four children will have 4 daughters
#

import random

all_girls = 0

for i in range(1000):
    girls = 0
    for j in range(4):
        girls = girls + random.randint(0,1)
    if girls == 4:
        all_girls = all_girls + 1

percentage = all_girls/1000*100

print("In 1,000 simulated four-child families")
print("approximately {:.1f} were made up of four daughters.".format(percentage))


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



"""
#
# This program can convert a temperature from Fahrenheit to Celsius.
# It creates a table of conversions from 0 to 100 F in increments of 10.
# 

print("Fahrenheit  Celsius")
for temp_in_f in range(0, 101,10):
    temp_in_c = (temp_in_f - 32) * 5 / 9
    print("{:6d}{:12.1f}".format(temp_in_f,temp_in_c))

"""

for i in (1,2,3):
    print("Hi!")


x = 0
while x < 2:
    y = 0
    while y < 5:
        print('*')
        y = y + 1
    print()
    x = x + 1



# Guess a random number between 1 and 100 picked by the computer.
# The computer will let you know if you are too high or too low.
#
# Kate Chatfield-Reed
# Winter 2023

import random

number = random.randint(1,100)
print("Guess a number between 1 and 100.")
guess = int(input("> "))

while guess != number:
    if number < guess:
        print("Too high. Try again!")
    elif number > guess:
        print("Too low. Try again!")
    guess = int(input("> "))

print("Correct! The number is {:d}.".format(guess))



# Find the smallest and largest values in a sequence entered by the user.
#
# Kate Chatfield-Reed
# Winter 2023

print("This program will display the largest and smallest values you enter.")
print()
print("You have to choose a special number to indicate the end of your input.")
sentinel = float(input("What number will indicate that you have entered all your values?"))
print()

print("Begin entering your values now.")
print("Press Enter after each one, and type your special number when you are done.")
num = float(input("> "))
smallest = num
largest = num
while num != sentinel:
    if num < smallest:
        smallest = num
    elif num > largest:
        largest = num
    num = float(input("> "))

if smallest == largest == sentinel:
    print("You only entered the special number you chose.")
else:
    print("The smallest value in your list is:", smallest)
    print("The largest value in your list is:", largest)



#
# This program prints the average of user input numbers.
# 

print("This program computes the average of the numbers entered.")
num_count = -1 # taking out the count from -999 in advance
total = 0
new_value = 0

while new_value != -999:
    total = total + new_value # I'm doing this before we get the number so I don't add -999
    num_count = num_count + 1
    new_value = float(input( "Enter a number to incorporate in the average: " ))
    

average = total/num_count
print("The average is {:.1f}.".format(average))




#
# This program prints the average of user input numbers.
# 

print("This program computes the average of the numbers entered.")
again = 'y'
num_count = 0
total = 0

while again == 'y' or again == 'Y':
    total = total + float(input( "Enter a number to incorporate in the average: " ))
    num_count = num_count + 1
    
    again = input("Do you want to add another value (y/n)? ")

average = total/num_count
print("The average is {:.1f}.".format(average))



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



print("Instructions to user...")
grade = float(input("Enter a numerical grade between 0 and 100: "))

while grade>100 or grade<0:
    print("Error: The grade must be between 0 and 100.")
    grade = float(input("Enter a numerical grade between 0 and 100: "))

if grade>=95:
    print("A+")
elif grade>= 86:
    print("A")



i = 1
while i <= 3:
    print("Hi!")
    i = i + 1


print("Instructions to user...")
grade = float(input("Enter a numerical grade between 0 and 100: "))

if grade >100 or grade<0:
    print("Error: The grade must be between 0 and 100.")
elif grade>=95:
    print("A+")
elif grade>= 86:
    print("A")
...
"""