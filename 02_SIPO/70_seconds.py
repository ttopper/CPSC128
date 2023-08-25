# seconds.py
# This program gets a time in seconds and converts it to days, hours, and minutes.
# It also uses print statements to help show its work.
# CPSC 128 Example
# Kate Chatfield-Reed, Winter 2023
#

print("This program gets a time in seconds and converts it to days, hours, and minutes.")


tot_seconds = int(input('Enter a time in seconds: '))

# find out how many days fit into the total number of seconds
days = tot_seconds // (24*60*60)

# find out how many seconds are left over after you take out the days
remainder = tot_seconds % (24*60*60)

# show progress
print(days, 'days, with,',remainder,'seconds left over')
pause = input() # wait for user to hit any key

# find out how many hours fit into the remaining seconds
hours = remainder // (60*60)

# find out how many seconds are left over after you take out the days and hours
remainder = remainder % (60*60)

# show progress
print(days, 'days,', hours, 'hours, with,',remainder,'seconds left over')
pause = input() # wait for user to hit any key

# find out how many minutes fit into the remaining seconds
minutes = remainder // 60

# find out how many seconds are left over after you take out the days, hours, and minutes
remainder = remainder % 60

#display the result
print(days, 'days,',hours,'hours,',minutes, 'minutes, and', remainder,'seconds.')