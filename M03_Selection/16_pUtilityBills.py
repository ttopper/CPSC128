# pUtilityBills.py
# Kate Chatfield-Reed

print('''
=======================
    Bill Calculator
-----------------------''')
kwh = float(input('Enter kilowatt-hours used: '))
if kwh < 0:
    print('\nRecheck input value!')
    print("It was egative, and the meters\ndon't run backward.")
else:
    if kwh <= 500.0:
        amount = 20.0
    elif kwh <= 1000.0:
        amount = 20.0 + 0.03*(kwh-500)
    else:
        amount = 35.0 + 0.02*(kwh-1000)
print('Bill amount = ${:.2f}.'.format(amount))
