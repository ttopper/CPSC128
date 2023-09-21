# Example: One program to convert F to C _or_ C to F

Consider this program to convert temperatures in Fahrenheit to Celsius.

    print("This program converts temperatures from Fahrenheit to Celsius.")
    temp_in_f = int(input( "Enter a temperature in Fahrenheit (e.g. 10) and press Enter: " ))
    temp_in_c = (temp_in_f - 32) * 5 / 9
    print(temp_in_f, " degrees Fahrenheit = ", temp_in_c, " degrees Celsius.")

(For simplicity I have removed the opening comments).

If instead we wanted to convert temperatures in Celsius to Fahrenheit we
could write a second very similar program to do so:

    print("This program converts temperatures from Celsius to Fahrenheit .")
    temp_in_c= int(input( "Enter a temperature in Celsius (e.g. 10) and press Enter: " ))
    temp_in_f = temp_in_c * 9 / 5 + 32;
    print(temp_in_c, " degrees Celsius = ", temp_in_f, " degrees Fahrenheit.")

But what if we want a single program that can do either conversion? We
will need to place both sets of conversion code in one program and then
choose which one to execute. How will we choose? Based on user input,
i.e. we will present the choices and let the user choose. The resulting
program might look like this.

    ###########################################################
    ## tmpcnvrt.py -- allows the user to convert a temperature
    ##        in Fahrenheit to Celsius or vice versa.
    ##
    ## CPSC 128 Demonstration Program
    ##
    ## Kate Chatfield-Reed, Winter 2023
    ###########################################################
    print("This program converts temperatures from Fahrenheit to Celsius,")
    print("or from Celsius to Fahrenheit.")
    print("Choose")
    print("1 to convert Fahrenheit to Celsius")
    print("2 to convert Celsius to Fahrenheit")

    choice = int(input( "Your choice? " ))

    if choice == 1:
        print("This program converts temperatures from Fahrenheit to Celsius.")
        temp_in_f = int(input( "Enter a temperature in Fahrenheit (e.g. 10) and press Enter: " ))
        temp_in_c = (temp_in_f - 32) * 5 / 9
        print(temp_in_f, " degrees Fahrenheit = ", temp_in_c, " degrees Celsius.")

    elif choice == 2:
        print("This program converts temperatures from Celsius to Fahrenheit .")
        temp_in_c= int(input( "Enter a temperature in Celsius (e.g. 10) and press Enter: " ))
        temp_in_f = temp_in_c * 9 / 5 + 32
        print(temp_in_c, " degrees Celsius = ", temp_in_f, " degrees Fahrenheit.")

    else:
        print("Error: Your choice not recognized!")

The program begins by displaying a text menu offering the user numbered
choices. The user types a number and the program tests the number. If it
is a 1, the block of indented code after the `if` statement is executed,
and the blocks of code after the `elif` and `else` below it are skipped.

If it is not a 1, the block of indented code after the `if` is skipped,
and the `elif` is executed. If this test
is `True` (i.e. `choice` contains 2) the block of code after
the `elif` is executed, and the `else` is skipped.

If the value of `choice` is not 2, then the code after the `else` is
executed and the message `Error: Your choice not recognized` is
displayed.

Note that the block of code after the `if` and after the `elif` contain
several statements, so they must be consistently indented to turn them
into single compound statements.

Also, take careful note of the program formatting. The statements after
an `if`, `elif` or `else` are all indented 4 spaces.

In summary, this program selects one of three actions to carry out based
on user input.

-   If the initial value entered is 1, it performs a conversion from
    Fahrenheit to Celsius.
-   If the initial value entered is 2, it performs a conversion from
    Celsius to Fahrenheit.
-   If any other value is entered it displays an error message.

When more than one test is used to choose between multiple
possibilities, as above, the `if`, `elif`s and `else` are arranged in a
cascade. Our next program will illustrate how to create compound tests,
i.e. multiple comparisons combined with logical operators (`and`, `or`,
and `not`), and how to structure multiple `if`s efficiently in a
cascade.
