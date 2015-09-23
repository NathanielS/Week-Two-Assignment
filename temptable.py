# Default shell for a Python 3.x program
# Copy this and rename it to write your own code
#
__author__ = 'Nathaniel Smith'

# CIS-125-82A
# Temperature Table
#
# This program will use a loop to print a table of Celsius temperatures
# and the Fahrenheit equivalents every 10 degrees from 0C to 100C

def main ():
    for x in range(0,101,10):
        a = x * 9/5 + 32
        print(x,a)
main ()        