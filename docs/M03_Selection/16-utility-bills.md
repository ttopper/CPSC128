# Utility bills

## Problem:

A utility company takes readings each month and charges its customers on the following basis.

| kWh	    |   Rate |
|-----------|-----------------------------------|
| Under 500   | $20.00 |
| 500 to 1000 | $20.00 + $0.03 per kWh over 500 |
| Over 1000   | $35.00 + 0.02 per kWh above 1000 |


Write a program to calculate a customer's bill amount given the number of kilowatt-hours used.

Sample runs:

    ===============================
            Bill calculator
    -------------------------------
    Enter kilowatt-hours used: 300
    Bill amount = $20.00
    ===============================
            Bill calculator
    -------------------------------
    Enter kilowatt-hours used: 600
    Bill amount = $23.00
    ===============================
            Bill calculator
    -------------------------------
    Enter kilowatt-hours used: 1200
    Bill amount = $39.00

## Solution:

![Python code to calculate a utility bill at different
rates.](16_pUtilityBills_py.png)
