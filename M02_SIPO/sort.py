# sort.py
#
#This program evaluates three values, sorts them from smallest to largest,
#then prints the result.

print("This program takes three unique numbers and sorts them from biggest to smallest.")
# gets 3 values from the user
print ("Okay, gimme a value:")
v1 = float(input())
print ("Now, gimme a value different from the last one:")
v2 = float(input())
print ("And now I need one more, different from both of the others:")
v3 = float(input())
print ("Working...")

# checks to see if any of the values are the same
if v1 == v2 or v1 == v3 or v2 == v3:
    print ("Whoa, whoa, whoa! Two or more of these values are equal! Didn't I just tell you that you can't do that?!")
# now that we know they are all different we can find out which is biggest
else:
    # if v1 is bigger than v2 we have still have to figure out where v3 fits in 
    if v1 > v2:
        # if v3 is bigger than v1 it has to be the biggest
        if v3 > v1:
            print (v3,">",v1,">",v2)
        # if we get here v3 is smaller than v1, so we check to see if it is bigger than v2
        elif v3 > v2:
            print (v1,">",v3,">",v2)
        # it isn't bigger than v1 or v2, so it must be the smallest number
        else:
            print (v1,">",v2,">",v3)
    # now let's check to see if v2 is bigger than v3
    elif v2 > v3:
        # we already know that v2 is bigger than v1 (because v1 > v2 failed above)
        # so no we need to figure out v3 relative to v1
        if v1 > v3:
            print (v2,">",v1,">",v3)
        else:
            print (v2,">",v3,">",v1)
    # now we know that v1 is less than v2 (because v1 > v2 failed above)
    # we know that v2 is less than v2 (because v2 > v3 failed above)
    # so we know the only option left
    else:
        print (v3,">",v2,">",v1)

input("Press enter to close.")