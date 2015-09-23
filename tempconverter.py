# Default shell for a Python 3.x program
#
__author__ = 'Nathaniel Smith'

# CIS-125-82A
# Temperature converter
#
# This program prompts the user for a temperature in Fahrenheit,
#converts it to Celsius, and prints out the results

def main ():
    F = eval(input("Please enter a temperature in Fahrenheit: "))
    C = (F - 32) * 5/9
    print("The temperature ", F, " in Fahrenheit is equal to ", C, " Celsius.")
main ()