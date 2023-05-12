# Sentinel controlled input

The previous program asked the user after each data value they input if they wanted to input another. This gets tiresome for the user who may have a long list of numbers they want to type in as quickly as possible.

Instead of asking after each value is input we could have them enter a special value, called a sentinel, to indicate the end of their data. Here's a program that uses -999 as a sentinel to indicate the end of the user input.

![Python program that displays the largest and smallest value entered.
It also uses a sentinel
value.](10_sentinel_input.py.png)

Extension challenge: But what if the number -999 occurs in the user's data set? Then our program will end prematurely. How could the program be modified to let the user enter the sentinel value before they begin entering their data?