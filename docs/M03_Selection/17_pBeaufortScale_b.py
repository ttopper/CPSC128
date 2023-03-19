# pBeaufortScale-b.py
# Kate Chatfield-Reed

print('''.:!Beaufort Wind Scale!:.
''')

wind_speed = float(input("Enter the wind speed in miles per hour (ideally measure 10 m off the ground): "))
print()

if wind_speed < 0:
    print("Check your anemometer, it shouldn't generate negative values.")
elif wind_speed > 83:
    print('A wind speed of', wind_speed, 'is off the Beaufort scale, so there is no classification')
    print('for it (but I suggest you take shelter).')
else:
    if wind_speed <= 1:
        force = 0
        specification = "Calm"
    elif wind_speed <= 3:
        force = 1
        specification = "Light Air"
    elif wind_speed <= 7:
        force = 2
        specification = "Light Breeze"
    elif wind_speed <= 12:
        force = 3
        specification = "Gentle Breeze"
    elif wind_speed <= 18:
        force = 4
        specification = "Moderate Breeze"
    elif wind_speed <= 24:
        force = 5
        specification = "Fresh Breeze"
    elif wind_speed <= 31:
        force = 6
        specification = "Strong Breeze"
    elif wind_speed <= 38:
        force = 7
        specification = "Near Gale"
    elif wind_speed <= 46:
        force = 8
        specification = "Gale"
    elif wind_speed <= 54:
        force = 9
        specification = "Severe Gale"
    elif wind_speed <= 63:
        force = 10
        specification = "Storm"
    elif wind_speed <= 72:
        force = 11
        specification = "Violent Storm"
    else:
        force = 12
        specification = "Hurricane"

print('A wind speed of {:.1f} mph corresponds to Force {} or {}'.format(wind_speed,force,specification))
print()
