# guessing_game.py
#
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
