# animal_samping.py
# Uses mark and recapture method to estimate population size in the wild
# It uses the equation N = (s*n)/x
# Where,
# N is the estimate of the total population
# s is the number of animals marked
# n is the number of animals recaptured
# x is the number of recaptured animals that are marked
#
# THIS CODE HAS 9+ ERRORS FOR YOU TO IDENTIFY AND FIX WHERE POSSIBLE
#
# TIPS
# Pay attention to the text colour in IDLE
# Use the error messages to narrow down where the syntax errors occur
# Make sure every backet and quotation mark that is opened is closed
# Think about all the possible inputs that someone might enter
# Think about the variable types
# And check the examples from the slides for hints.
#

# Explain the program (1 syntax error)
print(“This program calculates an estimate of a population size in the wild based on mark and recapture numbers.“)

# Get the values (5 errors: 4 syntax errors and 1 sneaky semantic error)
n = int(input("Enter the number of animals were marked in the first sample: ")
s = int(input("Enter the number of animals that you recaptured: '))
 x = input('How many animals in the recaptured sample were marked? ')

# Calculate the population size (several possible runtime errors to identify)
# BUT you don't need fix them because we haven't learned the tools yet!
N = (s*n)/x

Output the results (2 errors: 1 syntax and 1 semantic)
print("You tagged",s,"animals, recaptured",n,"animals, of which",x,"were tagged.")
print("The population size is approximately, N, animals.")