# Default shell for a Python 3.x program
#
__author__ = 'Nathaniel Smith'

# CIS-125-82A
# Distance
#
# This program promts the user for a distance measured in kilometers,
# converts it to miles and prints out the results.

def main ():
    K = eval(input("Please enter a distance in kilometers: "))
    M = K * 0.62
    print("The distance ", K, " in kilometers is equal to ", M, " miles.")
main ()