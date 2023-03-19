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
